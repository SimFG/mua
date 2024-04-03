from typing import Literal, Union
from ..protocol.common_pb2 import *
from ..protocol.schema_pb2 import *

# not stable type
CONSISTENCY_LEVEL = Union[str, Literal[
                            "strong",
                            "session",
                            "bounded",
                            "eventually",
                            "customized",
                            ]]

CONSISTENCY_LEVEL_ARRAY = [
    "strong",
    "session",
    "bounded",
    "eventually",
    "customized",
    ]

DTYPE = Union[str, Literal[
    "bool",
    "int8", "int16", "int32", "int64",
    "float", "double",
    "string", "varchar",
    "array", "json",
    "binary_vector", "float_vector", "float16_vector", "bfloat16_vector", "sparse_vector",
    ]]

DTYPE_ARRAY = [
    "bool",
    "int8", "int16", "int32", "int64",
    "float", "double",
    "string", "varchar",
    "array", "json",
    "binary_vector", "float_vector", "float16_vector", "bfloat16_vector", "sparse_vector",
]


INDEX_TYPE = Union[str, Literal[
    "FLAT", "IVF_FLAT", "IVF_SQ8", "IVF_PQ", "SCANN",
    "DISKANN", "HNSW",
    "BIN_FLAT", "BIN_IVF_FLAT",
    "GPU_BRUTE_FORCE", "GPU_IVF_FLAT", "GPU_IVF_PQ", "GPU_CAGRA", "GPU_BRUTE_FORCE",
    ]]

INDEX_TYPE_ARRAY = [
    "FLAT", "IVF_FLAT", "IVF_SQ8", "IVF_PQ", "SCANN",
    "DISKANN", "HNSW",
    "BIN_FLAT", "BIN_IVF_FLAT",
    "GPU_BRUTE_FORCE", "GPU_IVF_FLAT", "GPU_IVF_PQ", "GPU_CAGRA", "GPU_BRUTE_FORCE",
    ]


METRIC_TYPE = Union[str, Literal[
    "L2", "IP", "COSINE", "HAMMING", "JACCARD", "SUBSTRUCTURE", "SUPERSTRUCTURE",
    ]]

METRIC_TYPE_ARRAY = [
    "L2", "IP", "COSINE", "HAMMING", "JACCARD", "SUBSTRUCTURE", "SUPERSTRUCTURE",
    ]

# more details: see https://milvus.io/docs/users_and_roles.md#Users-and-Roles
COLLECTION_PRIVILEGE = Union[str, Literal[
    "CreateIndex", "DropIndex", "IndexDetail",
    "Load", "GetLoadingProgress", "GetLoadState",
    "Release", "Insert", "Delete", "Upsert", "Search", "Flush", "GetFlushState",
    "Query", "GetStatistics", "Compaction", "Import", "LoadBalance",
    "CreatePartition", "ShowPartitions", "DropPartition", "HasPartition",
    ]]

GLOBAL_PRIVILEGE = Union[str, Literal[
    "All", "CreateCollection", "DropCollection", "DescribeCollection", "ShowCollections",
    "RenameCollection", "FlushAll",
    "CreateOwnership", "DropOwnership", "SelectOwnership", "ManageOwnership",
    "CreateResourceGroup", "DropResourceGroup", "DescribeResourceGroup", "ListResourceGroups",
    "TransferNode", "TransferReplica",
    "CreateDatabase", "DropDatabase", "ListDatabases",
    "CreateAlias", "DropAlias", "ShowAliases", "DescribeAlias",
    ]]

USER_PRIVILEGE = Union[str, Literal[
    "UpdateUser", "SelectUser",
    ]]


def get_consistency_level(level: str) -> ConsistencyLevel:
    level = level.lower()
    match level:
        case "strong":
            return ConsistencyLevel.Strong
        case "session":
            return ConsistencyLevel.Session
        case "bounded":
            return ConsistencyLevel.Bounded
        case "eventual":
            return ConsistencyLevel.Eventually
        case "customized":
            return ConsistencyLevel.Customized
        case (_):
            raise ValueError(f"Invalid consistency level: {level}")

def get_data_type(dtype: str) -> DataType:
    d = dtype.lower()
    match d:
        case "bool":
            return DataType.Bool
        case "int8":
            return DataType.Int8
        case "int16":
            return DataType.Int16
        case "int32":
            return DataType.Int32
        case "int64":
            return DataType.Int64
        case "float":
            return DataType.Float
        case "double":
            return DataType.Double
        case "string":
            return DataType.String
        case "varchar":
            return DataType.VarChar
        case "array":
            return DataType.Array
        case "json":
            return DataType.JSON
        case "binary_vector" | "binaryvector":
            return DataType.BinaryVector
        case "float_vector" | "floatvector":
            return DataType.FloatVector
        case "float16_vector" | "float16vector":
            return DataType.Float16Vector
        case "bfloat16_vector" | "bfloat16vector":
            return DataType.BFloat16Vector
        case "sparse_vector" | "sparsevector":
            return DataType.SparseFloatVector
        case (_):
            raise ValueError(f"Invalid data type: {dtype}")
