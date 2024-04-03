from . import common_pb2 as _common_pb2
from . import schema_pb2 as _schema_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DDLCollection: _ClassVar[RateType]
    DDLPartition: _ClassVar[RateType]
    DDLIndex: _ClassVar[RateType]
    DDLFlush: _ClassVar[RateType]
    DDLCompaction: _ClassVar[RateType]
    DMLInsert: _ClassVar[RateType]
    DMLDelete: _ClassVar[RateType]
    DMLBulkLoad: _ClassVar[RateType]
    DQLSearch: _ClassVar[RateType]
    DQLQuery: _ClassVar[RateType]
    DMLUpsert: _ClassVar[RateType]

class ImportJobState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    None: _ClassVar[ImportJobState]
    Pending: _ClassVar[ImportJobState]
    PreImporting: _ClassVar[ImportJobState]
    Importing: _ClassVar[ImportJobState]
    Failed: _ClassVar[ImportJobState]
    Completed: _ClassVar[ImportJobState]
DDLCollection: RateType
DDLPartition: RateType
DDLIndex: RateType
DDLFlush: RateType
DDLCompaction: RateType
DMLInsert: RateType
DMLDelete: RateType
DMLBulkLoad: RateType
DQLSearch: RateType
DQLQuery: RateType
DMLUpsert: RateType
None: ImportJobState
Pending: ImportJobState
PreImporting: ImportJobState
Importing: ImportJobState
Failed: ImportJobState
Completed: ImportJobState

class GetTimeTickChannelRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetStatisticsChannelRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetDdChannelRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NodeInfo(_message.Message):
    __slots__ = ("address", "role")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    address: _common_pb2.Address
    role: str
    def __init__(self, address: _Optional[_Union[_common_pb2.Address, _Mapping]] = ..., role: _Optional[str] = ...) -> None: ...

class InitParams(_message.Message):
    __slots__ = ("nodeID", "start_params")
    NODEID_FIELD_NUMBER: _ClassVar[int]
    START_PARAMS_FIELD_NUMBER: _ClassVar[int]
    nodeID: int
    start_params: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    def __init__(self, nodeID: _Optional[int] = ..., start_params: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ...) -> None: ...

class StringList(_message.Message):
    __slots__ = ("values", "status")
    VALUES_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    status: _common_pb2.Status
    def __init__(self, values: _Optional[_Iterable[str]] = ..., status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ...) -> None: ...

class GetStatisticsRequest(_message.Message):
    __slots__ = ("base", "dbID", "collectionID", "partitionIDs", "travel_timestamp", "guarantee_timestamp", "timeout_timestamp")
    BASE_FIELD_NUMBER: _ClassVar[int]
    DBID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONIDS_FIELD_NUMBER: _ClassVar[int]
    TRAVEL_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    GUARANTEE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    dbID: int
    collectionID: int
    partitionIDs: _containers.RepeatedScalarFieldContainer[int]
    travel_timestamp: int
    guarantee_timestamp: int
    timeout_timestamp: int
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., dbID: _Optional[int] = ..., collectionID: _Optional[int] = ..., partitionIDs: _Optional[_Iterable[int]] = ..., travel_timestamp: _Optional[int] = ..., guarantee_timestamp: _Optional[int] = ..., timeout_timestamp: _Optional[int] = ...) -> None: ...

class GetStatisticsResponse(_message.Message):
    __slots__ = ("base", "status", "stats")
    BASE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    status: _common_pb2.Status
    stats: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., stats: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ...) -> None: ...

class CreateAliasRequest(_message.Message):
    __slots__ = ("base", "db_name", "collection_name", "alias")
    BASE_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    db_name: str
    collection_name: str
    alias: str
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., db_name: _Optional[str] = ..., collection_name: _Optional[str] = ..., alias: _Optional[str] = ...) -> None: ...

class DropAliasRequest(_message.Message):
    __slots__ = ("base", "db_name", "alias")
    BASE_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    db_name: str
    alias: str
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., db_name: _Optional[str] = ..., alias: _Optional[str] = ...) -> None: ...

class AlterAliasRequest(_message.Message):
    __slots__ = ("base", "db_name", "collection_name", "alias")
    BASE_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    db_name: str
    collection_name: str
    alias: str
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., db_name: _Optional[str] = ..., collection_name: _Optional[str] = ..., alias: _Optional[str] = ...) -> None: ...

class CreateIndexRequest(_message.Message):
    __slots__ = ("base", "db_name", "collection_name", "field_name", "dbID", "collectionID", "fieldID", "extra_params")
    BASE_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    DBID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    FIELDID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_PARAMS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    db_name: str
    collection_name: str
    field_name: str
    dbID: int
    collectionID: int
    fieldID: int
    extra_params: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., db_name: _Optional[str] = ..., collection_name: _Optional[str] = ..., field_name: _Optional[str] = ..., dbID: _Optional[int] = ..., collectionID: _Optional[int] = ..., fieldID: _Optional[int] = ..., extra_params: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ...) -> None: ...

class SearchRequest(_message.Message):
    __slots__ = ("base", "reqID", "dbID", "collectionID", "partitionIDs", "dsl", "placeholder_group", "dsl_type", "serialized_expr_plan", "output_fields_id", "mvcc_timestamp", "guarantee_timestamp", "timeout_timestamp", "nq", "topk", "metricType", "ignoreGrowing", "username")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQID_FIELD_NUMBER: _ClassVar[int]
    DBID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONIDS_FIELD_NUMBER: _ClassVar[int]
    DSL_FIELD_NUMBER: _ClassVar[int]
    PLACEHOLDER_GROUP_FIELD_NUMBER: _ClassVar[int]
    DSL_TYPE_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_EXPR_PLAN_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELDS_ID_FIELD_NUMBER: _ClassVar[int]
    MVCC_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    GUARANTEE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    NQ_FIELD_NUMBER: _ClassVar[int]
    TOPK_FIELD_NUMBER: _ClassVar[int]
    METRICTYPE_FIELD_NUMBER: _ClassVar[int]
    IGNOREGROWING_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    reqID: int
    dbID: int
    collectionID: int
    partitionIDs: _containers.RepeatedScalarFieldContainer[int]
    dsl: str
    placeholder_group: bytes
    dsl_type: _common_pb2.DslType
    serialized_expr_plan: bytes
    output_fields_id: _containers.RepeatedScalarFieldContainer[int]
    mvcc_timestamp: int
    guarantee_timestamp: int
    timeout_timestamp: int
    nq: int
    topk: int
    metricType: str
    ignoreGrowing: bool
    username: str
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., reqID: _Optional[int] = ..., dbID: _Optional[int] = ..., collectionID: _Optional[int] = ..., partitionIDs: _Optional[_Iterable[int]] = ..., dsl: _Optional[str] = ..., placeholder_group: _Optional[bytes] = ..., dsl_type: _Optional[_Union[_common_pb2.DslType, str]] = ..., serialized_expr_plan: _Optional[bytes] = ..., output_fields_id: _Optional[_Iterable[int]] = ..., mvcc_timestamp: _Optional[int] = ..., guarantee_timestamp: _Optional[int] = ..., timeout_timestamp: _Optional[int] = ..., nq: _Optional[int] = ..., topk: _Optional[int] = ..., metricType: _Optional[str] = ..., ignoreGrowing: bool = ..., username: _Optional[str] = ...) -> None: ...

class HybridSearchRequest(_message.Message):
    __slots__ = ("base", "reqID", "dbID", "collectionID", "partitionIDs", "reqs", "mvcc_timestamp", "guarantee_timestamp", "timeout_timestamp")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQID_FIELD_NUMBER: _ClassVar[int]
    DBID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONIDS_FIELD_NUMBER: _ClassVar[int]
    REQS_FIELD_NUMBER: _ClassVar[int]
    MVCC_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    GUARANTEE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    reqID: int
    dbID: int
    collectionID: int
    partitionIDs: _containers.RepeatedScalarFieldContainer[int]
    reqs: _containers.RepeatedCompositeFieldContainer[SearchRequest]
    mvcc_timestamp: int
    guarantee_timestamp: int
    timeout_timestamp: int
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., reqID: _Optional[int] = ..., dbID: _Optional[int] = ..., collectionID: _Optional[int] = ..., partitionIDs: _Optional[_Iterable[int]] = ..., reqs: _Optional[_Iterable[_Union[SearchRequest, _Mapping]]] = ..., mvcc_timestamp: _Optional[int] = ..., guarantee_timestamp: _Optional[int] = ..., timeout_timestamp: _Optional[int] = ...) -> None: ...

class SearchResults(_message.Message):
    __slots__ = ("base", "status", "reqID", "metric_type", "num_queries", "top_k", "sealed_segmentIDs_searched", "channelIDs_searched", "global_sealed_segmentIDs", "sliced_blob", "sliced_num_count", "sliced_offset", "costAggregation", "channels_mvcc", "all_search_count")
    class ChannelsMvccEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REQID_FIELD_NUMBER: _ClassVar[int]
    METRIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    NUM_QUERIES_FIELD_NUMBER: _ClassVar[int]
    TOP_K_FIELD_NUMBER: _ClassVar[int]
    SEALED_SEGMENTIDS_SEARCHED_FIELD_NUMBER: _ClassVar[int]
    CHANNELIDS_SEARCHED_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_SEALED_SEGMENTIDS_FIELD_NUMBER: _ClassVar[int]
    SLICED_BLOB_FIELD_NUMBER: _ClassVar[int]
    SLICED_NUM_COUNT_FIELD_NUMBER: _ClassVar[int]
    SLICED_OFFSET_FIELD_NUMBER: _ClassVar[int]
    COSTAGGREGATION_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_MVCC_FIELD_NUMBER: _ClassVar[int]
    ALL_SEARCH_COUNT_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    status: _common_pb2.Status
    reqID: int
    metric_type: str
    num_queries: int
    top_k: int
    sealed_segmentIDs_searched: _containers.RepeatedScalarFieldContainer[int]
    channelIDs_searched: _containers.RepeatedScalarFieldContainer[str]
    global_sealed_segmentIDs: _containers.RepeatedScalarFieldContainer[int]
    sliced_blob: bytes
    sliced_num_count: int
    sliced_offset: int
    costAggregation: CostAggregation
    channels_mvcc: _containers.ScalarMap[str, int]
    all_search_count: int
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., reqID: _Optional[int] = ..., metric_type: _Optional[str] = ..., num_queries: _Optional[int] = ..., top_k: _Optional[int] = ..., sealed_segmentIDs_searched: _Optional[_Iterable[int]] = ..., channelIDs_searched: _Optional[_Iterable[str]] = ..., global_sealed_segmentIDs: _Optional[_Iterable[int]] = ..., sliced_blob: _Optional[bytes] = ..., sliced_num_count: _Optional[int] = ..., sliced_offset: _Optional[int] = ..., costAggregation: _Optional[_Union[CostAggregation, _Mapping]] = ..., channels_mvcc: _Optional[_Mapping[str, int]] = ..., all_search_count: _Optional[int] = ...) -> None: ...

class CostAggregation(_message.Message):
    __slots__ = ("responseTime", "serviceTime", "totalNQ")
    RESPONSETIME_FIELD_NUMBER: _ClassVar[int]
    SERVICETIME_FIELD_NUMBER: _ClassVar[int]
    TOTALNQ_FIELD_NUMBER: _ClassVar[int]
    responseTime: int
    serviceTime: int
    totalNQ: int
    def __init__(self, responseTime: _Optional[int] = ..., serviceTime: _Optional[int] = ..., totalNQ: _Optional[int] = ...) -> None: ...

class RetrieveRequest(_message.Message):
    __slots__ = ("base", "reqID", "dbID", "collectionID", "partitionIDs", "serialized_expr_plan", "output_fields_id", "mvcc_timestamp", "guarantee_timestamp", "timeout_timestamp", "limit", "ignoreGrowing", "is_count", "iteration_extension_reduce_rate", "username", "reduce_stop_for_best")
    BASE_FIELD_NUMBER: _ClassVar[int]
    REQID_FIELD_NUMBER: _ClassVar[int]
    DBID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONIDS_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_EXPR_PLAN_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELDS_ID_FIELD_NUMBER: _ClassVar[int]
    MVCC_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    GUARANTEE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    IGNOREGROWING_FIELD_NUMBER: _ClassVar[int]
    IS_COUNT_FIELD_NUMBER: _ClassVar[int]
    ITERATION_EXTENSION_REDUCE_RATE_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    REDUCE_STOP_FOR_BEST_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    reqID: int
    dbID: int
    collectionID: int
    partitionIDs: _containers.RepeatedScalarFieldContainer[int]
    serialized_expr_plan: bytes
    output_fields_id: _containers.RepeatedScalarFieldContainer[int]
    mvcc_timestamp: int
    guarantee_timestamp: int
    timeout_timestamp: int
    limit: int
    ignoreGrowing: bool
    is_count: bool
    iteration_extension_reduce_rate: int
    username: str
    reduce_stop_for_best: bool
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., reqID: _Optional[int] = ..., dbID: _Optional[int] = ..., collectionID: _Optional[int] = ..., partitionIDs: _Optional[_Iterable[int]] = ..., serialized_expr_plan: _Optional[bytes] = ..., output_fields_id: _Optional[_Iterable[int]] = ..., mvcc_timestamp: _Optional[int] = ..., guarantee_timestamp: _Optional[int] = ..., timeout_timestamp: _Optional[int] = ..., limit: _Optional[int] = ..., ignoreGrowing: bool = ..., is_count: bool = ..., iteration_extension_reduce_rate: _Optional[int] = ..., username: _Optional[str] = ..., reduce_stop_for_best: bool = ...) -> None: ...

class RetrieveResults(_message.Message):
    __slots__ = ("base", "status", "reqID", "ids", "fields_data", "sealed_segmentIDs_retrieved", "channelIDs_retrieved", "global_sealed_segmentIDs", "costAggregation", "all_retrieve_count")
    BASE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REQID_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    FIELDS_DATA_FIELD_NUMBER: _ClassVar[int]
    SEALED_SEGMENTIDS_RETRIEVED_FIELD_NUMBER: _ClassVar[int]
    CHANNELIDS_RETRIEVED_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_SEALED_SEGMENTIDS_FIELD_NUMBER: _ClassVar[int]
    COSTAGGREGATION_FIELD_NUMBER: _ClassVar[int]
    ALL_RETRIEVE_COUNT_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    status: _common_pb2.Status
    reqID: int
    ids: _schema_pb2.IDs
    fields_data: _containers.RepeatedCompositeFieldContainer[_schema_pb2.FieldData]
    sealed_segmentIDs_retrieved: _containers.RepeatedScalarFieldContainer[int]
    channelIDs_retrieved: _containers.RepeatedScalarFieldContainer[str]
    global_sealed_segmentIDs: _containers.RepeatedScalarFieldContainer[int]
    costAggregation: CostAggregation
    all_retrieve_count: int
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., reqID: _Optional[int] = ..., ids: _Optional[_Union[_schema_pb2.IDs, _Mapping]] = ..., fields_data: _Optional[_Iterable[_Union[_schema_pb2.FieldData, _Mapping]]] = ..., sealed_segmentIDs_retrieved: _Optional[_Iterable[int]] = ..., channelIDs_retrieved: _Optional[_Iterable[str]] = ..., global_sealed_segmentIDs: _Optional[_Iterable[int]] = ..., costAggregation: _Optional[_Union[CostAggregation, _Mapping]] = ..., all_retrieve_count: _Optional[int] = ...) -> None: ...

class LoadIndex(_message.Message):
    __slots__ = ("base", "segmentID", "fieldName", "fieldID", "index_paths", "index_params")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SEGMENTID_FIELD_NUMBER: _ClassVar[int]
    FIELDNAME_FIELD_NUMBER: _ClassVar[int]
    FIELDID_FIELD_NUMBER: _ClassVar[int]
    INDEX_PATHS_FIELD_NUMBER: _ClassVar[int]
    INDEX_PARAMS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    segmentID: int
    fieldName: str
    fieldID: int
    index_paths: _containers.RepeatedScalarFieldContainer[str]
    index_params: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., segmentID: _Optional[int] = ..., fieldName: _Optional[str] = ..., fieldID: _Optional[int] = ..., index_paths: _Optional[_Iterable[str]] = ..., index_params: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ...) -> None: ...

class IndexStats(_message.Message):
    __slots__ = ("index_params", "num_related_segments")
    INDEX_PARAMS_FIELD_NUMBER: _ClassVar[int]
    NUM_RELATED_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    index_params: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    num_related_segments: int
    def __init__(self, index_params: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ..., num_related_segments: _Optional[int] = ...) -> None: ...

class FieldStats(_message.Message):
    __slots__ = ("collectionID", "fieldID", "index_stats")
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    FIELDID_FIELD_NUMBER: _ClassVar[int]
    INDEX_STATS_FIELD_NUMBER: _ClassVar[int]
    collectionID: int
    fieldID: int
    index_stats: _containers.RepeatedCompositeFieldContainer[IndexStats]
    def __init__(self, collectionID: _Optional[int] = ..., fieldID: _Optional[int] = ..., index_stats: _Optional[_Iterable[_Union[IndexStats, _Mapping]]] = ...) -> None: ...

class SegmentStats(_message.Message):
    __slots__ = ("segmentID", "memory_size", "num_rows", "recently_modified")
    SEGMENTID_FIELD_NUMBER: _ClassVar[int]
    MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
    NUM_ROWS_FIELD_NUMBER: _ClassVar[int]
    RECENTLY_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    segmentID: int
    memory_size: int
    num_rows: int
    recently_modified: bool
    def __init__(self, segmentID: _Optional[int] = ..., memory_size: _Optional[int] = ..., num_rows: _Optional[int] = ..., recently_modified: bool = ...) -> None: ...

class ChannelTimeTickMsg(_message.Message):
    __slots__ = ("base", "channelNames", "timestamps", "default_timestamp")
    BASE_FIELD_NUMBER: _ClassVar[int]
    CHANNELNAMES_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    channelNames: _containers.RepeatedScalarFieldContainer[str]
    timestamps: _containers.RepeatedScalarFieldContainer[int]
    default_timestamp: int
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., channelNames: _Optional[_Iterable[str]] = ..., timestamps: _Optional[_Iterable[int]] = ..., default_timestamp: _Optional[int] = ...) -> None: ...

class CredentialInfo(_message.Message):
    __slots__ = ("username", "encrypted_password", "tenant", "is_super", "sha256_password")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    IS_SUPER_FIELD_NUMBER: _ClassVar[int]
    SHA256_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    encrypted_password: str
    tenant: str
    is_super: bool
    sha256_password: str
    def __init__(self, username: _Optional[str] = ..., encrypted_password: _Optional[str] = ..., tenant: _Optional[str] = ..., is_super: bool = ..., sha256_password: _Optional[str] = ...) -> None: ...

class ListPolicyRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ...) -> None: ...

class ListPolicyResponse(_message.Message):
    __slots__ = ("status", "policy_infos", "user_roles")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    POLICY_INFOS_FIELD_NUMBER: _ClassVar[int]
    USER_ROLES_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    policy_infos: _containers.RepeatedScalarFieldContainer[str]
    user_roles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., policy_infos: _Optional[_Iterable[str]] = ..., user_roles: _Optional[_Iterable[str]] = ...) -> None: ...

class ShowConfigurationsRequest(_message.Message):
    __slots__ = ("base", "pattern")
    BASE_FIELD_NUMBER: _ClassVar[int]
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    pattern: str
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., pattern: _Optional[str] = ...) -> None: ...

class ShowConfigurationsResponse(_message.Message):
    __slots__ = ("status", "configuations")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONFIGUATIONS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    configuations: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., configuations: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ...) -> None: ...

class Rate(_message.Message):
    __slots__ = ("rt", "r")
    RT_FIELD_NUMBER: _ClassVar[int]
    R_FIELD_NUMBER: _ClassVar[int]
    rt: RateType
    r: float
    def __init__(self, rt: _Optional[_Union[RateType, str]] = ..., r: _Optional[float] = ...) -> None: ...

class ImportFile(_message.Message):
    __slots__ = ("id", "paths")
    ID_FIELD_NUMBER: _ClassVar[int]
    PATHS_FIELD_NUMBER: _ClassVar[int]
    id: int
    paths: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[int] = ..., paths: _Optional[_Iterable[str]] = ...) -> None: ...

class ImportRequestInternal(_message.Message):
    __slots__ = ("dbID", "collectionID", "partitionIDs", "channel_names", "schema", "files", "options")
    DBID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONIDS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_NAMES_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    dbID: int
    collectionID: int
    partitionIDs: _containers.RepeatedScalarFieldContainer[int]
    channel_names: _containers.RepeatedScalarFieldContainer[str]
    schema: _schema_pb2.CollectionSchema
    files: _containers.RepeatedCompositeFieldContainer[ImportFile]
    options: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    def __init__(self, dbID: _Optional[int] = ..., collectionID: _Optional[int] = ..., partitionIDs: _Optional[_Iterable[int]] = ..., channel_names: _Optional[_Iterable[str]] = ..., schema: _Optional[_Union[_schema_pb2.CollectionSchema, _Mapping]] = ..., files: _Optional[_Iterable[_Union[ImportFile, _Mapping]]] = ..., options: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ...) -> None: ...

class ImportRequest(_message.Message):
    __slots__ = ("db_name", "collection_name", "partition_name", "files", "options")
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTITION_NAME_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    db_name: str
    collection_name: str
    partition_name: str
    files: _containers.RepeatedCompositeFieldContainer[ImportFile]
    options: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    def __init__(self, db_name: _Optional[str] = ..., collection_name: _Optional[str] = ..., partition_name: _Optional[str] = ..., files: _Optional[_Iterable[_Union[ImportFile, _Mapping]]] = ..., options: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ...) -> None: ...

class ImportResponse(_message.Message):
    __slots__ = ("status", "jobID")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    JOBID_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    jobID: str
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., jobID: _Optional[str] = ...) -> None: ...

class GetImportProgressRequest(_message.Message):
    __slots__ = ("db_name", "jobID")
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    JOBID_FIELD_NUMBER: _ClassVar[int]
    db_name: str
    jobID: str
    def __init__(self, db_name: _Optional[str] = ..., jobID: _Optional[str] = ...) -> None: ...

class GetImportProgressResponse(_message.Message):
    __slots__ = ("status", "state", "reason", "progress")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    state: ImportJobState
    reason: str
    progress: int
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., state: _Optional[_Union[ImportJobState, str]] = ..., reason: _Optional[str] = ..., progress: _Optional[int] = ...) -> None: ...

class ListImportsRequestInternal(_message.Message):
    __slots__ = ("dbID", "collectionID")
    DBID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    dbID: int
    collectionID: int
    def __init__(self, dbID: _Optional[int] = ..., collectionID: _Optional[int] = ...) -> None: ...

class ListImportsRequest(_message.Message):
    __slots__ = ("db_name", "collection_name")
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    db_name: str
    collection_name: str
    def __init__(self, db_name: _Optional[str] = ..., collection_name: _Optional[str] = ...) -> None: ...

class ListImportsResponse(_message.Message):
    __slots__ = ("status", "jobIDs", "states", "reasons", "progresses")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    JOBIDS_FIELD_NUMBER: _ClassVar[int]
    STATES_FIELD_NUMBER: _ClassVar[int]
    REASONS_FIELD_NUMBER: _ClassVar[int]
    PROGRESSES_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    jobIDs: _containers.RepeatedScalarFieldContainer[str]
    states: _containers.RepeatedScalarFieldContainer[ImportJobState]
    reasons: _containers.RepeatedScalarFieldContainer[str]
    progresses: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., jobIDs: _Optional[_Iterable[str]] = ..., states: _Optional[_Iterable[_Union[ImportJobState, str]]] = ..., reasons: _Optional[_Iterable[str]] = ..., progresses: _Optional[_Iterable[int]] = ...) -> None: ...
