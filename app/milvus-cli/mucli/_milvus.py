import csv
import os
import random
import urllib
from typing import List
import urllib.request

from click import (
    Choice,
    Group,
    Path,
    confirm,
    confirmation_option,
    echo,
    group,
    option,
    pass_context,
    pass_obj,
    password_option,
    prompt,
    version_option,
)
from click.core import Context
from click.types import IntParamType
from dotenv import load_dotenv

import milvus_connector
from milvus_connector.core._types import (
    CONSISTENCY_LEVEL_ARRAY,
    INDEX_TYPE_ARRAY,
    METRIC_TYPE_ARRAY,
)
from milvus_connector.core.util import (
    CollectionField,
    construct_data,
    convert_data,
    generate_random_data,
    ok,
)
from mucli._case import hello_milvus_case
from mucli._option import (
    collection_id,
    collection_name,
    compose,
    consistency_level,
    database_name,
    field_name,
    format_collection_field,
    get_auto_field,
    get_partition_key_field,
    index_name,
    partition_name,
    partition_names,
    replica_num,
    rolename,
    username,
)

SUB_COMMAND_GROUP = ["case", "proxy"]

# alias -> real command
ALIAS_CMD = {
    "collections": "show-collections",
    "collection": "describe-collection",
    "load": "load-collection",
    "list-collections": "show-collections",
    "partitions": "show-partitions",
    "list-partitions": "show-partitions",
    "index": "describe-index",
    "databases": "list-databases",
    "show-databases": "list-databases",
    "users": "select-user",
    "roles": "select-role",
}


class MilvusGroup(Group):
    def list_commands(self, ctx: Context) -> List[str]:
        cmds = super().list_commands(ctx)
        for sub_cmd in SUB_COMMAND_GROUP:
            if sub_cmd in cmds:
                cmds.remove(sub_cmd)
        cmds.extend(SUB_COMMAND_GROUP)
        return cmds

    def get_command(self, ctx, cmd_name):
        rv = Group.get_command(self, ctx, cmd_name)
        if rv is not None:
            return rv
        if ALIAS_CMD.get(cmd_name):
            rv = Group.get_command(self, ctx, ALIAS_CMD.get(cmd_name))
            if rv is not None:
                return rv
        matches = [x for x in self.list_commands(ctx) if cmd_name in x]
        if not matches:
            ctx.fail(f"Not such command: {cmd_name}")
            return None
        hints = "\n".join(sorted(matches))
        ctx.fail(f"Maybe you find:\n{hints}")

    def resolve_command(self, ctx, args):
        # always return the full command name
        _, cmd, args = super().resolve_command(ctx, args)
        return cmd.name, cmd, args


@group(
    cls=MilvusGroup,
    epilog="Check out our docs at https://milvus.io/docs for more milvus details",
)
@version_option(version="0.0.1")
@option(
    "-u",
    "--uri",
    default=lambda: os.environ.get("MILVUS_URI", "localhost:19530"),
    show_default="localhost:19530",
    prompt="Milvus connection uri",
    prompt_required=False,
    help="Milvus connection uri",
)
@option(
    "-t",
    "--token",
    default=lambda: os.environ.get("MILVUS_TOKEN", "root:Milvus"),
    show_default="root:Milvus",
    prompt="Milvus connection token",
    prompt_required=False,
    help="Milvus connection token",
)
@option(
    "-d",
    "--database",
    default=lambda: os.environ.get("MILVUS_DATABASE", "default"),
    show_default="default",
    prompt="Milvus connection database",
    prompt_required=False,
    help="Milvus connection database",
)
@option(
    "-e",
    "--env",
    type=Path(),
    show_default=".env",
    prompt="Milvus connection database",
    prompt_required=False,
    help="Path to milvus .env file",
)
@pass_context
def milvus_cli(ctx, uri, token, database, env):
    """This is a pure and easy python CLI tool to interact with Milvus."""
    if env:
        if os.path.exists(env):
            load_dotenv(env)
            uri = os.getenv("MILVUS_URI", uri)
            token = os.getenv("MILVUS_TOKEN", token)
            database = os.getenv("MILVUS_DATABASE", database)
        else:
            ctx.fail(f"File not found: {env}")
    ctx.obj = lambda: milvus_connector.Milvus(uri=uri, token=token, database=database)


@milvus_cli.command()
@pass_obj
def show_collections(cli):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(client.json().show_collections())


@compose(
    milvus_cli.command(short_help="Create collection"),
    collection_name(),
    option(
        "-sn",
        "--shard-num",
        type=IntParamType(),
        default=1,
        show_default=True,
        prompt="Shard num",
        prompt_required=False,
        help="Shard num",
    ),
    option(
        "-cl",
        "--consistency-level",
        default="bounded",
        show_default=True,
        type=Choice(CONSISTENCY_LEVEL_ARRAY, case_sensitive=False),
        prompt_required=False,
        prompt="Consistency level",
        help="Consistency level",
    ),
    option(
        "-cd",
        "--collection-description",
        default="",
        show_default=True,
        type=str,
        prompt_required=False,
        prompt="Collection description",
        help="Collection description",
    ),
    option(
        "-ai",
        "--auto-id",
        type=bool,
        default=False,
        show_default=True,
        prompt_required=False,
        prompt="Auto id",
        help="Auto id",
    ),
    option(
        "-ed",
        "--enable-dynamic-field",
        type=bool,
        default=False,
        show_default=True,
        prompt_required=False,
        prompt="Enable dynamic field",
        help="Enable dynamic field",
    ),
    option(
        "-p",
        "--property",
        "props",
        multiple=True,
        help="Collection properties, format: [key]:[value]",
    ),
    option(
        "-pk",
        "--pk-field",
        prompt="Collection pk field",
        prompt_required=False,
        help="Collection pk field, format: name:[field_name];dtype:[data_type];desc:[field_description];auto_id:false",
    ),
    option(
        "-f",
        "--field",
        "fields",
        multiple=True,
        help="Collection field, format: name:[field_name];dtype:[data_type];desc:[field_description];dim:[vector_dim];is_partition_key:false",
    ),
    option(
        "--auto-field", type=bool, help="quick fields, include: pk, random, embedding[vector:128]"
    ),
    option(
        "--auto-partition", type=bool, help="quick fields should include partition key field or not"
    ),
    option("--auto-dim", type=int, default=32, help="quick fields vector dim"),
)
@pass_obj
def create_collection(
    cli,
    name,
    shard_num,
    consistency_level,
    collection_description,
    auto_id,
    enable_dynamic_field,
    props,
    pk_field,
    fields,
    auto_field,
    auto_partition,
    auto_dim,
):
    """create collection, param hints:

    the field format:\n
        key1:value1;key2:value2...

    the field key options:\n
        name,dtype,desc,auto_id,dim,max_length,is_partition_key

    dtype options:\n
    \b
        "bool",
        "int8", "int16", "int32", "int64",
        "float", "double",
        "string", "varchar",
        "array", "json",
        "binary_vector", "float_vector", "float16_vector", "bfloat16_vector", "sparse_vector",
    """
    client: milvus_connector.Milvus = cli()
    with client:
        fields_obj = []
        if auto_field:
            fields_obj.extend(get_auto_field(dim=auto_dim, auto_id=auto_id))
            if auto_partition:
                fields_obj.append(get_partition_key_field())
        else:
            pk_obj = CollectionField(**format_collection_field(pk_field))
            fields_obj.append(pk_obj)
            for f in fields:
                field_obj = CollectionField(**format_collection_field(f))
                fields_obj.append(field_obj)
        echo(
            client.json().create_collection(
                collection_name=name,
                shard_num=shard_num,
                consistency_level=consistency_level,
                collection_description=collection_description,
                auto_id=True if auto_id else False,
                enable_dynamic_field=True if enable_dynamic_field else False,
                properties=props if props else {},
                fields=fields_obj,
            )
        )


@compose(
    milvus_cli.command(),
    collection_name(prompt_required=False),
    collection_id(),
    option(
        "-p",
        "--property",
        "props",
        multiple=True,
        help="Collection properties, format: [key]:[value]",
    ),
)
@pass_obj
def alter_collection(cli, name, cid, props):
    client: milvus_connector.Milvus = cli()
    with client:
        if name and cid:
            echo("Please only provide either collection name or collection id")
            return
        if not name and not cid:
            collection_name = prompt("Collection name")
        if len(props) == 0:
            echo(
                "Please must provide one or more collection properties, like: -p key1:value1 -p key2:value2"
            )
            return
        properties = []
        for p in props:
            res = p.split(":")
            if len(res) != 2:
                echo(f"Invalid property format: {p}, should be [key]:[value]")
                return
            k, v = res
            properties.append({k: v})
        if collection_name or cid:
            echo(client.json().alter_collection(collection_name=name, collection_id=cid))


@compose(
    milvus_cli.command(),
    collection_name(prompt_required=False),
    collection_id(),
)
@pass_obj
def describe_collection(cli, name, cid):
    client: milvus_connector.Milvus = cli()
    with client:
        if name and cid:
            echo("Please only provide either collection name or collection id")
            return
        if not name and not cid:
            name = prompt("Collection name")
        if name or cid:
            echo(client.json().describe_collection(collection_name=name, collection_id=cid))
        else:
            echo("Please provide valid collection name or collection id")


@compose(
    milvus_cli.command(),
    collection_name(),
)
@pass_obj
def collection_statistics(cli, name):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(client.json().get_collection_statistics(collection_name=name))


@compose(
    milvus_cli.command(),
    collection_name(),
    partition_name(),
    option("-df", "--data-file", type=Path(), prompt_required=False, help="Vector data csv file"),
    option("-rd", "--random-data", type=bool, default=False, help="Random vector search"),
    option("-rn", "--random-num", type=int, default=2000, help="Random vector num"),
)
@pass_obj
def insert(cli, name, partition_name, data_file, random_data, random_num):
    client: milvus_connector.Milvus = cli()
    with client:
        insert_data = []
        num_row = 0
        if random_data:
            collection_info = client.describe_collection(collection_name=name)
            if not ok(collection_info.status):
                echo(f"fail to get collection info, status: {collection_info.status}")
                return
            for field in collection_info.schema.fields:
                if field.autoID:
                    continue
                dim = next(
                    (
                        int(type_param.value)
                        for type_param in field.type_params
                        if type_param.key == "dim"
                    ),
                    0,
                )
                insert_data.append(
                    generate_random_data(random_num, field.name, field.data_type, dim=dim)
                )
            num_row = random_num
        else:
            if data_file and not os.path.exists(data_file):
                echo(f"File not found: {data_file}")
                return
            collection_info = client.describe_collection(collection_name=name)
            if not ok(collection_info.status):
                echo(f"fail to get collection info, status: {collection_info.status}")
                return
            with open(data_file, "r", newline="") as file:
                reader = csv.reader(file)
                header = next(reader)
                data = list(reader)
            num_row = len(data)
            file_data = {}
            field_type_map = {}
            for field in collection_info.schema.fields:
                field_type_map[field.name] = field.data_type
            for row in data:
                row_data = row.split(",")
                for index, column_data in enumerate(row_data):
                    file_field_name = header[index]
                    field_type = field_type_map.get(file_field_name, None)
                    if field_type is None:
                        echo(f"Field not found: {file_field_name}")
                        return
                    if file_field_name not in file_data:
                        file_data[file_field_name] = []
                    file_data[file_field_name].append(convert_data(field_type, column_data))
            for field_name, field_data in file_data.items():
                insert_data.append(
                    construct_data(field_name, field_type_map[field_name], field_data)
                )
        echo(
            client.json().insert(
                collection_name=name,
                partition_name=partition_name,
                fields_data=insert_data,
                num_rows=num_row,
            )
        )


@compose(
    milvus_cli.command(),
    collection_name(),
    partition_name(),
    option("-e", "--expr", prompt="Expr", help="Expr"),
)
@pass_obj
def delete(cli, name, partition_name, expr):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(
            client.json().delete(
                collection_name=name,
                partition_name=partition_name,
                expr=expr,
            )
        )


@compose(
    milvus_cli.command(),
    collection_name(),
    partition_names(),
    option("-e", "--expr", prompt_required=False, prompt="Expr", help="Expr"),
    option("-f", "--field", "fields", multiple=True, help="Fields"),
    option(
        "-vf",
        "--vector-field-name",
        default="embedding",
        prompt_required=False,
        prompt="Vector field name",
        help="Vector field name",
    ),
    option("-tk", "--topk", type=int, default=10, help="Topk"),
    option(
        "-mt",
        "--metric-type",
        type=Choice(METRIC_TYPE_ARRAY, case_sensitive=False),
        default="L2",
        help="Metric type",
    ),
    option(
        "-vd",
        "--vector-data-file",
        type=Path(),
        prompt_required=False,
        prompt="Vector data file",
        help="Vector data file",
    ),
    option("-ri", "--random-vector", type=bool, default=False, help="Random vector search"),
)
@pass_obj
def search(
    cli,
    name,
    partition_names,
    expr,
    fields,
    vector_field_name,
    topk,
    metric_type,
    vector_data_file,
    random_vector,
):
    client: milvus_connector.Milvus = cli()
    with client:
        if len(fields) == 0:
            echo("Please provide one or more fields, like: -f field1 -f field2")
            return
        if vector_data_file and not os.path.exists(vector_data_file):
            echo(f"File not found: {vector_data_file}")
            return
        if random_vector:
            collection_info = client.describe_collection(collection_name=name)
            if not ok(collection_info.status):
                echo(f"fail to get collection info, status: {collection_info.status}")
                return
            vector_data = None
            real_vector_field = None
            for field in collection_info.schema.fields:
                if field.name == vector_field_name:
                    for type_param in field.type_params:
                        if type_param.key == "dim":
                            # TODO it need to be random diff type according to the data type
                            vector_data = [random.random() for _ in range(int(type_param.value))]
                            break
                elif vector_data:
                    break
                else:
                    if any([type_param.key == "dim" for type_param in field.type_params]):
                        real_vector_field = field.name
            if not vector_data:
                echo(
                    f"Vector field not found: {vector_field_name}, dected vector field: {real_vector_field}"
                )
                return
            vector_data = [vector_data]
        else:
            if not vector_data_file:
                echo("Please provide vector data file or use the --random-vector option")
                return
            with open(vector_data_file, "r") as f:
                file_content = f.readlines()
                file_content = [line.strip() for line in file_content]
                # TODO it need to use the diff convert func according to the data type
                vector_data = [list(map(float, line.split(","))) for line in file_content]
        echo(
            client.json().search(
                req=client.construct_search_request(
                    collection_name=name,
                    partition_names=partition_names,
                    expr=expr,
                    output_fields=fields,
                    vector_field=vector_field_name,
                    top_k=topk,
                    metric_type=metric_type,
                    search_data=vector_data,
                ),
            )
        )


@compose(
    milvus_cli.command(),
    collection_name(),
    partition_names(),
    option("-e", "--expr", prompt="Expr", help="Expr"),
    option("-f", "--field", "fields", multiple=True, help="Fields"),
    option("-l", "--limit", default=-1, type=int, help="Limit"),
    consistency_level(),
    option(
        "-qp",
        "--query-param",
        "query_params",
        multiple=True,
        help="Query params, format: [key]:[value]",
    ),
)
@pass_obj
def query(cli, name, partition_names, expr, fields, limit, consistency_level, query_params):
    client: milvus_connector.Milvus = cli()
    with client:
        if len(fields) == 0:
            echo("Please provide one or more fields, like: -f field1 -f field2")
            return
        _query_params = {}
        if len(query_params) > 0:
            for qp in query_params:
                res = qp.split(":")
                if len(res) != 2:
                    echo(f"Invalid query param format: {qp}, should be [key]:[value]")
                    return
                k, v = res
                _query_params[k] = v
        echo(
            client.json().query(
                collection_name=name,
                partition_names=partition_names,
                expr=expr,
                output_fields=fields,
                limit=limit,
                consistency_level=consistency_level,
                query_params=_query_params,
            )
        )


@compose(
    milvus_cli.command(),
    collection_name(),
    partition_names(),
    option("-e", "--expr", default="", prompt_required=False, prompt="Expr", help="Expr"),
)
@pass_obj
def query_star(cli, name, partition_names, expr):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(
            client.json().query(
                collection_name=name,
                partition_names=partition_names,
                expr=expr,
                output_fields=["count(*)"],
                consistency_level="strong",
            )
        )


@compose(
    milvus_cli.command(),
    collection_name(),
    index_name(),
    field_name(prompt_required=False),
    option(
        "-it",
        "--index-type",
        type=Choice(INDEX_TYPE_ARRAY, case_sensitive=False),
        default="IVF_FLAT",
        prompt_required=False,
        prompt="Index type",
        help="Index type",
    ),
    option(
        "-mt",
        "--metric-type",
        type=Choice(METRIC_TYPE_ARRAY, case_sensitive=False),
        default="L2",
        prompt_required=False,
        prompt="Metric type",
        help="Metric type",
    ),
    option(
        "-nl", "--nlist", type=int, default=128, prompt_required=False, prompt="Nlist", help="Nlist"
    ),
)
@pass_obj
def create_index(cli, name, index_name, field_name, index_type, metric_type, nlist):
    client: milvus_connector.Milvus = cli()
    with client:
        if field_name is None:
            collection_info = client.describe_collection(collection_name=name)
            if not ok(collection_info.status):
                echo(f"fail to get collection info, status: {collection_info.status}")
                return
            for field in collection_info.schema.fields:
                if any([type_param.key == "dim" for type_param in field.type_params]):
                    field_name = field.name
        echo(
            client.json().create_index(
                collection_name=name,
                index_name=index_name,
                field_name=field_name,
                index_type=index_type,
                metric_type=metric_type,
                nlist=nlist,
            )
        )


@compose(
    milvus_cli.command(),
    collection_name(),
)
@pass_obj
def drop_index(cli, name):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(client.json().drop_index(collection_name=name))


@compose(
    milvus_cli.command(),
    collection_name(),
)
@pass_obj
def describe_index(cli, name):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(client.json().describe_index(collection_name=name))


@compose(
    milvus_cli.command(),
    collection_name(),
    replica_num(),
)
@pass_obj
def load_collection(cli, name, num):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(client.json().load_collection(collection_name=name, replica_number=num))


@compose(milvus_cli.command(), collection_name(), partition_names())
@pass_obj
def load_state(cli, name, partition_names):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(client.json().get_load_state(collection_name=name, partition_names=partition_names))


@compose(milvus_cli.command(), collection_name(), partition_names())
@pass_obj
def load_progress(cli, name, partition_names):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(
            client.json().get_loading_progress(
                collection_name=name, partition_names=partition_names
            )
        )

@compose(milvus_cli.command(), collection_name())
@pass_obj
def get_replicas(cli, name):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(client.json().get_replicas(collection_name=name))

@compose(
    milvus_cli.command(),
    collection_name(),
)
@pass_obj
def release_collection(cli, name):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(client.json().release_collection(collection_name=name))


@compose(
    milvus_cli.command(),
    collection_name(multiple=True),
)
@pass_obj
def flush(cli, name):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(client.json().flush(collection_names=name))


@compose(
    milvus_cli.command(),
    collection_name(),
)
@pass_obj
def flush_state(cli, name):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(client.json().get_flush_state(collection_name=name))


@compose(
    milvus_cli.command(),
)
@pass_obj
def flush_all(cli):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(client.json().flush_all())


@compose(
    milvus_cli.command(),
)
@pass_obj
def flush_all_state(cli):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(client.json().get_flush_all_state())


@compose(milvus_cli.command(), collection_name(), partition_name())
@pass_obj
def create_partition(cli, name, partition_name):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(client.json().create_partition(collection_name=name, partition_name=partition_name))


@compose(
    milvus_cli.command(),
    collection_name(),
    partition_name(),
    confirmation_option("-f", "--force", prompt="Are you sure you want to drop the collection?"),
)
@pass_obj
def drop_partition(cli, name, partition_name, force):
    client: milvus_connector.Milvus = cli()
    with client:
        drop = True
        if not force:
            drop = confirm(f"Drop partition <{partition_name}> ?")
        if drop:
            echo(client.json().drop_partition(collection_name=name, partition_name=partition_name))


@compose(
    milvus_cli.command(),
    collection_name(),
    partition_names(),
    replica_num(),
)
@pass_obj
def load_partitions(cli, name, partition_names, num):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(
            client.json().load_partitions(
                collection_name=name,
                partition_names=partition_names,
                replica_number=num,
            )
        )


@compose(
    milvus_cli.command(),
    collection_name(),
    partition_names(),
)
@pass_obj
def release_partitions(cli, name, partition_names):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(
            client.json().release_partitions(
                collection_name=name,
                partition_names=partition_names,
            )
        )


@compose(milvus_cli.command(), collection_name(), collection_id())
@pass_obj
def show_partitions(cli, name, cid):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(
            client.json().show_partitions(
                collection_name=name,
                collection_id=cid,
            )
        )


@compose(milvus_cli.command(), collection_name(), partition_name())
@pass_obj
def partition_statistics(cli, name, partition_name):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(
            client.json().get_partition_statistics(
                collection_name=name,
                partition_name=partition_name,
            )
        )


@compose(
    milvus_cli.command(),
    collection_name(),
    collection_id(),
)
@pass_obj
def compact(cli, name, cid):
    client: milvus_connector.Milvus = cli()
    with client:
        if cid:
            echo(client.json().compaction(collection_id=cid))
        else:
            rsp = client.describe_collection(collection_name=name)
            if ok(rsp.status):
                echo(client.json().compaction(collection_id=rsp.collectionID))
            else:
                echo(rsp)


@compose(
    milvus_cli.command(),
    option("-c", "--compaction-id", prompt="Compaction id", help="Compaction id"),
)
@pass_obj
def compact_state(cli, compaction_id):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(client.json().get_compaction_state(compaction_id=compaction_id))


@compose(
    milvus_cli.command(),
    option("-c", "--compaction-id", prompt="Compaction id", help="Compaction id"),
)
@pass_obj
def compact_state_with_plans(cli, compaction_id):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(client.json().get_compaction_state_with_plans(compaction_id=compaction_id))


@compose(
    milvus_cli.command(),
    collection_name(),
    confirmation_option(
        "-f", "--force", default=False, prompt="Are you sure you want to drop the collection?"
    ),
)
@pass_obj
def drop_collection(cli, name):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(client.json().drop_collection(collection_name=name))


@compose(
    milvus_cli.command(),
    username(),
    password_option(),
)
@pass_obj
def create_user(cli, username, password):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(
            client.json().create_user(
                username=username,
                password=password,
            )
        )


@compose(
    milvus_cli.command(),
    username(),
)
@pass_obj
def drop_user(cli, username):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(client.json().delete_user(username=username))


@compose(
    milvus_cli.command(),
    username(),
    password_option("-op", "--old-password", prompt="Old password", help="Old password"),
    password_option("-np", "--new-password", prompt="New password", help="New password"),
)
@pass_obj
def update_password(cli, username, old_password, new_password):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(
            client.json().update_user(
                username=username,
                old_password=old_password,
                new_password=new_password,
            )
        )


@compose(
    milvus_cli.command(),
)
@pass_obj
def list_users(cli):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(client.json().list_users())


@compose(
    milvus_cli.command(),
    rolename(),
)
@pass_obj
def create_role(cli, rolename):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(
            client.json().create_role(
                role_name=rolename,
            )
        )


@compose(
    milvus_cli.command(),
    rolename(),
)
@pass_obj
def drop_role(cli, rolename):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(
            client.json().delete_role(
                role_name=rolename,
            )
        )


@compose(
    milvus_cli.command(),
    username(),
    rolename(),
    option("--add/--no-add", " /--remove", default=True, help="Add or remove user to role"),
)
@pass_obj
def operate_user_role(cli, username, rolename, add):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(
            client.json().operate_user_role(
                username=username,
                role_name=rolename,
                action="add_user_to_role" if add else "remove_user_from_role",
            )
        )


@compose(
    milvus_cli.command(),
    username(prompt_required=False),
    option("--include/--no-include", default=False, help="Include the role information or not"),
)
@pass_obj
def select_user(cli, username, include):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(
            client.json().select_user(
                username=username,
                include_role_info=include,
            )
        )


@compose(
    milvus_cli.command(),
    rolename(prompt_required=False),
    option("--include/--no-include", default=False, help="Include the user information or not"),
)
@pass_obj
def select_role(cli, rolename, include):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(
            client.json().select_role(
                role_name=rolename,
                include_user_info=include,
            )
        )


@compose(
    milvus_cli.command(),
    database_name(),
    rolename(),
    option("-on", "--object-name", prompt="Object name", help="Object name"),
    option(
        "-ot",
        "--object-type",
        type=Choice(
            [
                "collection",
                "global",
                "user",
            ],
            case_sensitive=False,
        ),
        prompt="Object type",
        help="Object type",
    ),
    option("--grant/--no-grant", " /--revoke", default=True, help="Grant or revoke the privilege"),
    option("-p", "--privilege", prompt="Privilege", help="Privilege"),
)
@pass_obj
def operate_privilege(cli, database, rolename, object_name, object_type, grant, privilege):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(
            client.json().operate_privilege(
                db_name=database,
                role_name=rolename,
                object_name=object_name,
                object_type=object_type,
                action="grant" if grant else "revoke",
                privilege=privilege,
            )
        )


@compose(
    milvus_cli.command(),
    database_name(),
    rolename(),
    option("-on", "--object-name", prompt_required=False, prompt="Object name", help="Object name"),
    option(
        "-ot",
        "--object-type",
        prompt_required=False,
        type=Choice(
            [
                "collection",
                "global",
                "user",
            ],
            case_sensitive=False,
        ),
        prompt="Object type",
        help="Object type",
    ),
    option("-p", "--privilege", prompt_required=False, prompt="Privilege", help="Privilege"),
)
@pass_obj
def select_grant(cli, database, rolename, object_name, object_type, privilege):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(
            client.json().select_grant(
                db_name=database,
                role_name=rolename,
                object_name=object_name,
                object_type=object_type,
                privilege=privilege,
            )
        )


@compose(
    milvus_cli.command(),
    database_name(),
)
@pass_obj
def create_database(cli, database):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(client.json().create_database(db_name=database))


@compose(
    milvus_cli.command(),
    database_name(),
)
@pass_obj
def drop_database(cli, database):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(client.json().drop_database(db_name=database))


@compose(
    milvus_cli.command(),
)
@pass_obj
def list_databases(cli):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(client.json().list_databases())


@compose(
    milvus_cli.command(),
    option("-c", "--channel-name", prompt="Channel name", help="Channel name"),
)
@pass_obj
def replicate_message(cli, channel_name):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(client.json().replicate_message(channel_name=channel_name))


@compose(
    milvus_cli.command(),
)
@pass_obj
def get_version(cli):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(client.json().get_version())


@compose(
    milvus_cli.command(),
)
@pass_obj
def check_health(cli):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(client.json().check_health())


@compose(
    milvus_cli.command(),
)
@pass_obj
def connect(cli):
    client: milvus_connector.Milvus = cli()
    with client:
        echo(client.json().connect())


@compose(
    milvus_cli.command(),
    option("-u", "--uri", prompt_required=False,
           prompt="URI", help="URI", default="http://localhost:9091"),
    option("-a", "--auth", prompt_required=False,
           prompt="Auth key", help="Auth key", default="by-dev"),
    option("-e", "--expr", prompt_required=False,
           prompt="Expr", help="Expr", default="param.ProxyCfg.MaxUserNum.GetValue()"),
)
@pass_obj
def expr(cli, uri, auth, expr):
    url = f"{uri}/expr?auth={auth}&code={expr}"
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
    echo(content)


@compose(
    milvus_cli.command(),
    option("-u", "--uri", prompt_required=False,
           prompt="URI", help="URI", default="http://localhost:9091"),
    option("-a", "--auth", prompt_required=False,
           prompt="Auth key", help="Auth key", default="by-dev"),
    option("-f", "--filter", prompt_required=False,
           prompt="Filter world", help="Filter world", default="proxy.maxNameLength"),
)
@pass_obj
def get_config(cli, uri, auth, filter):
    component = filter.split(".")[0]
    url = f'{uri}/expr?auth={auth}&code=param.GetComponentConfigurations("{component}","{filter}")'
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
    echo(content)


@compose(
    milvus_cli.command(),
    option("-u", "--uri", prompt_required=False,
           prompt="URI", help="URI", default="http://localhost:9091"),
    option("-a", "--auth", prompt_required=False,
           prompt="Auth key", help="Auth key", default="by-dev"),
    option("-k", "--key", prompt_required=False,
           prompt="Config key", help="Config Key", default="proxy.maxNameLength"),
    option("-v", "--value", prompt_required=False,
           prompt="Config value", help="Config value", default="256"),
)
@pass_obj
def set_config(cli, uri, auth, key, value):
    url = f'{uri}/expr?auth={auth}&code=param.Save("{key}","{value}")'
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
    echo(content)


@milvus_cli.group()
def proxy():
    """[group] proxy inner command"""
    pass


@proxy.command()
def get_metric():
    echo("Metric")


@milvus_cli.group()
@pass_obj
def case(cli):
    """[group] milvus quick case command"""
    pass


@case.command()
@pass_obj
def hello_milvus(cli):
    hello_milvus_case(cli)


@milvus_cli.group()
@option("-u", "--uri",
        prompt_required=False, prompt="URI", help="URI", default="http://localhost:21123")
@pass_context
def query_node(ctx, uri):
    """[group] query node inner command"""
    ctx.obj = lambda: milvus_connector.QueryNode(uri=uri)


@query_node.command()
@pass_obj
def get_data_distribution(cli):
    client: milvus_connector.QueryNode = cli()
    with client:
        echo(client.json().get_data_distribution())


@query_node.command()
@option("-m", "--metric-type", prompt_required=False,
        prompt="Metric type", help="Metric type", default="system_info")
@pass_obj
def query_node_metric(cli, metric_type):
    client: milvus_connector.QueryNode = cli()
    with client:
        echo(client.json().get_metric(metric_type=metric_type))


@query_node.command()
@option("-p", "--pattern",
        prompt_required=False, default="", prompt="Config", help="Config")
@pass_obj
def query_node_configs(cli, pattern):
    client: milvus_connector.QueryNode = cli()
    with client:
        echo(client.json().show_configs(pattern=pattern))


@query_node.command()
@option("-s", "--segment-id", "segment-ids", multiple=True, prompt="Segment id", help="Segment id")
@pass_obj
def get_segment_info(cli, segment_ids):
    client: milvus_connector.QueryNode = cli()
    with client:
        echo(client.json().get_segment_info(segment_ids=segment_ids))
