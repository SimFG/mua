import random
import time

from click import echo

import milvus_connector
from milvus_connector.core.util import generate_random_data, ok
from milvus_connector.protocol.common_pb2 import LoadStateLoaded
from mucli._option import (
    get_auto_field,
    get_partition_key_field,
)


def hello_milvus_case(cli):
    client: milvus_connector.Milvus = cli()
    with client:
        name = "hello_milvus"

        echo("create `hello_milvus` collection")
        fields_obj = []
        fields_obj.extend(get_auto_field())
        fields_obj.append(get_partition_key_field())
        create_resp = client.create_collection(
            collection_name=name,
            shard_num=1,
            consistency_level="strong",
            collection_description="hello_milvus",
            fields=fields_obj,
        )
        if not ok(create_resp):
            echo(f"create collection fail: {create_resp}")
            return

        echo("insert data to `hello_milvus` collection")
        insert_data = []
        num_row = 0
        random_num = 2000
        collection_info = client.describe_collection(collection_name=name)
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
        insert_resp = client.insert(
            collection_name=name,
            fields_data=insert_data,
            num_rows=num_row,
        )
        if not ok(insert_resp.status):
            echo(f"insert data fail: {insert_resp}")
            return

        echo("flush `hello_milvus` collection")
        flush_resp = client.flush(collection_names=[name])
        if not ok(flush_resp.status):
            echo(f"flush collection fail: {flush_resp}")
            return

        echo("create index for `hello_milvus` collection")
        create_index_resp = client.create_index(
            collection_name=name,
            field_name="embedding",
            index_name="embedding_index",
        )
        if not ok(create_index_resp):
            echo(f"create index fail: {create_index_resp}")
            return

        echo("load `hello_milvus` collection")
        load_resp = client.load_collection(collection_name=name)
        if not ok(load_resp):
            echo(f"load collection fail: {load_resp}")
            return

        echo("wait for loading `hello_milvus` collection")
        load_state_resp = client.get_load_state(collection_name=name)
        while load_state_resp.state != LoadStateLoaded:
            echo(f"load state: {load_state_resp.state}")
            time.sleep(0.5)
            load_state_resp = client.get_load_state(collection_name=name)

        echo("search `hello_milvus` collection")
        search_resp = client.search(
            req=client.construct_search_request(
                collection_name=name,
                expr="pk > 0",
                output_fields=["pk", "random"],
                vector_field="embedding",
                search_data=[[random.random() for _ in range(32)]],
            )
        )
        if not ok(search_resp.status):
            echo(f"search collection fail: {search_resp}")
            return

        echo("delete `hello_milvus` collection")
        delete_resp = client.delete(collection_name=name, expr="pk > 100")
        if not ok(delete_resp.status):
            echo(f"delete collection fail: {delete_resp}")
            return

        echo("query `hello_milvus` collection")
        query_resp = client.query(collection_name=name, expr="pk > 1000")
        if not ok(query_resp.status):
            echo(f"query collection fail: {query_resp}")
            return

        echo("show collections")
        show_collections_resp = client.show_collections()
        if not ok(show_collections_resp.status):
            echo(f"show collections fail: {show_collections_resp}")
            return

        echo("release `hello_milvus` collection")
        release_resp = client.release_collection(collection_name=name)
        if not ok(release_resp):
            echo(f"release collection fail: {release_resp}")
            return

        echo("drop index for `hello_milvus` collection")
        drop_index_resp = client.drop_index(collection_name=name, index_name="embedding_index")
        if not ok(drop_index_resp):
            echo(f"drop index fail: {drop_index_resp}")
            return

        echo("drop `hello_milvus` collection")
        drop_resp = client.drop_collection(collection_name=name)
        if not ok(drop_resp):
            echo(f"drop collection fail: {drop_resp}")
            return
