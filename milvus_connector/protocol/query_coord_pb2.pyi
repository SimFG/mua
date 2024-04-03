from . import common_pb2 as _common_pb2
from . import milvus_pb2 as _milvus_pb2
from . import internal_pb2 as _internal_pb2
from . import schema_pb2 as _schema_pb2
from . import msg_pb2 as _msg_pb2
from . import data_coord_pb2 as _data_coord_pb2
from . import index_coord_pb2 as _index_coord_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoadScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Full: _ClassVar[LoadScope]
    Delta: _ClassVar[LoadScope]
    Index: _ClassVar[LoadScope]

class DataScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UnKnown: _ClassVar[DataScope]
    All: _ClassVar[DataScope]
    Streaming: _ClassVar[DataScope]
    Historical: _ClassVar[DataScope]

class PartitionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NotExist: _ClassVar[PartitionState]
    NotPresent: _ClassVar[PartitionState]
    OnDisk: _ClassVar[PartitionState]
    PartialInMemory: _ClassVar[PartitionState]
    InMemory: _ClassVar[PartitionState]
    PartialInGPU: _ClassVar[PartitionState]
    InGPU: _ClassVar[PartitionState]

class TriggerCondition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UnKnowCondition: _ClassVar[TriggerCondition]
    Handoff: _ClassVar[TriggerCondition]
    LoadBalance: _ClassVar[TriggerCondition]
    GrpcRequest: _ClassVar[TriggerCondition]
    NodeDown: _ClassVar[TriggerCondition]

class LoadType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UnKnownType: _ClassVar[LoadType]
    LoadPartition: _ClassVar[LoadType]
    LoadCollection: _ClassVar[LoadType]

class LoadStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Invalid: _ClassVar[LoadStatus]
    Loading: _ClassVar[LoadStatus]
    Loaded: _ClassVar[LoadStatus]

class SyncType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Remove: _ClassVar[SyncType]
    Set: _ClassVar[SyncType]
    Amend: _ClassVar[SyncType]
    UpdateVersion: _ClassVar[SyncType]
Full: LoadScope
Delta: LoadScope
Index: LoadScope
UnKnown: DataScope
All: DataScope
Streaming: DataScope
Historical: DataScope
NotExist: PartitionState
NotPresent: PartitionState
OnDisk: PartitionState
PartialInMemory: PartitionState
InMemory: PartitionState
PartialInGPU: PartitionState
InGPU: PartitionState
UnKnowCondition: TriggerCondition
Handoff: TriggerCondition
LoadBalance: TriggerCondition
GrpcRequest: TriggerCondition
NodeDown: TriggerCondition
UnKnownType: LoadType
LoadPartition: LoadType
LoadCollection: LoadType
Invalid: LoadStatus
Loading: LoadStatus
Loaded: LoadStatus
Remove: SyncType
Set: SyncType
Amend: SyncType
UpdateVersion: SyncType

class ShowCollectionsRequest(_message.Message):
    __slots__ = ("base", "dbID", "collectionIDs")
    BASE_FIELD_NUMBER: _ClassVar[int]
    DBID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONIDS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    dbID: int
    collectionIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., dbID: _Optional[int] = ..., collectionIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class ShowCollectionsResponse(_message.Message):
    __slots__ = ("status", "collectionIDs", "inMemory_percentages", "query_service_available", "refresh_progress")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONIDS_FIELD_NUMBER: _ClassVar[int]
    INMEMORY_PERCENTAGES_FIELD_NUMBER: _ClassVar[int]
    QUERY_SERVICE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    REFRESH_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    collectionIDs: _containers.RepeatedScalarFieldContainer[int]
    inMemory_percentages: _containers.RepeatedScalarFieldContainer[int]
    query_service_available: _containers.RepeatedScalarFieldContainer[bool]
    refresh_progress: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., collectionIDs: _Optional[_Iterable[int]] = ..., inMemory_percentages: _Optional[_Iterable[int]] = ..., query_service_available: _Optional[_Iterable[bool]] = ..., refresh_progress: _Optional[_Iterable[int]] = ...) -> None: ...

class ShowPartitionsRequest(_message.Message):
    __slots__ = ("base", "dbID", "collectionID", "partitionIDs")
    BASE_FIELD_NUMBER: _ClassVar[int]
    DBID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONIDS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    dbID: int
    collectionID: int
    partitionIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., dbID: _Optional[int] = ..., collectionID: _Optional[int] = ..., partitionIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class ShowPartitionsResponse(_message.Message):
    __slots__ = ("status", "partitionIDs", "inMemory_percentages", "refresh_progress")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PARTITIONIDS_FIELD_NUMBER: _ClassVar[int]
    INMEMORY_PERCENTAGES_FIELD_NUMBER: _ClassVar[int]
    REFRESH_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    partitionIDs: _containers.RepeatedScalarFieldContainer[int]
    inMemory_percentages: _containers.RepeatedScalarFieldContainer[int]
    refresh_progress: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., partitionIDs: _Optional[_Iterable[int]] = ..., inMemory_percentages: _Optional[_Iterable[int]] = ..., refresh_progress: _Optional[_Iterable[int]] = ...) -> None: ...

class LoadCollectionRequest(_message.Message):
    __slots__ = ("base", "dbID", "collectionID", "schema", "replica_number", "field_indexID", "refresh", "resource_groups")
    class FieldIndexIDEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    DBID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    REPLICA_NUMBER_FIELD_NUMBER: _ClassVar[int]
    FIELD_INDEXID_FIELD_NUMBER: _ClassVar[int]
    REFRESH_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    dbID: int
    collectionID: int
    schema: _schema_pb2.CollectionSchema
    replica_number: int
    field_indexID: _containers.ScalarMap[int, int]
    refresh: bool
    resource_groups: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., dbID: _Optional[int] = ..., collectionID: _Optional[int] = ..., schema: _Optional[_Union[_schema_pb2.CollectionSchema, _Mapping]] = ..., replica_number: _Optional[int] = ..., field_indexID: _Optional[_Mapping[int, int]] = ..., refresh: bool = ..., resource_groups: _Optional[_Iterable[str]] = ...) -> None: ...

class ReleaseCollectionRequest(_message.Message):
    __slots__ = ("base", "dbID", "collectionID", "nodeID")
    BASE_FIELD_NUMBER: _ClassVar[int]
    DBID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    NODEID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    dbID: int
    collectionID: int
    nodeID: int
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., dbID: _Optional[int] = ..., collectionID: _Optional[int] = ..., nodeID: _Optional[int] = ...) -> None: ...

class GetStatisticsRequest(_message.Message):
    __slots__ = ("req", "dml_channels", "segmentIDs", "from_shard_leader", "scope")
    REQ_FIELD_NUMBER: _ClassVar[int]
    DML_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    SEGMENTIDS_FIELD_NUMBER: _ClassVar[int]
    FROM_SHARD_LEADER_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    req: _internal_pb2.GetStatisticsRequest
    dml_channels: _containers.RepeatedScalarFieldContainer[str]
    segmentIDs: _containers.RepeatedScalarFieldContainer[int]
    from_shard_leader: bool
    scope: DataScope
    def __init__(self, req: _Optional[_Union[_internal_pb2.GetStatisticsRequest, _Mapping]] = ..., dml_channels: _Optional[_Iterable[str]] = ..., segmentIDs: _Optional[_Iterable[int]] = ..., from_shard_leader: bool = ..., scope: _Optional[_Union[DataScope, str]] = ...) -> None: ...

class LoadPartitionsRequest(_message.Message):
    __slots__ = ("base", "dbID", "collectionID", "partitionIDs", "schema", "replica_number", "field_indexID", "refresh", "resource_groups", "index_info_list")
    class FieldIndexIDEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    DBID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONIDS_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    REPLICA_NUMBER_FIELD_NUMBER: _ClassVar[int]
    FIELD_INDEXID_FIELD_NUMBER: _ClassVar[int]
    REFRESH_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    INDEX_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    dbID: int
    collectionID: int
    partitionIDs: _containers.RepeatedScalarFieldContainer[int]
    schema: _schema_pb2.CollectionSchema
    replica_number: int
    field_indexID: _containers.ScalarMap[int, int]
    refresh: bool
    resource_groups: _containers.RepeatedScalarFieldContainer[str]
    index_info_list: _containers.RepeatedCompositeFieldContainer[_index_coord_pb2.IndexInfo]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., dbID: _Optional[int] = ..., collectionID: _Optional[int] = ..., partitionIDs: _Optional[_Iterable[int]] = ..., schema: _Optional[_Union[_schema_pb2.CollectionSchema, _Mapping]] = ..., replica_number: _Optional[int] = ..., field_indexID: _Optional[_Mapping[int, int]] = ..., refresh: bool = ..., resource_groups: _Optional[_Iterable[str]] = ..., index_info_list: _Optional[_Iterable[_Union[_index_coord_pb2.IndexInfo, _Mapping]]] = ...) -> None: ...

class ReleasePartitionsRequest(_message.Message):
    __slots__ = ("base", "dbID", "collectionID", "partitionIDs", "nodeID")
    BASE_FIELD_NUMBER: _ClassVar[int]
    DBID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONIDS_FIELD_NUMBER: _ClassVar[int]
    NODEID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    dbID: int
    collectionID: int
    partitionIDs: _containers.RepeatedScalarFieldContainer[int]
    nodeID: int
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., dbID: _Optional[int] = ..., collectionID: _Optional[int] = ..., partitionIDs: _Optional[_Iterable[int]] = ..., nodeID: _Optional[int] = ...) -> None: ...

class GetPartitionStatesRequest(_message.Message):
    __slots__ = ("base", "dbID", "collectionID", "partitionIDs")
    BASE_FIELD_NUMBER: _ClassVar[int]
    DBID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONIDS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    dbID: int
    collectionID: int
    partitionIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., dbID: _Optional[int] = ..., collectionID: _Optional[int] = ..., partitionIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class GetPartitionStatesResponse(_message.Message):
    __slots__ = ("status", "partition_descriptions")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PARTITION_DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    partition_descriptions: _containers.RepeatedCompositeFieldContainer[PartitionStates]
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., partition_descriptions: _Optional[_Iterable[_Union[PartitionStates, _Mapping]]] = ...) -> None: ...

class GetSegmentInfoRequest(_message.Message):
    __slots__ = ("base", "segmentIDs", "collectionID")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SEGMENTIDS_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    segmentIDs: _containers.RepeatedScalarFieldContainer[int]
    collectionID: int
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., segmentIDs: _Optional[_Iterable[int]] = ..., collectionID: _Optional[int] = ...) -> None: ...

class GetSegmentInfoResponse(_message.Message):
    __slots__ = ("status", "infos")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    INFOS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    infos: _containers.RepeatedCompositeFieldContainer[SegmentInfo]
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., infos: _Optional[_Iterable[_Union[SegmentInfo, _Mapping]]] = ...) -> None: ...

class GetShardLeadersRequest(_message.Message):
    __slots__ = ("base", "collectionID")
    BASE_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    collectionID: int
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., collectionID: _Optional[int] = ...) -> None: ...

class GetShardLeadersResponse(_message.Message):
    __slots__ = ("status", "shards")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SHARDS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    shards: _containers.RepeatedCompositeFieldContainer[ShardLeadersList]
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., shards: _Optional[_Iterable[_Union[ShardLeadersList, _Mapping]]] = ...) -> None: ...

class ShardLeadersList(_message.Message):
    __slots__ = ("channel_name", "node_ids", "node_addrs")
    CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
    NODE_IDS_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRS_FIELD_NUMBER: _ClassVar[int]
    channel_name: str
    node_ids: _containers.RepeatedScalarFieldContainer[int]
    node_addrs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, channel_name: _Optional[str] = ..., node_ids: _Optional[_Iterable[int]] = ..., node_addrs: _Optional[_Iterable[str]] = ...) -> None: ...

class SyncNewCreatedPartitionRequest(_message.Message):
    __slots__ = ("base", "collectionID", "partitionID")
    BASE_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    collectionID: int
    partitionID: int
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., collectionID: _Optional[int] = ..., partitionID: _Optional[int] = ...) -> None: ...

class LoadMetaInfo(_message.Message):
    __slots__ = ("load_type", "collectionID", "partitionIDs", "metric_type")
    LOAD_TYPE_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONIDS_FIELD_NUMBER: _ClassVar[int]
    METRIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    load_type: LoadType
    collectionID: int
    partitionIDs: _containers.RepeatedScalarFieldContainer[int]
    metric_type: str
    def __init__(self, load_type: _Optional[_Union[LoadType, str]] = ..., collectionID: _Optional[int] = ..., partitionIDs: _Optional[_Iterable[int]] = ..., metric_type: _Optional[str] = ...) -> None: ...

class WatchDmChannelsRequest(_message.Message):
    __slots__ = ("base", "nodeID", "collectionID", "partitionIDs", "infos", "schema", "exclude_infos", "load_meta", "replicaID", "segment_infos", "offlineNodeID", "version", "index_info_list")
    class SegmentInfosEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _data_coord_pb2.SegmentInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_data_coord_pb2.SegmentInfo, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    NODEID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONIDS_FIELD_NUMBER: _ClassVar[int]
    INFOS_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_INFOS_FIELD_NUMBER: _ClassVar[int]
    LOAD_META_FIELD_NUMBER: _ClassVar[int]
    REPLICAID_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_INFOS_FIELD_NUMBER: _ClassVar[int]
    OFFLINENODEID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    INDEX_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    nodeID: int
    collectionID: int
    partitionIDs: _containers.RepeatedScalarFieldContainer[int]
    infos: _containers.RepeatedCompositeFieldContainer[_data_coord_pb2.VchannelInfo]
    schema: _schema_pb2.CollectionSchema
    exclude_infos: _containers.RepeatedCompositeFieldContainer[_data_coord_pb2.SegmentInfo]
    load_meta: LoadMetaInfo
    replicaID: int
    segment_infos: _containers.MessageMap[int, _data_coord_pb2.SegmentInfo]
    offlineNodeID: int
    version: int
    index_info_list: _containers.RepeatedCompositeFieldContainer[_index_coord_pb2.IndexInfo]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., nodeID: _Optional[int] = ..., collectionID: _Optional[int] = ..., partitionIDs: _Optional[_Iterable[int]] = ..., infos: _Optional[_Iterable[_Union[_data_coord_pb2.VchannelInfo, _Mapping]]] = ..., schema: _Optional[_Union[_schema_pb2.CollectionSchema, _Mapping]] = ..., exclude_infos: _Optional[_Iterable[_Union[_data_coord_pb2.SegmentInfo, _Mapping]]] = ..., load_meta: _Optional[_Union[LoadMetaInfo, _Mapping]] = ..., replicaID: _Optional[int] = ..., segment_infos: _Optional[_Mapping[int, _data_coord_pb2.SegmentInfo]] = ..., offlineNodeID: _Optional[int] = ..., version: _Optional[int] = ..., index_info_list: _Optional[_Iterable[_Union[_index_coord_pb2.IndexInfo, _Mapping]]] = ...) -> None: ...

class UnsubDmChannelRequest(_message.Message):
    __slots__ = ("base", "nodeID", "collectionID", "channel_name")
    BASE_FIELD_NUMBER: _ClassVar[int]
    NODEID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    nodeID: int
    collectionID: int
    channel_name: str
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., nodeID: _Optional[int] = ..., collectionID: _Optional[int] = ..., channel_name: _Optional[str] = ...) -> None: ...

class SegmentLoadInfo(_message.Message):
    __slots__ = ("segmentID", "partitionID", "collectionID", "dbID", "flush_time", "binlog_paths", "num_of_rows", "statslogs", "deltalogs", "compactionFrom", "index_infos", "segment_size", "insert_channel", "start_position", "delta_position", "readableVersion", "level", "storageVersion")
    SEGMENTID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    DBID_FIELD_NUMBER: _ClassVar[int]
    FLUSH_TIME_FIELD_NUMBER: _ClassVar[int]
    BINLOG_PATHS_FIELD_NUMBER: _ClassVar[int]
    NUM_OF_ROWS_FIELD_NUMBER: _ClassVar[int]
    STATSLOGS_FIELD_NUMBER: _ClassVar[int]
    DELTALOGS_FIELD_NUMBER: _ClassVar[int]
    COMPACTIONFROM_FIELD_NUMBER: _ClassVar[int]
    INDEX_INFOS_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_SIZE_FIELD_NUMBER: _ClassVar[int]
    INSERT_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    START_POSITION_FIELD_NUMBER: _ClassVar[int]
    DELTA_POSITION_FIELD_NUMBER: _ClassVar[int]
    READABLEVERSION_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    STORAGEVERSION_FIELD_NUMBER: _ClassVar[int]
    segmentID: int
    partitionID: int
    collectionID: int
    dbID: int
    flush_time: int
    binlog_paths: _containers.RepeatedCompositeFieldContainer[_data_coord_pb2.FieldBinlog]
    num_of_rows: int
    statslogs: _containers.RepeatedCompositeFieldContainer[_data_coord_pb2.FieldBinlog]
    deltalogs: _containers.RepeatedCompositeFieldContainer[_data_coord_pb2.FieldBinlog]
    compactionFrom: _containers.RepeatedScalarFieldContainer[int]
    index_infos: _containers.RepeatedCompositeFieldContainer[FieldIndexInfo]
    segment_size: int
    insert_channel: str
    start_position: _msg_pb2.MsgPosition
    delta_position: _msg_pb2.MsgPosition
    readableVersion: int
    level: _data_coord_pb2.SegmentLevel
    storageVersion: int
    def __init__(self, segmentID: _Optional[int] = ..., partitionID: _Optional[int] = ..., collectionID: _Optional[int] = ..., dbID: _Optional[int] = ..., flush_time: _Optional[int] = ..., binlog_paths: _Optional[_Iterable[_Union[_data_coord_pb2.FieldBinlog, _Mapping]]] = ..., num_of_rows: _Optional[int] = ..., statslogs: _Optional[_Iterable[_Union[_data_coord_pb2.FieldBinlog, _Mapping]]] = ..., deltalogs: _Optional[_Iterable[_Union[_data_coord_pb2.FieldBinlog, _Mapping]]] = ..., compactionFrom: _Optional[_Iterable[int]] = ..., index_infos: _Optional[_Iterable[_Union[FieldIndexInfo, _Mapping]]] = ..., segment_size: _Optional[int] = ..., insert_channel: _Optional[str] = ..., start_position: _Optional[_Union[_msg_pb2.MsgPosition, _Mapping]] = ..., delta_position: _Optional[_Union[_msg_pb2.MsgPosition, _Mapping]] = ..., readableVersion: _Optional[int] = ..., level: _Optional[_Union[_data_coord_pb2.SegmentLevel, str]] = ..., storageVersion: _Optional[int] = ...) -> None: ...

class FieldIndexInfo(_message.Message):
    __slots__ = ("fieldID", "enable_index", "index_name", "indexID", "buildID", "index_params", "index_file_paths", "index_size", "index_version", "num_rows", "current_index_version", "index_store_version")
    FIELDID_FIELD_NUMBER: _ClassVar[int]
    ENABLE_INDEX_FIELD_NUMBER: _ClassVar[int]
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    INDEXID_FIELD_NUMBER: _ClassVar[int]
    BUILDID_FIELD_NUMBER: _ClassVar[int]
    INDEX_PARAMS_FIELD_NUMBER: _ClassVar[int]
    INDEX_FILE_PATHS_FIELD_NUMBER: _ClassVar[int]
    INDEX_SIZE_FIELD_NUMBER: _ClassVar[int]
    INDEX_VERSION_FIELD_NUMBER: _ClassVar[int]
    NUM_ROWS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_INDEX_VERSION_FIELD_NUMBER: _ClassVar[int]
    INDEX_STORE_VERSION_FIELD_NUMBER: _ClassVar[int]
    fieldID: int
    enable_index: bool
    index_name: str
    indexID: int
    buildID: int
    index_params: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    index_file_paths: _containers.RepeatedScalarFieldContainer[str]
    index_size: int
    index_version: int
    num_rows: int
    current_index_version: int
    index_store_version: int
    def __init__(self, fieldID: _Optional[int] = ..., enable_index: bool = ..., index_name: _Optional[str] = ..., indexID: _Optional[int] = ..., buildID: _Optional[int] = ..., index_params: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ..., index_file_paths: _Optional[_Iterable[str]] = ..., index_size: _Optional[int] = ..., index_version: _Optional[int] = ..., num_rows: _Optional[int] = ..., current_index_version: _Optional[int] = ..., index_store_version: _Optional[int] = ...) -> None: ...

class LoadSegmentsRequest(_message.Message):
    __slots__ = ("base", "dst_nodeID", "infos", "schema", "source_nodeID", "collectionID", "load_meta", "replicaID", "delta_positions", "version", "need_transfer", "load_scope", "index_info_list", "lazy_load")
    BASE_FIELD_NUMBER: _ClassVar[int]
    DST_NODEID_FIELD_NUMBER: _ClassVar[int]
    INFOS_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    SOURCE_NODEID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    LOAD_META_FIELD_NUMBER: _ClassVar[int]
    REPLICAID_FIELD_NUMBER: _ClassVar[int]
    DELTA_POSITIONS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NEED_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    LOAD_SCOPE_FIELD_NUMBER: _ClassVar[int]
    INDEX_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    LAZY_LOAD_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    dst_nodeID: int
    infos: _containers.RepeatedCompositeFieldContainer[SegmentLoadInfo]
    schema: _schema_pb2.CollectionSchema
    source_nodeID: int
    collectionID: int
    load_meta: LoadMetaInfo
    replicaID: int
    delta_positions: _containers.RepeatedCompositeFieldContainer[_msg_pb2.MsgPosition]
    version: int
    need_transfer: bool
    load_scope: LoadScope
    index_info_list: _containers.RepeatedCompositeFieldContainer[_index_coord_pb2.IndexInfo]
    lazy_load: bool
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., dst_nodeID: _Optional[int] = ..., infos: _Optional[_Iterable[_Union[SegmentLoadInfo, _Mapping]]] = ..., schema: _Optional[_Union[_schema_pb2.CollectionSchema, _Mapping]] = ..., source_nodeID: _Optional[int] = ..., collectionID: _Optional[int] = ..., load_meta: _Optional[_Union[LoadMetaInfo, _Mapping]] = ..., replicaID: _Optional[int] = ..., delta_positions: _Optional[_Iterable[_Union[_msg_pb2.MsgPosition, _Mapping]]] = ..., version: _Optional[int] = ..., need_transfer: bool = ..., load_scope: _Optional[_Union[LoadScope, str]] = ..., index_info_list: _Optional[_Iterable[_Union[_index_coord_pb2.IndexInfo, _Mapping]]] = ..., lazy_load: bool = ...) -> None: ...

class ReleaseSegmentsRequest(_message.Message):
    __slots__ = ("base", "nodeID", "dbID", "collectionID", "partitionIDs", "segmentIDs", "scope", "shard", "need_transfer")
    BASE_FIELD_NUMBER: _ClassVar[int]
    NODEID_FIELD_NUMBER: _ClassVar[int]
    DBID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONIDS_FIELD_NUMBER: _ClassVar[int]
    SEGMENTIDS_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SHARD_FIELD_NUMBER: _ClassVar[int]
    NEED_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    nodeID: int
    dbID: int
    collectionID: int
    partitionIDs: _containers.RepeatedScalarFieldContainer[int]
    segmentIDs: _containers.RepeatedScalarFieldContainer[int]
    scope: DataScope
    shard: str
    need_transfer: bool
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., nodeID: _Optional[int] = ..., dbID: _Optional[int] = ..., collectionID: _Optional[int] = ..., partitionIDs: _Optional[_Iterable[int]] = ..., segmentIDs: _Optional[_Iterable[int]] = ..., scope: _Optional[_Union[DataScope, str]] = ..., shard: _Optional[str] = ..., need_transfer: bool = ...) -> None: ...

class SearchRequest(_message.Message):
    __slots__ = ("req", "dml_channels", "segmentIDs", "from_shard_leader", "scope", "total_channel_num")
    REQ_FIELD_NUMBER: _ClassVar[int]
    DML_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    SEGMENTIDS_FIELD_NUMBER: _ClassVar[int]
    FROM_SHARD_LEADER_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CHANNEL_NUM_FIELD_NUMBER: _ClassVar[int]
    req: _internal_pb2.SearchRequest
    dml_channels: _containers.RepeatedScalarFieldContainer[str]
    segmentIDs: _containers.RepeatedScalarFieldContainer[int]
    from_shard_leader: bool
    scope: DataScope
    total_channel_num: int
    def __init__(self, req: _Optional[_Union[_internal_pb2.SearchRequest, _Mapping]] = ..., dml_channels: _Optional[_Iterable[str]] = ..., segmentIDs: _Optional[_Iterable[int]] = ..., from_shard_leader: bool = ..., scope: _Optional[_Union[DataScope, str]] = ..., total_channel_num: _Optional[int] = ...) -> None: ...

class HybridSearchRequest(_message.Message):
    __slots__ = ("req", "dml_channels", "total_channel_num")
    REQ_FIELD_NUMBER: _ClassVar[int]
    DML_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CHANNEL_NUM_FIELD_NUMBER: _ClassVar[int]
    req: _internal_pb2.HybridSearchRequest
    dml_channels: _containers.RepeatedScalarFieldContainer[str]
    total_channel_num: int
    def __init__(self, req: _Optional[_Union[_internal_pb2.HybridSearchRequest, _Mapping]] = ..., dml_channels: _Optional[_Iterable[str]] = ..., total_channel_num: _Optional[int] = ...) -> None: ...

class HybridSearchResult(_message.Message):
    __slots__ = ("base", "status", "results", "costAggregation", "channels_mvcc")
    class ChannelsMvccEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    COSTAGGREGATION_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_MVCC_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    status: _common_pb2.Status
    results: _containers.RepeatedCompositeFieldContainer[_internal_pb2.SearchResults]
    costAggregation: _internal_pb2.CostAggregation
    channels_mvcc: _containers.ScalarMap[str, int]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., results: _Optional[_Iterable[_Union[_internal_pb2.SearchResults, _Mapping]]] = ..., costAggregation: _Optional[_Union[_internal_pb2.CostAggregation, _Mapping]] = ..., channels_mvcc: _Optional[_Mapping[str, int]] = ...) -> None: ...

class QueryRequest(_message.Message):
    __slots__ = ("req", "dml_channels", "segmentIDs", "from_shard_leader", "scope")
    REQ_FIELD_NUMBER: _ClassVar[int]
    DML_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    SEGMENTIDS_FIELD_NUMBER: _ClassVar[int]
    FROM_SHARD_LEADER_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    req: _internal_pb2.RetrieveRequest
    dml_channels: _containers.RepeatedScalarFieldContainer[str]
    segmentIDs: _containers.RepeatedScalarFieldContainer[int]
    from_shard_leader: bool
    scope: DataScope
    def __init__(self, req: _Optional[_Union[_internal_pb2.RetrieveRequest, _Mapping]] = ..., dml_channels: _Optional[_Iterable[str]] = ..., segmentIDs: _Optional[_Iterable[int]] = ..., from_shard_leader: bool = ..., scope: _Optional[_Union[DataScope, str]] = ...) -> None: ...

class SyncReplicaSegmentsRequest(_message.Message):
    __slots__ = ("base", "vchannel_name", "replica_segments")
    BASE_FIELD_NUMBER: _ClassVar[int]
    VCHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
    REPLICA_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    vchannel_name: str
    replica_segments: _containers.RepeatedCompositeFieldContainer[ReplicaSegmentsInfo]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., vchannel_name: _Optional[str] = ..., replica_segments: _Optional[_Iterable[_Union[ReplicaSegmentsInfo, _Mapping]]] = ...) -> None: ...

class ReplicaSegmentsInfo(_message.Message):
    __slots__ = ("node_id", "partition_id", "segment_ids", "versions")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_IDS_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    partition_id: int
    segment_ids: _containers.RepeatedScalarFieldContainer[int]
    versions: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, node_id: _Optional[int] = ..., partition_id: _Optional[int] = ..., segment_ids: _Optional[_Iterable[int]] = ..., versions: _Optional[_Iterable[int]] = ...) -> None: ...

class GetLoadInfoRequest(_message.Message):
    __slots__ = ("base", "collection_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    collection_id: int
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., collection_id: _Optional[int] = ...) -> None: ...

class GetLoadInfoResponse(_message.Message):
    __slots__ = ("status", "schema", "load_type", "partitions")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    LOAD_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    schema: _schema_pb2.CollectionSchema
    load_type: LoadType
    partitions: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., schema: _Optional[_Union[_schema_pb2.CollectionSchema, _Mapping]] = ..., load_type: _Optional[_Union[LoadType, str]] = ..., partitions: _Optional[_Iterable[int]] = ...) -> None: ...

class HandoffSegmentsRequest(_message.Message):
    __slots__ = ("base", "segmentInfos", "released_segments")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SEGMENTINFOS_FIELD_NUMBER: _ClassVar[int]
    RELEASED_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    segmentInfos: _containers.RepeatedCompositeFieldContainer[SegmentInfo]
    released_segments: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., segmentInfos: _Optional[_Iterable[_Union[SegmentInfo, _Mapping]]] = ..., released_segments: _Optional[_Iterable[int]] = ...) -> None: ...

class LoadBalanceRequest(_message.Message):
    __slots__ = ("base", "source_nodeIDs", "balance_reason", "dst_nodeIDs", "sealed_segmentIDs", "collectionID")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_NODEIDS_FIELD_NUMBER: _ClassVar[int]
    BALANCE_REASON_FIELD_NUMBER: _ClassVar[int]
    DST_NODEIDS_FIELD_NUMBER: _ClassVar[int]
    SEALED_SEGMENTIDS_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    source_nodeIDs: _containers.RepeatedScalarFieldContainer[int]
    balance_reason: TriggerCondition
    dst_nodeIDs: _containers.RepeatedScalarFieldContainer[int]
    sealed_segmentIDs: _containers.RepeatedScalarFieldContainer[int]
    collectionID: int
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., source_nodeIDs: _Optional[_Iterable[int]] = ..., balance_reason: _Optional[_Union[TriggerCondition, str]] = ..., dst_nodeIDs: _Optional[_Iterable[int]] = ..., sealed_segmentIDs: _Optional[_Iterable[int]] = ..., collectionID: _Optional[int] = ...) -> None: ...

class DmChannelWatchInfo(_message.Message):
    __slots__ = ("collectionID", "dmChannel", "nodeID_loaded", "replicaID", "node_ids")
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    DMCHANNEL_FIELD_NUMBER: _ClassVar[int]
    NODEID_LOADED_FIELD_NUMBER: _ClassVar[int]
    REPLICAID_FIELD_NUMBER: _ClassVar[int]
    NODE_IDS_FIELD_NUMBER: _ClassVar[int]
    collectionID: int
    dmChannel: str
    nodeID_loaded: int
    replicaID: int
    node_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, collectionID: _Optional[int] = ..., dmChannel: _Optional[str] = ..., nodeID_loaded: _Optional[int] = ..., replicaID: _Optional[int] = ..., node_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class QueryChannelInfo(_message.Message):
    __slots__ = ("collectionID", "query_channel", "query_result_channel", "global_sealed_segments", "seek_position")
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    QUERY_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    QUERY_RESULT_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_SEALED_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    SEEK_POSITION_FIELD_NUMBER: _ClassVar[int]
    collectionID: int
    query_channel: str
    query_result_channel: str
    global_sealed_segments: _containers.RepeatedCompositeFieldContainer[SegmentInfo]
    seek_position: _msg_pb2.MsgPosition
    def __init__(self, collectionID: _Optional[int] = ..., query_channel: _Optional[str] = ..., query_result_channel: _Optional[str] = ..., global_sealed_segments: _Optional[_Iterable[_Union[SegmentInfo, _Mapping]]] = ..., seek_position: _Optional[_Union[_msg_pb2.MsgPosition, _Mapping]] = ...) -> None: ...

class PartitionStates(_message.Message):
    __slots__ = ("partitionID", "state", "inMemory_percentage")
    PARTITIONID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    INMEMORY_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    partitionID: int
    state: PartitionState
    inMemory_percentage: int
    def __init__(self, partitionID: _Optional[int] = ..., state: _Optional[_Union[PartitionState, str]] = ..., inMemory_percentage: _Optional[int] = ...) -> None: ...

class SegmentInfo(_message.Message):
    __slots__ = ("segmentID", "collectionID", "partitionID", "nodeID", "mem_size", "num_rows", "index_name", "indexID", "dmChannel", "compactionFrom", "createdByCompaction", "segment_state", "index_infos", "replica_ids", "node_ids", "enable_index", "is_fake")
    SEGMENTID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONID_FIELD_NUMBER: _ClassVar[int]
    NODEID_FIELD_NUMBER: _ClassVar[int]
    MEM_SIZE_FIELD_NUMBER: _ClassVar[int]
    NUM_ROWS_FIELD_NUMBER: _ClassVar[int]
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    INDEXID_FIELD_NUMBER: _ClassVar[int]
    DMCHANNEL_FIELD_NUMBER: _ClassVar[int]
    COMPACTIONFROM_FIELD_NUMBER: _ClassVar[int]
    CREATEDBYCOMPACTION_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_STATE_FIELD_NUMBER: _ClassVar[int]
    INDEX_INFOS_FIELD_NUMBER: _ClassVar[int]
    REPLICA_IDS_FIELD_NUMBER: _ClassVar[int]
    NODE_IDS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_INDEX_FIELD_NUMBER: _ClassVar[int]
    IS_FAKE_FIELD_NUMBER: _ClassVar[int]
    segmentID: int
    collectionID: int
    partitionID: int
    nodeID: int
    mem_size: int
    num_rows: int
    index_name: str
    indexID: int
    dmChannel: str
    compactionFrom: _containers.RepeatedScalarFieldContainer[int]
    createdByCompaction: bool
    segment_state: _common_pb2.SegmentState
    index_infos: _containers.RepeatedCompositeFieldContainer[FieldIndexInfo]
    replica_ids: _containers.RepeatedScalarFieldContainer[int]
    node_ids: _containers.RepeatedScalarFieldContainer[int]
    enable_index: bool
    is_fake: bool
    def __init__(self, segmentID: _Optional[int] = ..., collectionID: _Optional[int] = ..., partitionID: _Optional[int] = ..., nodeID: _Optional[int] = ..., mem_size: _Optional[int] = ..., num_rows: _Optional[int] = ..., index_name: _Optional[str] = ..., indexID: _Optional[int] = ..., dmChannel: _Optional[str] = ..., compactionFrom: _Optional[_Iterable[int]] = ..., createdByCompaction: bool = ..., segment_state: _Optional[_Union[_common_pb2.SegmentState, str]] = ..., index_infos: _Optional[_Iterable[_Union[FieldIndexInfo, _Mapping]]] = ..., replica_ids: _Optional[_Iterable[int]] = ..., node_ids: _Optional[_Iterable[int]] = ..., enable_index: bool = ..., is_fake: bool = ...) -> None: ...

class CollectionInfo(_message.Message):
    __slots__ = ("collectionID", "partitionIDs", "partition_states", "load_type", "schema", "released_partitionIDs", "inMemory_percentage", "replica_ids", "replica_number")
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONIDS_FIELD_NUMBER: _ClassVar[int]
    PARTITION_STATES_FIELD_NUMBER: _ClassVar[int]
    LOAD_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    RELEASED_PARTITIONIDS_FIELD_NUMBER: _ClassVar[int]
    INMEMORY_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    REPLICA_IDS_FIELD_NUMBER: _ClassVar[int]
    REPLICA_NUMBER_FIELD_NUMBER: _ClassVar[int]
    collectionID: int
    partitionIDs: _containers.RepeatedScalarFieldContainer[int]
    partition_states: _containers.RepeatedCompositeFieldContainer[PartitionStates]
    load_type: LoadType
    schema: _schema_pb2.CollectionSchema
    released_partitionIDs: _containers.RepeatedScalarFieldContainer[int]
    inMemory_percentage: int
    replica_ids: _containers.RepeatedScalarFieldContainer[int]
    replica_number: int
    def __init__(self, collectionID: _Optional[int] = ..., partitionIDs: _Optional[_Iterable[int]] = ..., partition_states: _Optional[_Iterable[_Union[PartitionStates, _Mapping]]] = ..., load_type: _Optional[_Union[LoadType, str]] = ..., schema: _Optional[_Union[_schema_pb2.CollectionSchema, _Mapping]] = ..., released_partitionIDs: _Optional[_Iterable[int]] = ..., inMemory_percentage: _Optional[int] = ..., replica_ids: _Optional[_Iterable[int]] = ..., replica_number: _Optional[int] = ...) -> None: ...

class UnsubscribeChannels(_message.Message):
    __slots__ = ("collectionID", "channels")
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    collectionID: int
    channels: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, collectionID: _Optional[int] = ..., channels: _Optional[_Iterable[str]] = ...) -> None: ...

class UnsubscribeChannelInfo(_message.Message):
    __slots__ = ("nodeID", "collection_channels")
    NODEID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    nodeID: int
    collection_channels: _containers.RepeatedCompositeFieldContainer[UnsubscribeChannels]
    def __init__(self, nodeID: _Optional[int] = ..., collection_channels: _Optional[_Iterable[_Union[UnsubscribeChannels, _Mapping]]] = ...) -> None: ...

class SegmentChangeInfo(_message.Message):
    __slots__ = ("online_nodeID", "online_segments", "offline_nodeID", "offline_segments")
    ONLINE_NODEID_FIELD_NUMBER: _ClassVar[int]
    ONLINE_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    OFFLINE_NODEID_FIELD_NUMBER: _ClassVar[int]
    OFFLINE_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    online_nodeID: int
    online_segments: _containers.RepeatedCompositeFieldContainer[SegmentInfo]
    offline_nodeID: int
    offline_segments: _containers.RepeatedCompositeFieldContainer[SegmentInfo]
    def __init__(self, online_nodeID: _Optional[int] = ..., online_segments: _Optional[_Iterable[_Union[SegmentInfo, _Mapping]]] = ..., offline_nodeID: _Optional[int] = ..., offline_segments: _Optional[_Iterable[_Union[SegmentInfo, _Mapping]]] = ...) -> None: ...

class SealedSegmentsChangeInfo(_message.Message):
    __slots__ = ("base", "infos")
    BASE_FIELD_NUMBER: _ClassVar[int]
    INFOS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    infos: _containers.RepeatedCompositeFieldContainer[SegmentChangeInfo]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., infos: _Optional[_Iterable[_Union[SegmentChangeInfo, _Mapping]]] = ...) -> None: ...

class GetDataDistributionRequest(_message.Message):
    __slots__ = ("base", "checkpoints")
    class CheckpointsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _msg_pb2.MsgPosition
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_msg_pb2.MsgPosition, _Mapping]] = ...) -> None: ...
    BASE_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINTS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    checkpoints: _containers.MessageMap[str, _msg_pb2.MsgPosition]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., checkpoints: _Optional[_Mapping[str, _msg_pb2.MsgPosition]] = ...) -> None: ...

class GetDataDistributionResponse(_message.Message):
    __slots__ = ("status", "nodeID", "segments", "channels", "leader_views")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NODEID_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    LEADER_VIEWS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    nodeID: int
    segments: _containers.RepeatedCompositeFieldContainer[SegmentVersionInfo]
    channels: _containers.RepeatedCompositeFieldContainer[ChannelVersionInfo]
    leader_views: _containers.RepeatedCompositeFieldContainer[LeaderView]
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., nodeID: _Optional[int] = ..., segments: _Optional[_Iterable[_Union[SegmentVersionInfo, _Mapping]]] = ..., channels: _Optional[_Iterable[_Union[ChannelVersionInfo, _Mapping]]] = ..., leader_views: _Optional[_Iterable[_Union[LeaderView, _Mapping]]] = ...) -> None: ...

class LeaderView(_message.Message):
    __slots__ = ("collection", "channel", "segment_dist", "growing_segmentIDs", "growing_segments", "TargetVersion", "num_of_growing_rows")
    class SegmentDistEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SegmentDist
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SegmentDist, _Mapping]] = ...) -> None: ...
    class GrowingSegmentsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _msg_pb2.MsgPosition
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_msg_pb2.MsgPosition, _Mapping]] = ...) -> None: ...
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_DIST_FIELD_NUMBER: _ClassVar[int]
    GROWING_SEGMENTIDS_FIELD_NUMBER: _ClassVar[int]
    GROWING_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    TARGETVERSION_FIELD_NUMBER: _ClassVar[int]
    NUM_OF_GROWING_ROWS_FIELD_NUMBER: _ClassVar[int]
    collection: int
    channel: str
    segment_dist: _containers.MessageMap[int, SegmentDist]
    growing_segmentIDs: _containers.RepeatedScalarFieldContainer[int]
    growing_segments: _containers.MessageMap[int, _msg_pb2.MsgPosition]
    TargetVersion: int
    num_of_growing_rows: int
    def __init__(self, collection: _Optional[int] = ..., channel: _Optional[str] = ..., segment_dist: _Optional[_Mapping[int, SegmentDist]] = ..., growing_segmentIDs: _Optional[_Iterable[int]] = ..., growing_segments: _Optional[_Mapping[int, _msg_pb2.MsgPosition]] = ..., TargetVersion: _Optional[int] = ..., num_of_growing_rows: _Optional[int] = ...) -> None: ...

class SegmentDist(_message.Message):
    __slots__ = ("nodeID", "version")
    NODEID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    nodeID: int
    version: int
    def __init__(self, nodeID: _Optional[int] = ..., version: _Optional[int] = ...) -> None: ...

class SegmentVersionInfo(_message.Message):
    __slots__ = ("ID", "collection", "partition", "channel", "version", "last_delta_timestamp", "index_info")
    class IndexInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: FieldIndexInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[FieldIndexInfo, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    PARTITION_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    LAST_DELTA_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    INDEX_INFO_FIELD_NUMBER: _ClassVar[int]
    ID: int
    collection: int
    partition: int
    channel: str
    version: int
    last_delta_timestamp: int
    index_info: _containers.MessageMap[int, FieldIndexInfo]
    def __init__(self, ID: _Optional[int] = ..., collection: _Optional[int] = ..., partition: _Optional[int] = ..., channel: _Optional[str] = ..., version: _Optional[int] = ..., last_delta_timestamp: _Optional[int] = ..., index_info: _Optional[_Mapping[int, FieldIndexInfo]] = ...) -> None: ...

class ChannelVersionInfo(_message.Message):
    __slots__ = ("channel", "collection", "version")
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    channel: str
    collection: int
    version: int
    def __init__(self, channel: _Optional[str] = ..., collection: _Optional[int] = ..., version: _Optional[int] = ...) -> None: ...

class CollectionLoadInfo(_message.Message):
    __slots__ = ("collectionID", "released_partitions", "replica_number", "status", "field_indexID", "load_type", "recover_times")
    class FieldIndexIDEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    RELEASED_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    REPLICA_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FIELD_INDEXID_FIELD_NUMBER: _ClassVar[int]
    LOAD_TYPE_FIELD_NUMBER: _ClassVar[int]
    RECOVER_TIMES_FIELD_NUMBER: _ClassVar[int]
    collectionID: int
    released_partitions: _containers.RepeatedScalarFieldContainer[int]
    replica_number: int
    status: LoadStatus
    field_indexID: _containers.ScalarMap[int, int]
    load_type: LoadType
    recover_times: int
    def __init__(self, collectionID: _Optional[int] = ..., released_partitions: _Optional[_Iterable[int]] = ..., replica_number: _Optional[int] = ..., status: _Optional[_Union[LoadStatus, str]] = ..., field_indexID: _Optional[_Mapping[int, int]] = ..., load_type: _Optional[_Union[LoadType, str]] = ..., recover_times: _Optional[int] = ...) -> None: ...

class PartitionLoadInfo(_message.Message):
    __slots__ = ("collectionID", "partitionID", "replica_number", "status", "field_indexID", "recover_times")
    class FieldIndexIDEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONID_FIELD_NUMBER: _ClassVar[int]
    REPLICA_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FIELD_INDEXID_FIELD_NUMBER: _ClassVar[int]
    RECOVER_TIMES_FIELD_NUMBER: _ClassVar[int]
    collectionID: int
    partitionID: int
    replica_number: int
    status: LoadStatus
    field_indexID: _containers.ScalarMap[int, int]
    recover_times: int
    def __init__(self, collectionID: _Optional[int] = ..., partitionID: _Optional[int] = ..., replica_number: _Optional[int] = ..., status: _Optional[_Union[LoadStatus, str]] = ..., field_indexID: _Optional[_Mapping[int, int]] = ..., recover_times: _Optional[int] = ...) -> None: ...

class Replica(_message.Message):
    __slots__ = ("ID", "collectionID", "nodes", "resource_group")
    ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    ID: int
    collectionID: int
    nodes: _containers.RepeatedScalarFieldContainer[int]
    resource_group: str
    def __init__(self, ID: _Optional[int] = ..., collectionID: _Optional[int] = ..., nodes: _Optional[_Iterable[int]] = ..., resource_group: _Optional[str] = ...) -> None: ...

class SyncAction(_message.Message):
    __slots__ = ("type", "partitionID", "segmentID", "nodeID", "version", "info", "growingInTarget", "sealedInTarget", "TargetVersion", "droppedInTarget", "checkpoint")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PARTITIONID_FIELD_NUMBER: _ClassVar[int]
    SEGMENTID_FIELD_NUMBER: _ClassVar[int]
    NODEID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    GROWINGINTARGET_FIELD_NUMBER: _ClassVar[int]
    SEALEDINTARGET_FIELD_NUMBER: _ClassVar[int]
    TARGETVERSION_FIELD_NUMBER: _ClassVar[int]
    DROPPEDINTARGET_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    type: SyncType
    partitionID: int
    segmentID: int
    nodeID: int
    version: int
    info: SegmentLoadInfo
    growingInTarget: _containers.RepeatedScalarFieldContainer[int]
    sealedInTarget: _containers.RepeatedScalarFieldContainer[int]
    TargetVersion: int
    droppedInTarget: _containers.RepeatedScalarFieldContainer[int]
    checkpoint: _msg_pb2.MsgPosition
    def __init__(self, type: _Optional[_Union[SyncType, str]] = ..., partitionID: _Optional[int] = ..., segmentID: _Optional[int] = ..., nodeID: _Optional[int] = ..., version: _Optional[int] = ..., info: _Optional[_Union[SegmentLoadInfo, _Mapping]] = ..., growingInTarget: _Optional[_Iterable[int]] = ..., sealedInTarget: _Optional[_Iterable[int]] = ..., TargetVersion: _Optional[int] = ..., droppedInTarget: _Optional[_Iterable[int]] = ..., checkpoint: _Optional[_Union[_msg_pb2.MsgPosition, _Mapping]] = ...) -> None: ...

class SyncDistributionRequest(_message.Message):
    __slots__ = ("base", "collectionID", "channel", "actions", "schema", "load_meta", "replicaID", "version", "index_info_list")
    BASE_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    LOAD_META_FIELD_NUMBER: _ClassVar[int]
    REPLICAID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    INDEX_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    collectionID: int
    channel: str
    actions: _containers.RepeatedCompositeFieldContainer[SyncAction]
    schema: _schema_pb2.CollectionSchema
    load_meta: LoadMetaInfo
    replicaID: int
    version: int
    index_info_list: _containers.RepeatedCompositeFieldContainer[_index_coord_pb2.IndexInfo]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., collectionID: _Optional[int] = ..., channel: _Optional[str] = ..., actions: _Optional[_Iterable[_Union[SyncAction, _Mapping]]] = ..., schema: _Optional[_Union[_schema_pb2.CollectionSchema, _Mapping]] = ..., load_meta: _Optional[_Union[LoadMetaInfo, _Mapping]] = ..., replicaID: _Optional[int] = ..., version: _Optional[int] = ..., index_info_list: _Optional[_Iterable[_Union[_index_coord_pb2.IndexInfo, _Mapping]]] = ...) -> None: ...

class ResourceGroup(_message.Message):
    __slots__ = ("name", "capacity", "nodes")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    name: str
    capacity: int
    nodes: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, name: _Optional[str] = ..., capacity: _Optional[int] = ..., nodes: _Optional[_Iterable[int]] = ...) -> None: ...

class TransferReplicaRequest(_message.Message):
    __slots__ = ("base", "source_resource_group", "target_resource_group", "collectionID", "num_replica")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_RESOURCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    TARGET_RESOURCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    NUM_REPLICA_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    source_resource_group: str
    target_resource_group: str
    collectionID: int
    num_replica: int
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., source_resource_group: _Optional[str] = ..., target_resource_group: _Optional[str] = ..., collectionID: _Optional[int] = ..., num_replica: _Optional[int] = ...) -> None: ...

class DescribeResourceGroupRequest(_message.Message):
    __slots__ = ("base", "resource_group")
    BASE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    resource_group: str
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., resource_group: _Optional[str] = ...) -> None: ...

class DescribeResourceGroupResponse(_message.Message):
    __slots__ = ("status", "resource_group")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    resource_group: ResourceGroupInfo
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., resource_group: _Optional[_Union[ResourceGroupInfo, _Mapping]] = ...) -> None: ...

class ResourceGroupInfo(_message.Message):
    __slots__ = ("name", "capacity", "num_available_node", "num_loaded_replica", "num_outgoing_node", "num_incoming_node")
    class NumLoadedReplicaEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class NumOutgoingNodeEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class NumIncomingNodeEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    NUM_AVAILABLE_NODE_FIELD_NUMBER: _ClassVar[int]
    NUM_LOADED_REPLICA_FIELD_NUMBER: _ClassVar[int]
    NUM_OUTGOING_NODE_FIELD_NUMBER: _ClassVar[int]
    NUM_INCOMING_NODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    capacity: int
    num_available_node: int
    num_loaded_replica: _containers.ScalarMap[int, int]
    num_outgoing_node: _containers.ScalarMap[int, int]
    num_incoming_node: _containers.ScalarMap[int, int]
    def __init__(self, name: _Optional[str] = ..., capacity: _Optional[int] = ..., num_available_node: _Optional[int] = ..., num_loaded_replica: _Optional[_Mapping[int, int]] = ..., num_outgoing_node: _Optional[_Mapping[int, int]] = ..., num_incoming_node: _Optional[_Mapping[int, int]] = ...) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ("base", "collection_id", "partition_id", "vchannel_name", "segment_id", "primary_keys", "timestamps", "scope")
    BASE_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    VCHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_KEYS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    collection_id: int
    partition_id: int
    vchannel_name: str
    segment_id: int
    primary_keys: _schema_pb2.IDs
    timestamps: _containers.RepeatedScalarFieldContainer[int]
    scope: DataScope
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., collection_id: _Optional[int] = ..., partition_id: _Optional[int] = ..., vchannel_name: _Optional[str] = ..., segment_id: _Optional[int] = ..., primary_keys: _Optional[_Union[_schema_pb2.IDs, _Mapping]] = ..., timestamps: _Optional[_Iterable[int]] = ..., scope: _Optional[_Union[DataScope, str]] = ...) -> None: ...

class ActivateCheckerRequest(_message.Message):
    __slots__ = ("base", "checkerID")
    BASE_FIELD_NUMBER: _ClassVar[int]
    CHECKERID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    checkerID: int
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., checkerID: _Optional[int] = ...) -> None: ...

class DeactivateCheckerRequest(_message.Message):
    __slots__ = ("base", "checkerID")
    BASE_FIELD_NUMBER: _ClassVar[int]
    CHECKERID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    checkerID: int
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., checkerID: _Optional[int] = ...) -> None: ...

class ListCheckersRequest(_message.Message):
    __slots__ = ("base", "checkerIDs")
    BASE_FIELD_NUMBER: _ClassVar[int]
    CHECKERIDS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    checkerIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., checkerIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class ListCheckersResponse(_message.Message):
    __slots__ = ("status", "checkerInfos")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CHECKERINFOS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    checkerInfos: _containers.RepeatedCompositeFieldContainer[CheckerInfo]
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., checkerInfos: _Optional[_Iterable[_Union[CheckerInfo, _Mapping]]] = ...) -> None: ...

class CheckerInfo(_message.Message):
    __slots__ = ("id", "desc", "activated", "found")
    ID_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    ACTIVATED_FIELD_NUMBER: _ClassVar[int]
    FOUND_FIELD_NUMBER: _ClassVar[int]
    id: int
    desc: str
    activated: bool
    found: bool
    def __init__(self, id: _Optional[int] = ..., desc: _Optional[str] = ..., activated: bool = ..., found: bool = ...) -> None: ...
