from . import common_pb2 as _common_pb2
from . import internal_pb2 as _internal_pb2
from . import milvus_pb2 as _milvus_pb2
from . import schema_pb2 as _schema_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IndexInfo(_message.Message):
    __slots__ = ("collectionID", "fieldID", "index_name", "indexID", "type_params", "index_params", "indexed_rows", "total_rows", "state", "index_state_fail_reason", "is_auto_index", "user_index_params", "pending_index_rows")
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    FIELDID_FIELD_NUMBER: _ClassVar[int]
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    INDEXID_FIELD_NUMBER: _ClassVar[int]
    TYPE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    INDEX_PARAMS_FIELD_NUMBER: _ClassVar[int]
    INDEXED_ROWS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ROWS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    INDEX_STATE_FAIL_REASON_FIELD_NUMBER: _ClassVar[int]
    IS_AUTO_INDEX_FIELD_NUMBER: _ClassVar[int]
    USER_INDEX_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PENDING_INDEX_ROWS_FIELD_NUMBER: _ClassVar[int]
    collectionID: int
    fieldID: int
    index_name: str
    indexID: int
    type_params: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    index_params: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    indexed_rows: int
    total_rows: int
    state: _common_pb2.IndexState
    index_state_fail_reason: str
    is_auto_index: bool
    user_index_params: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    pending_index_rows: int
    def __init__(self, collectionID: _Optional[int] = ..., fieldID: _Optional[int] = ..., index_name: _Optional[str] = ..., indexID: _Optional[int] = ..., type_params: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ..., index_params: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ..., indexed_rows: _Optional[int] = ..., total_rows: _Optional[int] = ..., state: _Optional[_Union[_common_pb2.IndexState, str]] = ..., index_state_fail_reason: _Optional[str] = ..., is_auto_index: bool = ..., user_index_params: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ..., pending_index_rows: _Optional[int] = ...) -> None: ...

class FieldIndex(_message.Message):
    __slots__ = ("index_info", "deleted", "create_time")
    INDEX_INFO_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    index_info: IndexInfo
    deleted: bool
    create_time: int
    def __init__(self, index_info: _Optional[_Union[IndexInfo, _Mapping]] = ..., deleted: bool = ..., create_time: _Optional[int] = ...) -> None: ...

class SegmentIndex(_message.Message):
    __slots__ = ("collectionID", "partitionID", "segmentID", "num_rows", "indexID", "buildID", "nodeID", "index_version", "state", "fail_reason", "index_file_keys", "deleted", "create_time", "serialize_size", "write_handoff", "current_index_version", "index_store_version")
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONID_FIELD_NUMBER: _ClassVar[int]
    SEGMENTID_FIELD_NUMBER: _ClassVar[int]
    NUM_ROWS_FIELD_NUMBER: _ClassVar[int]
    INDEXID_FIELD_NUMBER: _ClassVar[int]
    BUILDID_FIELD_NUMBER: _ClassVar[int]
    NODEID_FIELD_NUMBER: _ClassVar[int]
    INDEX_VERSION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    FAIL_REASON_FIELD_NUMBER: _ClassVar[int]
    INDEX_FILE_KEYS_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SERIALIZE_SIZE_FIELD_NUMBER: _ClassVar[int]
    WRITE_HANDOFF_FIELD_NUMBER: _ClassVar[int]
    CURRENT_INDEX_VERSION_FIELD_NUMBER: _ClassVar[int]
    INDEX_STORE_VERSION_FIELD_NUMBER: _ClassVar[int]
    collectionID: int
    partitionID: int
    segmentID: int
    num_rows: int
    indexID: int
    buildID: int
    nodeID: int
    index_version: int
    state: _common_pb2.IndexState
    fail_reason: str
    index_file_keys: _containers.RepeatedScalarFieldContainer[str]
    deleted: bool
    create_time: int
    serialize_size: int
    write_handoff: bool
    current_index_version: int
    index_store_version: int
    def __init__(self, collectionID: _Optional[int] = ..., partitionID: _Optional[int] = ..., segmentID: _Optional[int] = ..., num_rows: _Optional[int] = ..., indexID: _Optional[int] = ..., buildID: _Optional[int] = ..., nodeID: _Optional[int] = ..., index_version: _Optional[int] = ..., state: _Optional[_Union[_common_pb2.IndexState, str]] = ..., fail_reason: _Optional[str] = ..., index_file_keys: _Optional[_Iterable[str]] = ..., deleted: bool = ..., create_time: _Optional[int] = ..., serialize_size: _Optional[int] = ..., write_handoff: bool = ..., current_index_version: _Optional[int] = ..., index_store_version: _Optional[int] = ...) -> None: ...

class RegisterNodeRequest(_message.Message):
    __slots__ = ("base", "address", "nodeID")
    BASE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NODEID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    address: _common_pb2.Address
    nodeID: int
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., address: _Optional[_Union[_common_pb2.Address, _Mapping]] = ..., nodeID: _Optional[int] = ...) -> None: ...

class RegisterNodeResponse(_message.Message):
    __slots__ = ("status", "init_params")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    INIT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    init_params: _internal_pb2.InitParams
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., init_params: _Optional[_Union[_internal_pb2.InitParams, _Mapping]] = ...) -> None: ...

class GetIndexStateRequest(_message.Message):
    __slots__ = ("collectionID", "index_name")
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    collectionID: int
    index_name: str
    def __init__(self, collectionID: _Optional[int] = ..., index_name: _Optional[str] = ...) -> None: ...

class GetIndexStateResponse(_message.Message):
    __slots__ = ("status", "state", "fail_reason")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    FAIL_REASON_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    state: _common_pb2.IndexState
    fail_reason: str
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., state: _Optional[_Union[_common_pb2.IndexState, str]] = ..., fail_reason: _Optional[str] = ...) -> None: ...

class GetSegmentIndexStateRequest(_message.Message):
    __slots__ = ("collectionID", "index_name", "segmentIDs")
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    SEGMENTIDS_FIELD_NUMBER: _ClassVar[int]
    collectionID: int
    index_name: str
    segmentIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, collectionID: _Optional[int] = ..., index_name: _Optional[str] = ..., segmentIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class SegmentIndexState(_message.Message):
    __slots__ = ("segmentID", "state", "fail_reason", "index_name")
    SEGMENTID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    FAIL_REASON_FIELD_NUMBER: _ClassVar[int]
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    segmentID: int
    state: _common_pb2.IndexState
    fail_reason: str
    index_name: str
    def __init__(self, segmentID: _Optional[int] = ..., state: _Optional[_Union[_common_pb2.IndexState, str]] = ..., fail_reason: _Optional[str] = ..., index_name: _Optional[str] = ...) -> None: ...

class GetSegmentIndexStateResponse(_message.Message):
    __slots__ = ("status", "states")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATES_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    states: _containers.RepeatedCompositeFieldContainer[SegmentIndexState]
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., states: _Optional[_Iterable[_Union[SegmentIndexState, _Mapping]]] = ...) -> None: ...

class CreateIndexRequest(_message.Message):
    __slots__ = ("collectionID", "fieldID", "index_name", "type_params", "index_params", "timestamp", "is_auto_index", "user_index_params")
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    FIELDID_FIELD_NUMBER: _ClassVar[int]
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    INDEX_PARAMS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    IS_AUTO_INDEX_FIELD_NUMBER: _ClassVar[int]
    USER_INDEX_PARAMS_FIELD_NUMBER: _ClassVar[int]
    collectionID: int
    fieldID: int
    index_name: str
    type_params: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    index_params: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    timestamp: int
    is_auto_index: bool
    user_index_params: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    def __init__(self, collectionID: _Optional[int] = ..., fieldID: _Optional[int] = ..., index_name: _Optional[str] = ..., type_params: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ..., index_params: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ..., timestamp: _Optional[int] = ..., is_auto_index: bool = ..., user_index_params: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ...) -> None: ...

class AlterIndexRequest(_message.Message):
    __slots__ = ("collectionID", "index_name", "params")
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    collectionID: int
    index_name: str
    params: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    def __init__(self, collectionID: _Optional[int] = ..., index_name: _Optional[str] = ..., params: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ...) -> None: ...

class GetIndexInfoRequest(_message.Message):
    __slots__ = ("collectionID", "segmentIDs", "index_name")
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    SEGMENTIDS_FIELD_NUMBER: _ClassVar[int]
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    collectionID: int
    segmentIDs: _containers.RepeatedScalarFieldContainer[int]
    index_name: str
    def __init__(self, collectionID: _Optional[int] = ..., segmentIDs: _Optional[_Iterable[int]] = ..., index_name: _Optional[str] = ...) -> None: ...

class IndexFilePathInfo(_message.Message):
    __slots__ = ("segmentID", "fieldID", "indexID", "buildID", "index_name", "index_params", "index_file_paths", "serialized_size", "index_version", "num_rows", "current_index_version")
    SEGMENTID_FIELD_NUMBER: _ClassVar[int]
    FIELDID_FIELD_NUMBER: _ClassVar[int]
    INDEXID_FIELD_NUMBER: _ClassVar[int]
    BUILDID_FIELD_NUMBER: _ClassVar[int]
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    INDEX_PARAMS_FIELD_NUMBER: _ClassVar[int]
    INDEX_FILE_PATHS_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_SIZE_FIELD_NUMBER: _ClassVar[int]
    INDEX_VERSION_FIELD_NUMBER: _ClassVar[int]
    NUM_ROWS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_INDEX_VERSION_FIELD_NUMBER: _ClassVar[int]
    segmentID: int
    fieldID: int
    indexID: int
    buildID: int
    index_name: str
    index_params: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    index_file_paths: _containers.RepeatedScalarFieldContainer[str]
    serialized_size: int
    index_version: int
    num_rows: int
    current_index_version: int
    def __init__(self, segmentID: _Optional[int] = ..., fieldID: _Optional[int] = ..., indexID: _Optional[int] = ..., buildID: _Optional[int] = ..., index_name: _Optional[str] = ..., index_params: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ..., index_file_paths: _Optional[_Iterable[str]] = ..., serialized_size: _Optional[int] = ..., index_version: _Optional[int] = ..., num_rows: _Optional[int] = ..., current_index_version: _Optional[int] = ...) -> None: ...

class SegmentInfo(_message.Message):
    __slots__ = ("collectionID", "segmentID", "enable_index", "index_infos")
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    SEGMENTID_FIELD_NUMBER: _ClassVar[int]
    ENABLE_INDEX_FIELD_NUMBER: _ClassVar[int]
    INDEX_INFOS_FIELD_NUMBER: _ClassVar[int]
    collectionID: int
    segmentID: int
    enable_index: bool
    index_infos: _containers.RepeatedCompositeFieldContainer[IndexFilePathInfo]
    def __init__(self, collectionID: _Optional[int] = ..., segmentID: _Optional[int] = ..., enable_index: bool = ..., index_infos: _Optional[_Iterable[_Union[IndexFilePathInfo, _Mapping]]] = ...) -> None: ...

class GetIndexInfoResponse(_message.Message):
    __slots__ = ("status", "segment_info")
    class SegmentInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SegmentInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SegmentInfo, _Mapping]] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_INFO_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    segment_info: _containers.MessageMap[int, SegmentInfo]
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., segment_info: _Optional[_Mapping[int, SegmentInfo]] = ...) -> None: ...

class DropIndexRequest(_message.Message):
    __slots__ = ("collectionID", "partitionIDs", "index_name", "drop_all")
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONIDS_FIELD_NUMBER: _ClassVar[int]
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    DROP_ALL_FIELD_NUMBER: _ClassVar[int]
    collectionID: int
    partitionIDs: _containers.RepeatedScalarFieldContainer[int]
    index_name: str
    drop_all: bool
    def __init__(self, collectionID: _Optional[int] = ..., partitionIDs: _Optional[_Iterable[int]] = ..., index_name: _Optional[str] = ..., drop_all: bool = ...) -> None: ...

class DescribeIndexRequest(_message.Message):
    __slots__ = ("collectionID", "index_name", "timestamp")
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    collectionID: int
    index_name: str
    timestamp: int
    def __init__(self, collectionID: _Optional[int] = ..., index_name: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...

class DescribeIndexResponse(_message.Message):
    __slots__ = ("status", "index_infos")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    INDEX_INFOS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    index_infos: _containers.RepeatedCompositeFieldContainer[IndexInfo]
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., index_infos: _Optional[_Iterable[_Union[IndexInfo, _Mapping]]] = ...) -> None: ...

class GetIndexBuildProgressRequest(_message.Message):
    __slots__ = ("collectionID", "index_name")
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    collectionID: int
    index_name: str
    def __init__(self, collectionID: _Optional[int] = ..., index_name: _Optional[str] = ...) -> None: ...

class GetIndexBuildProgressResponse(_message.Message):
    __slots__ = ("status", "indexed_rows", "total_rows", "pending_index_rows")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    INDEXED_ROWS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ROWS_FIELD_NUMBER: _ClassVar[int]
    PENDING_INDEX_ROWS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    indexed_rows: int
    total_rows: int
    pending_index_rows: int
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., indexed_rows: _Optional[int] = ..., total_rows: _Optional[int] = ..., pending_index_rows: _Optional[int] = ...) -> None: ...

class StorageConfig(_message.Message):
    __slots__ = ("address", "access_keyID", "secret_access_key", "useSSL", "bucket_name", "root_path", "useIAM", "IAMEndpoint", "storage_type", "use_virtual_host", "region", "cloud_provider", "request_timeout_ms")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_KEYID_FIELD_NUMBER: _ClassVar[int]
    SECRET_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    USESSL_FIELD_NUMBER: _ClassVar[int]
    BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
    ROOT_PATH_FIELD_NUMBER: _ClassVar[int]
    USEIAM_FIELD_NUMBER: _ClassVar[int]
    IAMENDPOINT_FIELD_NUMBER: _ClassVar[int]
    STORAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    USE_VIRTUAL_HOST_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    address: str
    access_keyID: str
    secret_access_key: str
    useSSL: bool
    bucket_name: str
    root_path: str
    useIAM: bool
    IAMEndpoint: str
    storage_type: str
    use_virtual_host: bool
    region: str
    cloud_provider: str
    request_timeout_ms: int
    def __init__(self, address: _Optional[str] = ..., access_keyID: _Optional[str] = ..., secret_access_key: _Optional[str] = ..., useSSL: bool = ..., bucket_name: _Optional[str] = ..., root_path: _Optional[str] = ..., useIAM: bool = ..., IAMEndpoint: _Optional[str] = ..., storage_type: _Optional[str] = ..., use_virtual_host: bool = ..., region: _Optional[str] = ..., cloud_provider: _Optional[str] = ..., request_timeout_ms: _Optional[int] = ...) -> None: ...

class OptionalFieldInfo(_message.Message):
    __slots__ = ("fieldID", "field_name", "field_type", "data_paths", "data_ids")
    FIELDID_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_PATHS_FIELD_NUMBER: _ClassVar[int]
    DATA_IDS_FIELD_NUMBER: _ClassVar[int]
    fieldID: int
    field_name: str
    field_type: int
    data_paths: _containers.RepeatedScalarFieldContainer[str]
    data_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, fieldID: _Optional[int] = ..., field_name: _Optional[str] = ..., field_type: _Optional[int] = ..., data_paths: _Optional[_Iterable[str]] = ..., data_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class CreateJobRequest(_message.Message):
    __slots__ = ("clusterID", "index_file_prefix", "buildID", "data_paths", "index_version", "indexID", "index_name", "storage_config", "index_params", "type_params", "num_rows", "current_index_version", "collectionID", "partitionID", "segmentID", "fieldID", "field_name", "field_type", "store_path", "store_version", "index_store_path", "dim", "data_ids", "optional_scalar_fields")
    CLUSTERID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FILE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    BUILDID_FIELD_NUMBER: _ClassVar[int]
    DATA_PATHS_FIELD_NUMBER: _ClassVar[int]
    INDEX_VERSION_FIELD_NUMBER: _ClassVar[int]
    INDEXID_FIELD_NUMBER: _ClassVar[int]
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    INDEX_PARAMS_FIELD_NUMBER: _ClassVar[int]
    TYPE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    NUM_ROWS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_INDEX_VERSION_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONID_FIELD_NUMBER: _ClassVar[int]
    SEGMENTID_FIELD_NUMBER: _ClassVar[int]
    FIELDID_FIELD_NUMBER: _ClassVar[int]
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    STORE_PATH_FIELD_NUMBER: _ClassVar[int]
    STORE_VERSION_FIELD_NUMBER: _ClassVar[int]
    INDEX_STORE_PATH_FIELD_NUMBER: _ClassVar[int]
    DIM_FIELD_NUMBER: _ClassVar[int]
    DATA_IDS_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_SCALAR_FIELDS_FIELD_NUMBER: _ClassVar[int]
    clusterID: str
    index_file_prefix: str
    buildID: int
    data_paths: _containers.RepeatedScalarFieldContainer[str]
    index_version: int
    indexID: int
    index_name: str
    storage_config: StorageConfig
    index_params: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    type_params: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    num_rows: int
    current_index_version: int
    collectionID: int
    partitionID: int
    segmentID: int
    fieldID: int
    field_name: str
    field_type: _schema_pb2.DataType
    store_path: str
    store_version: int
    index_store_path: str
    dim: int
    data_ids: _containers.RepeatedScalarFieldContainer[int]
    optional_scalar_fields: _containers.RepeatedCompositeFieldContainer[OptionalFieldInfo]
    def __init__(self, clusterID: _Optional[str] = ..., index_file_prefix: _Optional[str] = ..., buildID: _Optional[int] = ..., data_paths: _Optional[_Iterable[str]] = ..., index_version: _Optional[int] = ..., indexID: _Optional[int] = ..., index_name: _Optional[str] = ..., storage_config: _Optional[_Union[StorageConfig, _Mapping]] = ..., index_params: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ..., type_params: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ..., num_rows: _Optional[int] = ..., current_index_version: _Optional[int] = ..., collectionID: _Optional[int] = ..., partitionID: _Optional[int] = ..., segmentID: _Optional[int] = ..., fieldID: _Optional[int] = ..., field_name: _Optional[str] = ..., field_type: _Optional[_Union[_schema_pb2.DataType, str]] = ..., store_path: _Optional[str] = ..., store_version: _Optional[int] = ..., index_store_path: _Optional[str] = ..., dim: _Optional[int] = ..., data_ids: _Optional[_Iterable[int]] = ..., optional_scalar_fields: _Optional[_Iterable[_Union[OptionalFieldInfo, _Mapping]]] = ...) -> None: ...

class QueryJobsRequest(_message.Message):
    __slots__ = ("clusterID", "buildIDs")
    CLUSTERID_FIELD_NUMBER: _ClassVar[int]
    BUILDIDS_FIELD_NUMBER: _ClassVar[int]
    clusterID: str
    buildIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, clusterID: _Optional[str] = ..., buildIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class IndexTaskInfo(_message.Message):
    __slots__ = ("buildID", "state", "index_file_keys", "serialized_size", "fail_reason", "current_index_version", "index_store_version")
    BUILDID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FILE_KEYS_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_SIZE_FIELD_NUMBER: _ClassVar[int]
    FAIL_REASON_FIELD_NUMBER: _ClassVar[int]
    CURRENT_INDEX_VERSION_FIELD_NUMBER: _ClassVar[int]
    INDEX_STORE_VERSION_FIELD_NUMBER: _ClassVar[int]
    buildID: int
    state: _common_pb2.IndexState
    index_file_keys: _containers.RepeatedScalarFieldContainer[str]
    serialized_size: int
    fail_reason: str
    current_index_version: int
    index_store_version: int
    def __init__(self, buildID: _Optional[int] = ..., state: _Optional[_Union[_common_pb2.IndexState, str]] = ..., index_file_keys: _Optional[_Iterable[str]] = ..., serialized_size: _Optional[int] = ..., fail_reason: _Optional[str] = ..., current_index_version: _Optional[int] = ..., index_store_version: _Optional[int] = ...) -> None: ...

class QueryJobsResponse(_message.Message):
    __slots__ = ("status", "clusterID", "index_infos")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CLUSTERID_FIELD_NUMBER: _ClassVar[int]
    INDEX_INFOS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    clusterID: str
    index_infos: _containers.RepeatedCompositeFieldContainer[IndexTaskInfo]
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., clusterID: _Optional[str] = ..., index_infos: _Optional[_Iterable[_Union[IndexTaskInfo, _Mapping]]] = ...) -> None: ...

class DropJobsRequest(_message.Message):
    __slots__ = ("clusterID", "buildIDs")
    CLUSTERID_FIELD_NUMBER: _ClassVar[int]
    BUILDIDS_FIELD_NUMBER: _ClassVar[int]
    clusterID: str
    buildIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, clusterID: _Optional[str] = ..., buildIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class JobInfo(_message.Message):
    __slots__ = ("num_rows", "dim", "start_time", "end_time", "index_params", "podID")
    NUM_ROWS_FIELD_NUMBER: _ClassVar[int]
    DIM_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    INDEX_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PODID_FIELD_NUMBER: _ClassVar[int]
    num_rows: int
    dim: int
    start_time: int
    end_time: int
    index_params: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    podID: int
    def __init__(self, num_rows: _Optional[int] = ..., dim: _Optional[int] = ..., start_time: _Optional[int] = ..., end_time: _Optional[int] = ..., index_params: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ..., podID: _Optional[int] = ...) -> None: ...

class GetJobStatsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetJobStatsResponse(_message.Message):
    __slots__ = ("status", "total_job_num", "in_progress_job_num", "enqueue_job_num", "task_slots", "job_infos", "enable_disk")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_JOB_NUM_FIELD_NUMBER: _ClassVar[int]
    IN_PROGRESS_JOB_NUM_FIELD_NUMBER: _ClassVar[int]
    ENQUEUE_JOB_NUM_FIELD_NUMBER: _ClassVar[int]
    TASK_SLOTS_FIELD_NUMBER: _ClassVar[int]
    JOB_INFOS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DISK_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    total_job_num: int
    in_progress_job_num: int
    enqueue_job_num: int
    task_slots: int
    job_infos: _containers.RepeatedCompositeFieldContainer[JobInfo]
    enable_disk: bool
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., total_job_num: _Optional[int] = ..., in_progress_job_num: _Optional[int] = ..., enqueue_job_num: _Optional[int] = ..., task_slots: _Optional[int] = ..., job_infos: _Optional[_Iterable[_Union[JobInfo, _Mapping]]] = ..., enable_disk: bool = ...) -> None: ...

class GetIndexStatisticsRequest(_message.Message):
    __slots__ = ("collectionID", "index_name")
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    collectionID: int
    index_name: str
    def __init__(self, collectionID: _Optional[int] = ..., index_name: _Optional[str] = ...) -> None: ...

class GetIndexStatisticsResponse(_message.Message):
    __slots__ = ("status", "index_infos")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    INDEX_INFOS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    index_infos: _containers.RepeatedCompositeFieldContainer[IndexInfo]
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., index_infos: _Optional[_Iterable[_Union[IndexInfo, _Mapping]]] = ...) -> None: ...

class ListIndexesRequest(_message.Message):
    __slots__ = ("collectionID",)
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    collectionID: int
    def __init__(self, collectionID: _Optional[int] = ...) -> None: ...

class ListIndexesResponse(_message.Message):
    __slots__ = ("status", "index_infos")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    INDEX_INFOS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    index_infos: _containers.RepeatedCompositeFieldContainer[IndexInfo]
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., index_infos: _Optional[_Iterable[_Union[IndexInfo, _Mapping]]] = ...) -> None: ...
