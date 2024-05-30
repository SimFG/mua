import json
from typing import Any, Dict, List

from click import Choice, option
from click.types import IntParamType

from milvus_connector.core._types import (
    CONSISTENCY_LEVEL_ARRAY,
)
from milvus_connector.core.util import CollectionField


def database_name(*args, **kwargs):
    if not args:
        args = ("-d", "--database")
    kwargs.setdefault("prompt_required", False)
    kwargs.setdefault("prompt", "Database name")
    kwargs.setdefault("help", "Database name")
    return option(*args, **kwargs)


def collection_name(*args, **kwargs):
    if not args:
        args = ("-n", "--name")
    kwargs.setdefault("prompt", "Collection name")
    kwargs.setdefault("help", "Collection name")
    return option(*args, **kwargs)


def collection_id(*args, **kwargs):
    if not args:
        args = ("-i", "--cid")
    kwargs.setdefault("prompt_required", False)
    kwargs.setdefault("prompt", "Collection id")
    kwargs.setdefault("help", "Collection id")
    return option(*args, **kwargs)


def partition_name(*args, **kwargs):
    if not args:
        args = ("-p", "--partition-name")
    kwargs.setdefault("default", "")
    kwargs.setdefault("prompt_required", False)
    kwargs.setdefault("prompt", "Partition name")
    kwargs.setdefault("help", "Partition name")
    return option(*args, **kwargs)


def partition_names(*args, **kwargs):
    if not args:
        args = ("-p", "--partition-names")
    kwargs.setdefault("prompt_required", False)
    kwargs.setdefault("multiple", True)
    kwargs.setdefault("help", "Partition names")
    return option(*args, **kwargs)


def index_name(*args, **kwargs):
    if not args:
        args = ("-in", "--index-name")
    kwargs.setdefault("prompt_required", False)
    kwargs.setdefault("prompt", "Index name")
    kwargs.setdefault("help", "Index name")
    return option(*args, **kwargs)


def field_name(*args, **kwargs):
    if not args:
        args = ("-fn", "--field-name")
    kwargs.setdefault("prompt", "Field name")
    kwargs.setdefault("help", "Field name")
    return option(*args, **kwargs)


def consistency_level(*args, **kwargs):
    if not args:
        args = ("-cl", "--consistency-level")
    kwargs.setdefault("type", Choice(CONSISTENCY_LEVEL_ARRAY, case_sensitive=False))
    kwargs.setdefault("default", "bounded")
    kwargs.setdefault("show_default", True)
    kwargs.setdefault("prompt_required", False)
    kwargs.setdefault("prompt", "Consistency level")
    kwargs.setdefault("help", "Consistency level")
    return option(*args, **kwargs)


def replica_num(*args, **kwargs):
    if not args:
        args = ("-r", "--replica-num", "num")
    kwargs.setdefault("prompt_required", False)
    kwargs.setdefault("prompt", "Replica num")
    kwargs.setdefault("type", IntParamType())
    kwargs.setdefault("default", 1)
    kwargs.setdefault("help", "Replica num")
    return option(*args, **kwargs)


def username(*args, **kwargs):
    if not args:
        args = ("-u", "--username")
    kwargs.setdefault("prompt", "Username")
    kwargs.setdefault("help", "Username")
    return option(*args, **kwargs)


def rolename(*args, **kwargs):
    if not args:
        args = ("-r", "--rolename")
    kwargs.setdefault("prompt", "Role name")
    kwargs.setdefault("help", "Role name")
    return option(*args, **kwargs)


# format_collection_field, v format:
# name:pk;
# is_primary_key:true;
# auto_id:true;
# is_dynamic:false;
# is_partition_key:false;
# dtype:int32;
# dim:16;
# params:{"nbits": 32}
def format_collection_field(v: str) -> Dict[str, Any]:
    atts = v.split(";")
    field_att = {}
    for att in atts:
        if len(att.split(":")) != 2:
            raise ValueError(f"Invalid field format: {v}")
        k, v = att.split(":")
        if k in ("is_primary_key", "auto_id", "is_dynamic", "is_partition_key", "is_cluster_key"):
            v = True if v else False
        elif k == "params":
            v = json.loads(v)
        elif k in ("dim", "max_length"):
            v = int(v)
        elif k == "desc":
            v = v.strip('"').strip("'")
        field_att[k] = v
    return field_att


def get_auto_field(dim: int = 32, auto_id: bool = False) -> List[CollectionField]:
    return [
        CollectionField(
            name="pk",
            is_primary_key=True,
            auto_id=auto_id,
            dtype="int64",
            desc="it's the pk field",
        ),
        CollectionField(
            name="random",
            dtype="varchar",
            desc="it's random string field",
            max_length=32,
        ),
        CollectionField(
            name="embedding",
            dtype="float_vector",
            desc="it's vector float field",
            dim=dim,
        ),
    ]


def get_partition_key_field() -> CollectionField:
    return CollectionField(
        name="partition_key",
        dtype="int64",
        desc="it's partition key int64 field",
        is_partition_key=True,
    )


def compose(*decorators):
    def wrapper(func, *args, **kwargs):
        for decorator in decorators:
            func = decorator(func, *args, **kwargs)
        return func

    return wrapper
