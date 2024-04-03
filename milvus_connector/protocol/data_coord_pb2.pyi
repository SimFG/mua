from . import common_pb2 as _common_pb2
from . import internal_pb2 as _internal_pb2
from . import milvus_pb2 as _milvus_pb2
from . import schema_pb2 as _schema_pb2
from . import msg_pb2 as _msg_pb2
from . import index_coord_pb2 as _index_coord_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SegmentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    New: _ClassVar[SegmentType]
    Normal: _ClassVar[SegmentType]
    Flushed: _ClassVar[SegmentType]
    Compacted: _ClassVar[SegmentType]

class SegmentLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Legacy: _ClassVar[SegmentLevel]
    L0: _ClassVar[SegmentLevel]
    L1: _ClassVar[SegmentLevel]
    L2: _ClassVar[SegmentLevel]

class ChannelWatchState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Uncomplete: _ClassVar[ChannelWatchState]
    Complete: _ClassVar[ChannelWatchState]
    ToWatch: _ClassVar[ChannelWatchState]
    WatchSuccess: _ClassVar[ChannelWatchState]
    WatchFailure: _ClassVar[ChannelWatchState]
    ToRelease: _ClassVar[ChannelWatchState]
    ReleaseSuccess: _ClassVar[ChannelWatchState]
    ReleaseFailure: _ClassVar[ChannelWatchState]

class CompactionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UndefinedCompaction: _ClassVar[CompactionType]
    MergeCompaction: _ClassVar[CompactionType]
    MixCompaction: _ClassVar[CompactionType]
    SingleCompaction: _ClassVar[CompactionType]
    MinorCompaction: _ClassVar[CompactionType]
    MajorCompaction: _ClassVar[CompactionType]
    Level0DeleteCompaction: _ClassVar[CompactionType]

class ImportTaskStateV2(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    None: _ClassVar[ImportTaskStateV2]
    Pending: _ClassVar[ImportTaskStateV2]
    InProgress: _ClassVar[ImportTaskStateV2]
    Failed: _ClassVar[ImportTaskStateV2]
    Completed: _ClassVar[ImportTaskStateV2]

class GcCommand(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    _: _ClassVar[GcCommand]
    Pause: _ClassVar[GcCommand]
    Resume: _ClassVar[GcCommand]
New: SegmentType
Normal: SegmentType
Flushed: SegmentType
Compacted: SegmentType
Legacy: SegmentLevel
L0: SegmentLevel
L1: SegmentLevel
L2: SegmentLevel
Uncomplete: ChannelWatchState
Complete: ChannelWatchState
ToWatch: ChannelWatchState
WatchSuccess: ChannelWatchState
WatchFailure: ChannelWatchState
ToRelease: ChannelWatchState
ReleaseSuccess: ChannelWatchState
ReleaseFailure: ChannelWatchState
UndefinedCompaction: CompactionType
MergeCompaction: CompactionType
MixCompaction: CompactionType
SingleCompaction: CompactionType
MinorCompaction: CompactionType
MajorCompaction: CompactionType
Level0DeleteCompaction: CompactionType
None: ImportTaskStateV2
Pending: ImportTaskStateV2
InProgress: ImportTaskStateV2
Failed: ImportTaskStateV2
Completed: ImportTaskStateV2
_: GcCommand
Pause: GcCommand
Resume: GcCommand

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FlushRequest(_message.Message):
    __slots__ = ("base", "dbID", "segmentIDs", "collectionID", "isImport")
    BASE_FIELD_NUMBER: _ClassVar[int]
    DBID_FIELD_NUMBER: _ClassVar[int]
    SEGMENTIDS_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    ISIMPORT_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    dbID: int
    segmentIDs: _containers.RepeatedScalarFieldContainer[int]
    collectionID: int
    isImport: bool
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., dbID: _Optional[int] = ..., segmentIDs: _Optional[_Iterable[int]] = ..., collectionID: _Optional[int] = ..., isImport: bool = ...) -> None: ...

class FlushResponse(_message.Message):
    __slots__ = ("status", "dbID", "collectionID", "segmentIDs", "flushSegmentIDs", "timeOfSeal", "flush_ts")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DBID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    SEGMENTIDS_FIELD_NUMBER: _ClassVar[int]
    FLUSHSEGMENTIDS_FIELD_NUMBER: _ClassVar[int]
    TIMEOFSEAL_FIELD_NUMBER: _ClassVar[int]
    FLUSH_TS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    dbID: int
    collectionID: int
    segmentIDs: _containers.RepeatedScalarFieldContainer[int]
    flushSegmentIDs: _containers.RepeatedScalarFieldContainer[int]
    timeOfSeal: int
    flush_ts: int
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., dbID: _Optional[int] = ..., collectionID: _Optional[int] = ..., segmentIDs: _Optional[_Iterable[int]] = ..., flushSegmentIDs: _Optional[_Iterable[int]] = ..., timeOfSeal: _Optional[int] = ..., flush_ts: _Optional[int] = ...) -> None: ...

class FlushChannelsRequest(_message.Message):
    __slots__ = ("base", "flush_ts", "channels")
    BASE_FIELD_NUMBER: _ClassVar[int]
    FLUSH_TS_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    flush_ts: int
    channels: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., flush_ts: _Optional[int] = ..., channels: _Optional[_Iterable[str]] = ...) -> None: ...

class SegmentIDRequest(_message.Message):
    __slots__ = ("count", "channel_name", "collectionID", "partitionID", "isImport", "importTaskID", "level")
    COUNT_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONID_FIELD_NUMBER: _ClassVar[int]
    ISIMPORT_FIELD_NUMBER: _ClassVar[int]
    IMPORTTASKID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    count: int
    channel_name: str
    collectionID: int
    partitionID: int
    isImport: bool
    importTaskID: int
    level: SegmentLevel
    def __init__(self, count: _Optional[int] = ..., channel_name: _Optional[str] = ..., collectionID: _Optional[int] = ..., partitionID: _Optional[int] = ..., isImport: bool = ..., importTaskID: _Optional[int] = ..., level: _Optional[_Union[SegmentLevel, str]] = ...) -> None: ...

class AssignSegmentIDRequest(_message.Message):
    __slots__ = ("nodeID", "peer_role", "segmentIDRequests")
    NODEID_FIELD_NUMBER: _ClassVar[int]
    PEER_ROLE_FIELD_NUMBER: _ClassVar[int]
    SEGMENTIDREQUESTS_FIELD_NUMBER: _ClassVar[int]
    nodeID: int
    peer_role: str
    segmentIDRequests: _containers.RepeatedCompositeFieldContainer[SegmentIDRequest]
    def __init__(self, nodeID: _Optional[int] = ..., peer_role: _Optional[str] = ..., segmentIDRequests: _Optional[_Iterable[_Union[SegmentIDRequest, _Mapping]]] = ...) -> None: ...

class SegmentIDAssignment(_message.Message):
    __slots__ = ("segID", "channel_name", "count", "collectionID", "partitionID", "expire_time", "status")
    SEGID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONID_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    segID: int
    channel_name: str
    count: int
    collectionID: int
    partitionID: int
    expire_time: int
    status: _common_pb2.Status
    def __init__(self, segID: _Optional[int] = ..., channel_name: _Optional[str] = ..., count: _Optional[int] = ..., collectionID: _Optional[int] = ..., partitionID: _Optional[int] = ..., expire_time: _Optional[int] = ..., status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ...) -> None: ...

class AssignSegmentIDResponse(_message.Message):
    __slots__ = ("segIDAssignments", "status")
    SEGIDASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    segIDAssignments: _containers.RepeatedCompositeFieldContainer[SegmentIDAssignment]
    status: _common_pb2.Status
    def __init__(self, segIDAssignments: _Optional[_Iterable[_Union[SegmentIDAssignment, _Mapping]]] = ..., status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ...) -> None: ...

class GetSegmentStatesRequest(_message.Message):
    __slots__ = ("base", "segmentIDs")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SEGMENTIDS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    segmentIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., segmentIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class SegmentStateInfo(_message.Message):
    __slots__ = ("segmentID", "state", "start_position", "end_position", "status")
    SEGMENTID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    START_POSITION_FIELD_NUMBER: _ClassVar[int]
    END_POSITION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    segmentID: int
    state: _common_pb2.SegmentState
    start_position: _msg_pb2.MsgPosition
    end_position: _msg_pb2.MsgPosition
    status: _common_pb2.Status
    def __init__(self, segmentID: _Optional[int] = ..., state: _Optional[_Union[_common_pb2.SegmentState, str]] = ..., start_position: _Optional[_Union[_msg_pb2.MsgPosition, _Mapping]] = ..., end_position: _Optional[_Union[_msg_pb2.MsgPosition, _Mapping]] = ..., status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ...) -> None: ...

class GetSegmentStatesResponse(_message.Message):
    __slots__ = ("status", "states")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATES_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    states: _containers.RepeatedCompositeFieldContainer[SegmentStateInfo]
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., states: _Optional[_Iterable[_Union[SegmentStateInfo, _Mapping]]] = ...) -> None: ...

class GetSegmentInfoRequest(_message.Message):
    __slots__ = ("base", "segmentIDs", "includeUnHealthy")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SEGMENTIDS_FIELD_NUMBER: _ClassVar[int]
    INCLUDEUNHEALTHY_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    segmentIDs: _containers.RepeatedScalarFieldContainer[int]
    includeUnHealthy: bool
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., segmentIDs: _Optional[_Iterable[int]] = ..., includeUnHealthy: bool = ...) -> None: ...

class GetSegmentInfoResponse(_message.Message):
    __slots__ = ("status", "infos", "channel_checkpoint")
    class ChannelCheckpointEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _msg_pb2.MsgPosition
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_msg_pb2.MsgPosition, _Mapping]] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    INFOS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    infos: _containers.RepeatedCompositeFieldContainer[SegmentInfo]
    channel_checkpoint: _containers.MessageMap[str, _msg_pb2.MsgPosition]
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., infos: _Optional[_Iterable[_Union[SegmentInfo, _Mapping]]] = ..., channel_checkpoint: _Optional[_Mapping[str, _msg_pb2.MsgPosition]] = ...) -> None: ...

class GetInsertBinlogPathsRequest(_message.Message):
    __slots__ = ("base", "segmentID")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SEGMENTID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    segmentID: int
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., segmentID: _Optional[int] = ...) -> None: ...

class GetInsertBinlogPathsResponse(_message.Message):
    __slots__ = ("fieldIDs", "paths", "status")
    FIELDIDS_FIELD_NUMBER: _ClassVar[int]
    PATHS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    fieldIDs: _containers.RepeatedScalarFieldContainer[int]
    paths: _containers.RepeatedCompositeFieldContainer[_internal_pb2.StringList]
    status: _common_pb2.Status
    def __init__(self, fieldIDs: _Optional[_Iterable[int]] = ..., paths: _Optional[_Iterable[_Union[_internal_pb2.StringList, _Mapping]]] = ..., status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ...) -> None: ...

class GetCollectionStatisticsRequest(_message.Message):
    __slots__ = ("base", "dbID", "collectionID")
    BASE_FIELD_NUMBER: _ClassVar[int]
    DBID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    dbID: int
    collectionID: int
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., dbID: _Optional[int] = ..., collectionID: _Optional[int] = ...) -> None: ...

class GetCollectionStatisticsResponse(_message.Message):
    __slots__ = ("stats", "status")
    STATS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    stats: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    status: _common_pb2.Status
    def __init__(self, stats: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ..., status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ...) -> None: ...

class GetPartitionStatisticsRequest(_message.Message):
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

class GetPartitionStatisticsResponse(_message.Message):
    __slots__ = ("stats", "status")
    STATS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    stats: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    status: _common_pb2.Status
    def __init__(self, stats: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ..., status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ...) -> None: ...

class GetSegmentInfoChannelRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VchannelInfo(_message.Message):
    __slots__ = ("collectionID", "channelName", "seek_position", "unflushedSegments", "flushedSegments", "dropped_segments", "unflushedSegmentIds", "flushedSegmentIds", "dropped_segmentIds", "indexed_segmentIds", "indexed_segments", "level_zero_segment_ids")
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    CHANNELNAME_FIELD_NUMBER: _ClassVar[int]
    SEEK_POSITION_FIELD_NUMBER: _ClassVar[int]
    UNFLUSHEDSEGMENTS_FIELD_NUMBER: _ClassVar[int]
    FLUSHEDSEGMENTS_FIELD_NUMBER: _ClassVar[int]
    DROPPED_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    UNFLUSHEDSEGMENTIDS_FIELD_NUMBER: _ClassVar[int]
    FLUSHEDSEGMENTIDS_FIELD_NUMBER: _ClassVar[int]
    DROPPED_SEGMENTIDS_FIELD_NUMBER: _ClassVar[int]
    INDEXED_SEGMENTIDS_FIELD_NUMBER: _ClassVar[int]
    INDEXED_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    LEVEL_ZERO_SEGMENT_IDS_FIELD_NUMBER: _ClassVar[int]
    collectionID: int
    channelName: str
    seek_position: _msg_pb2.MsgPosition
    unflushedSegments: _containers.RepeatedCompositeFieldContainer[SegmentInfo]
    flushedSegments: _containers.RepeatedCompositeFieldContainer[SegmentInfo]
    dropped_segments: _containers.RepeatedCompositeFieldContainer[SegmentInfo]
    unflushedSegmentIds: _containers.RepeatedScalarFieldContainer[int]
    flushedSegmentIds: _containers.RepeatedScalarFieldContainer[int]
    dropped_segmentIds: _containers.RepeatedScalarFieldContainer[int]
    indexed_segmentIds: _containers.RepeatedScalarFieldContainer[int]
    indexed_segments: _containers.RepeatedCompositeFieldContainer[SegmentInfo]
    level_zero_segment_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, collectionID: _Optional[int] = ..., channelName: _Optional[str] = ..., seek_position: _Optional[_Union[_msg_pb2.MsgPosition, _Mapping]] = ..., unflushedSegments: _Optional[_Iterable[_Union[SegmentInfo, _Mapping]]] = ..., flushedSegments: _Optional[_Iterable[_Union[SegmentInfo, _Mapping]]] = ..., dropped_segments: _Optional[_Iterable[_Union[SegmentInfo, _Mapping]]] = ..., unflushedSegmentIds: _Optional[_Iterable[int]] = ..., flushedSegmentIds: _Optional[_Iterable[int]] = ..., dropped_segmentIds: _Optional[_Iterable[int]] = ..., indexed_segmentIds: _Optional[_Iterable[int]] = ..., indexed_segments: _Optional[_Iterable[_Union[SegmentInfo, _Mapping]]] = ..., level_zero_segment_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class WatchDmChannelsRequest(_message.Message):
    __slots__ = ("base", "vchannels")
    BASE_FIELD_NUMBER: _ClassVar[int]
    VCHANNELS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    vchannels: _containers.RepeatedCompositeFieldContainer[VchannelInfo]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., vchannels: _Optional[_Iterable[_Union[VchannelInfo, _Mapping]]] = ...) -> None: ...

class FlushSegmentsRequest(_message.Message):
    __slots__ = ("base", "dbID", "collectionID", "segmentIDs", "channelName")
    BASE_FIELD_NUMBER: _ClassVar[int]
    DBID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    SEGMENTIDS_FIELD_NUMBER: _ClassVar[int]
    CHANNELNAME_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    dbID: int
    collectionID: int
    segmentIDs: _containers.RepeatedScalarFieldContainer[int]
    channelName: str
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., dbID: _Optional[int] = ..., collectionID: _Optional[int] = ..., segmentIDs: _Optional[_Iterable[int]] = ..., channelName: _Optional[str] = ...) -> None: ...

class SegmentMsg(_message.Message):
    __slots__ = ("base", "segment")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    segment: SegmentInfo
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., segment: _Optional[_Union[SegmentInfo, _Mapping]] = ...) -> None: ...

class SegmentInfo(_message.Message):
    __slots__ = ("ID", "collectionID", "partitionID", "insert_channel", "num_of_rows", "state", "max_row_num", "last_expire_time", "start_position", "dml_position", "binlogs", "statslogs", "deltalogs", "createdByCompaction", "compactionFrom", "dropped_at", "is_importing", "is_fake", "compacted", "level", "storage_version")
    ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONID_FIELD_NUMBER: _ClassVar[int]
    INSERT_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    NUM_OF_ROWS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    MAX_ROW_NUM_FIELD_NUMBER: _ClassVar[int]
    LAST_EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_POSITION_FIELD_NUMBER: _ClassVar[int]
    DML_POSITION_FIELD_NUMBER: _ClassVar[int]
    BINLOGS_FIELD_NUMBER: _ClassVar[int]
    STATSLOGS_FIELD_NUMBER: _ClassVar[int]
    DELTALOGS_FIELD_NUMBER: _ClassVar[int]
    CREATEDBYCOMPACTION_FIELD_NUMBER: _ClassVar[int]
    COMPACTIONFROM_FIELD_NUMBER: _ClassVar[int]
    DROPPED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_IMPORTING_FIELD_NUMBER: _ClassVar[int]
    IS_FAKE_FIELD_NUMBER: _ClassVar[int]
    COMPACTED_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    STORAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    ID: int
    collectionID: int
    partitionID: int
    insert_channel: str
    num_of_rows: int
    state: _common_pb2.SegmentState
    max_row_num: int
    last_expire_time: int
    start_position: _msg_pb2.MsgPosition
    dml_position: _msg_pb2.MsgPosition
    binlogs: _containers.RepeatedCompositeFieldContainer[FieldBinlog]
    statslogs: _containers.RepeatedCompositeFieldContainer[FieldBinlog]
    deltalogs: _containers.RepeatedCompositeFieldContainer[FieldBinlog]
    createdByCompaction: bool
    compactionFrom: _containers.RepeatedScalarFieldContainer[int]
    dropped_at: int
    is_importing: bool
    is_fake: bool
    compacted: bool
    level: SegmentLevel
    storage_version: int
    def __init__(self, ID: _Optional[int] = ..., collectionID: _Optional[int] = ..., partitionID: _Optional[int] = ..., insert_channel: _Optional[str] = ..., num_of_rows: _Optional[int] = ..., state: _Optional[_Union[_common_pb2.SegmentState, str]] = ..., max_row_num: _Optional[int] = ..., last_expire_time: _Optional[int] = ..., start_position: _Optional[_Union[_msg_pb2.MsgPosition, _Mapping]] = ..., dml_position: _Optional[_Union[_msg_pb2.MsgPosition, _Mapping]] = ..., binlogs: _Optional[_Iterable[_Union[FieldBinlog, _Mapping]]] = ..., statslogs: _Optional[_Iterable[_Union[FieldBinlog, _Mapping]]] = ..., deltalogs: _Optional[_Iterable[_Union[FieldBinlog, _Mapping]]] = ..., createdByCompaction: bool = ..., compactionFrom: _Optional[_Iterable[int]] = ..., dropped_at: _Optional[int] = ..., is_importing: bool = ..., is_fake: bool = ..., compacted: bool = ..., level: _Optional[_Union[SegmentLevel, str]] = ..., storage_version: _Optional[int] = ...) -> None: ...

class SegmentStartPosition(_message.Message):
    __slots__ = ("start_position", "segmentID")
    START_POSITION_FIELD_NUMBER: _ClassVar[int]
    SEGMENTID_FIELD_NUMBER: _ClassVar[int]
    start_position: _msg_pb2.MsgPosition
    segmentID: int
    def __init__(self, start_position: _Optional[_Union[_msg_pb2.MsgPosition, _Mapping]] = ..., segmentID: _Optional[int] = ...) -> None: ...

class SaveBinlogPathsRequest(_message.Message):
    __slots__ = ("base", "segmentID", "collectionID", "field2BinlogPaths", "checkPoints", "start_positions", "flushed", "field2StatslogPaths", "deltalogs", "dropped", "importing", "channel", "seg_level", "partitionID", "storageVersion")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SEGMENTID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    FIELD2BINLOGPATHS_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINTS_FIELD_NUMBER: _ClassVar[int]
    START_POSITIONS_FIELD_NUMBER: _ClassVar[int]
    FLUSHED_FIELD_NUMBER: _ClassVar[int]
    FIELD2STATSLOGPATHS_FIELD_NUMBER: _ClassVar[int]
    DELTALOGS_FIELD_NUMBER: _ClassVar[int]
    DROPPED_FIELD_NUMBER: _ClassVar[int]
    IMPORTING_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    SEG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    PARTITIONID_FIELD_NUMBER: _ClassVar[int]
    STORAGEVERSION_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    segmentID: int
    collectionID: int
    field2BinlogPaths: _containers.RepeatedCompositeFieldContainer[FieldBinlog]
    checkPoints: _containers.RepeatedCompositeFieldContainer[CheckPoint]
    start_positions: _containers.RepeatedCompositeFieldContainer[SegmentStartPosition]
    flushed: bool
    field2StatslogPaths: _containers.RepeatedCompositeFieldContainer[FieldBinlog]
    deltalogs: _containers.RepeatedCompositeFieldContainer[FieldBinlog]
    dropped: bool
    importing: bool
    channel: str
    seg_level: SegmentLevel
    partitionID: int
    storageVersion: int
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., segmentID: _Optional[int] = ..., collectionID: _Optional[int] = ..., field2BinlogPaths: _Optional[_Iterable[_Union[FieldBinlog, _Mapping]]] = ..., checkPoints: _Optional[_Iterable[_Union[CheckPoint, _Mapping]]] = ..., start_positions: _Optional[_Iterable[_Union[SegmentStartPosition, _Mapping]]] = ..., flushed: bool = ..., field2StatslogPaths: _Optional[_Iterable[_Union[FieldBinlog, _Mapping]]] = ..., deltalogs: _Optional[_Iterable[_Union[FieldBinlog, _Mapping]]] = ..., dropped: bool = ..., importing: bool = ..., channel: _Optional[str] = ..., seg_level: _Optional[_Union[SegmentLevel, str]] = ..., partitionID: _Optional[int] = ..., storageVersion: _Optional[int] = ...) -> None: ...

class CheckPoint(_message.Message):
    __slots__ = ("segmentID", "position", "num_of_rows")
    SEGMENTID_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    NUM_OF_ROWS_FIELD_NUMBER: _ClassVar[int]
    segmentID: int
    position: _msg_pb2.MsgPosition
    num_of_rows: int
    def __init__(self, segmentID: _Optional[int] = ..., position: _Optional[_Union[_msg_pb2.MsgPosition, _Mapping]] = ..., num_of_rows: _Optional[int] = ...) -> None: ...

class DeltaLogInfo(_message.Message):
    __slots__ = ("record_entries", "timestamp_from", "timestamp_to", "delta_log_path", "delta_log_size")
    RECORD_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FROM_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_TO_FIELD_NUMBER: _ClassVar[int]
    DELTA_LOG_PATH_FIELD_NUMBER: _ClassVar[int]
    DELTA_LOG_SIZE_FIELD_NUMBER: _ClassVar[int]
    record_entries: int
    timestamp_from: int
    timestamp_to: int
    delta_log_path: str
    delta_log_size: int
    def __init__(self, record_entries: _Optional[int] = ..., timestamp_from: _Optional[int] = ..., timestamp_to: _Optional[int] = ..., delta_log_path: _Optional[str] = ..., delta_log_size: _Optional[int] = ...) -> None: ...

class ChannelStatus(_message.Message):
    __slots__ = ("name", "state", "collectionID")
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: ChannelWatchState
    collectionID: int
    def __init__(self, name: _Optional[str] = ..., state: _Optional[_Union[ChannelWatchState, str]] = ..., collectionID: _Optional[int] = ...) -> None: ...

class DataNodeInfo(_message.Message):
    __slots__ = ("address", "version", "channels")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    address: str
    version: int
    channels: _containers.RepeatedCompositeFieldContainer[ChannelStatus]
    def __init__(self, address: _Optional[str] = ..., version: _Optional[int] = ..., channels: _Optional[_Iterable[_Union[ChannelStatus, _Mapping]]] = ...) -> None: ...

class SegmentBinlogs(_message.Message):
    __slots__ = ("segmentID", "fieldBinlogs", "num_of_rows", "statslogs", "deltalogs", "insert_channel")
    SEGMENTID_FIELD_NUMBER: _ClassVar[int]
    FIELDBINLOGS_FIELD_NUMBER: _ClassVar[int]
    NUM_OF_ROWS_FIELD_NUMBER: _ClassVar[int]
    STATSLOGS_FIELD_NUMBER: _ClassVar[int]
    DELTALOGS_FIELD_NUMBER: _ClassVar[int]
    INSERT_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    segmentID: int
    fieldBinlogs: _containers.RepeatedCompositeFieldContainer[FieldBinlog]
    num_of_rows: int
    statslogs: _containers.RepeatedCompositeFieldContainer[FieldBinlog]
    deltalogs: _containers.RepeatedCompositeFieldContainer[FieldBinlog]
    insert_channel: str
    def __init__(self, segmentID: _Optional[int] = ..., fieldBinlogs: _Optional[_Iterable[_Union[FieldBinlog, _Mapping]]] = ..., num_of_rows: _Optional[int] = ..., statslogs: _Optional[_Iterable[_Union[FieldBinlog, _Mapping]]] = ..., deltalogs: _Optional[_Iterable[_Union[FieldBinlog, _Mapping]]] = ..., insert_channel: _Optional[str] = ...) -> None: ...

class FieldBinlog(_message.Message):
    __slots__ = ("fieldID", "binlogs")
    FIELDID_FIELD_NUMBER: _ClassVar[int]
    BINLOGS_FIELD_NUMBER: _ClassVar[int]
    fieldID: int
    binlogs: _containers.RepeatedCompositeFieldContainer[Binlog]
    def __init__(self, fieldID: _Optional[int] = ..., binlogs: _Optional[_Iterable[_Union[Binlog, _Mapping]]] = ...) -> None: ...

class Binlog(_message.Message):
    __slots__ = ("entries_num", "timestamp_from", "timestamp_to", "log_path", "log_size", "logID")
    ENTRIES_NUM_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FROM_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_TO_FIELD_NUMBER: _ClassVar[int]
    LOG_PATH_FIELD_NUMBER: _ClassVar[int]
    LOG_SIZE_FIELD_NUMBER: _ClassVar[int]
    LOGID_FIELD_NUMBER: _ClassVar[int]
    entries_num: int
    timestamp_from: int
    timestamp_to: int
    log_path: str
    log_size: int
    logID: int
    def __init__(self, entries_num: _Optional[int] = ..., timestamp_from: _Optional[int] = ..., timestamp_to: _Optional[int] = ..., log_path: _Optional[str] = ..., log_size: _Optional[int] = ..., logID: _Optional[int] = ...) -> None: ...

class GetRecoveryInfoResponse(_message.Message):
    __slots__ = ("status", "channels", "binlogs")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    BINLOGS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    channels: _containers.RepeatedCompositeFieldContainer[VchannelInfo]
    binlogs: _containers.RepeatedCompositeFieldContainer[SegmentBinlogs]
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., channels: _Optional[_Iterable[_Union[VchannelInfo, _Mapping]]] = ..., binlogs: _Optional[_Iterable[_Union[SegmentBinlogs, _Mapping]]] = ...) -> None: ...

class GetRecoveryInfoRequest(_message.Message):
    __slots__ = ("base", "collectionID", "partitionID")
    BASE_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    collectionID: int
    partitionID: int
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., collectionID: _Optional[int] = ..., partitionID: _Optional[int] = ...) -> None: ...

class GetRecoveryInfoResponseV2(_message.Message):
    __slots__ = ("status", "channels", "segments")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    channels: _containers.RepeatedCompositeFieldContainer[VchannelInfo]
    segments: _containers.RepeatedCompositeFieldContainer[SegmentInfo]
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., channels: _Optional[_Iterable[_Union[VchannelInfo, _Mapping]]] = ..., segments: _Optional[_Iterable[_Union[SegmentInfo, _Mapping]]] = ...) -> None: ...

class GetRecoveryInfoRequestV2(_message.Message):
    __slots__ = ("base", "collectionID", "partitionIDs")
    BASE_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONIDS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    collectionID: int
    partitionIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., collectionID: _Optional[int] = ..., partitionIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class GetSegmentsByStatesRequest(_message.Message):
    __slots__ = ("base", "collectionID", "partitionID", "states")
    BASE_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONID_FIELD_NUMBER: _ClassVar[int]
    STATES_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    collectionID: int
    partitionID: int
    states: _containers.RepeatedScalarFieldContainer[_common_pb2.SegmentState]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., collectionID: _Optional[int] = ..., partitionID: _Optional[int] = ..., states: _Optional[_Iterable[_Union[_common_pb2.SegmentState, str]]] = ...) -> None: ...

class GetSegmentsByStatesResponse(_message.Message):
    __slots__ = ("status", "segments")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    segments: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., segments: _Optional[_Iterable[int]] = ...) -> None: ...

class GetFlushedSegmentsRequest(_message.Message):
    __slots__ = ("base", "collectionID", "partitionID", "includeUnhealthy")
    BASE_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONID_FIELD_NUMBER: _ClassVar[int]
    INCLUDEUNHEALTHY_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    collectionID: int
    partitionID: int
    includeUnhealthy: bool
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., collectionID: _Optional[int] = ..., partitionID: _Optional[int] = ..., includeUnhealthy: bool = ...) -> None: ...

class GetFlushedSegmentsResponse(_message.Message):
    __slots__ = ("status", "segments")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    segments: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., segments: _Optional[_Iterable[int]] = ...) -> None: ...

class SegmentFlushCompletedMsg(_message.Message):
    __slots__ = ("base", "segment")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    segment: SegmentInfo
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., segment: _Optional[_Union[SegmentInfo, _Mapping]] = ...) -> None: ...

class ChannelWatchInfo(_message.Message):
    __slots__ = ("vchan", "startTs", "state", "timeoutTs", "schema", "progress", "opID")
    VCHAN_FIELD_NUMBER: _ClassVar[int]
    STARTTS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUTTS_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    OPID_FIELD_NUMBER: _ClassVar[int]
    vchan: VchannelInfo
    startTs: int
    state: ChannelWatchState
    timeoutTs: int
    schema: _schema_pb2.CollectionSchema
    progress: int
    opID: int
    def __init__(self, vchan: _Optional[_Union[VchannelInfo, _Mapping]] = ..., startTs: _Optional[int] = ..., state: _Optional[_Union[ChannelWatchState, str]] = ..., timeoutTs: _Optional[int] = ..., schema: _Optional[_Union[_schema_pb2.CollectionSchema, _Mapping]] = ..., progress: _Optional[int] = ..., opID: _Optional[int] = ...) -> None: ...

class CompactionStateRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ...) -> None: ...

class SyncSegmentsRequest(_message.Message):
    __slots__ = ("planID", "compacted_to", "num_of_rows", "compacted_from", "stats_logs", "channel_name", "partition_id", "collection_id")
    PLANID_FIELD_NUMBER: _ClassVar[int]
    COMPACTED_TO_FIELD_NUMBER: _ClassVar[int]
    NUM_OF_ROWS_FIELD_NUMBER: _ClassVar[int]
    COMPACTED_FROM_FIELD_NUMBER: _ClassVar[int]
    STATS_LOGS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    planID: int
    compacted_to: int
    num_of_rows: int
    compacted_from: _containers.RepeatedScalarFieldContainer[int]
    stats_logs: _containers.RepeatedCompositeFieldContainer[FieldBinlog]
    channel_name: str
    partition_id: int
    collection_id: int
    def __init__(self, planID: _Optional[int] = ..., compacted_to: _Optional[int] = ..., num_of_rows: _Optional[int] = ..., compacted_from: _Optional[_Iterable[int]] = ..., stats_logs: _Optional[_Iterable[_Union[FieldBinlog, _Mapping]]] = ..., channel_name: _Optional[str] = ..., partition_id: _Optional[int] = ..., collection_id: _Optional[int] = ...) -> None: ...

class CompactionSegmentBinlogs(_message.Message):
    __slots__ = ("segmentID", "fieldBinlogs", "field2StatslogPaths", "deltalogs", "insert_channel", "level", "collectionID", "partitionID")
    SEGMENTID_FIELD_NUMBER: _ClassVar[int]
    FIELDBINLOGS_FIELD_NUMBER: _ClassVar[int]
    FIELD2STATSLOGPATHS_FIELD_NUMBER: _ClassVar[int]
    DELTALOGS_FIELD_NUMBER: _ClassVar[int]
    INSERT_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONID_FIELD_NUMBER: _ClassVar[int]
    segmentID: int
    fieldBinlogs: _containers.RepeatedCompositeFieldContainer[FieldBinlog]
    field2StatslogPaths: _containers.RepeatedCompositeFieldContainer[FieldBinlog]
    deltalogs: _containers.RepeatedCompositeFieldContainer[FieldBinlog]
    insert_channel: str
    level: SegmentLevel
    collectionID: int
    partitionID: int
    def __init__(self, segmentID: _Optional[int] = ..., fieldBinlogs: _Optional[_Iterable[_Union[FieldBinlog, _Mapping]]] = ..., field2StatslogPaths: _Optional[_Iterable[_Union[FieldBinlog, _Mapping]]] = ..., deltalogs: _Optional[_Iterable[_Union[FieldBinlog, _Mapping]]] = ..., insert_channel: _Optional[str] = ..., level: _Optional[_Union[SegmentLevel, str]] = ..., collectionID: _Optional[int] = ..., partitionID: _Optional[int] = ...) -> None: ...

class CompactionPlan(_message.Message):
    __slots__ = ("planID", "segmentBinlogs", "start_time", "timeout_in_seconds", "type", "timetravel", "channel", "collection_ttl", "total_rows")
    PLANID_FIELD_NUMBER: _ClassVar[int]
    SEGMENTBINLOGS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMETRAVEL_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_TTL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ROWS_FIELD_NUMBER: _ClassVar[int]
    planID: int
    segmentBinlogs: _containers.RepeatedCompositeFieldContainer[CompactionSegmentBinlogs]
    start_time: int
    timeout_in_seconds: int
    type: CompactionType
    timetravel: int
    channel: str
    collection_ttl: int
    total_rows: int
    def __init__(self, planID: _Optional[int] = ..., segmentBinlogs: _Optional[_Iterable[_Union[CompactionSegmentBinlogs, _Mapping]]] = ..., start_time: _Optional[int] = ..., timeout_in_seconds: _Optional[int] = ..., type: _Optional[_Union[CompactionType, str]] = ..., timetravel: _Optional[int] = ..., channel: _Optional[str] = ..., collection_ttl: _Optional[int] = ..., total_rows: _Optional[int] = ...) -> None: ...

class CompactionSegment(_message.Message):
    __slots__ = ("planID", "segmentID", "num_of_rows", "insert_logs", "field2StatslogPaths", "deltalogs", "channel")
    PLANID_FIELD_NUMBER: _ClassVar[int]
    SEGMENTID_FIELD_NUMBER: _ClassVar[int]
    NUM_OF_ROWS_FIELD_NUMBER: _ClassVar[int]
    INSERT_LOGS_FIELD_NUMBER: _ClassVar[int]
    FIELD2STATSLOGPATHS_FIELD_NUMBER: _ClassVar[int]
    DELTALOGS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    planID: int
    segmentID: int
    num_of_rows: int
    insert_logs: _containers.RepeatedCompositeFieldContainer[FieldBinlog]
    field2StatslogPaths: _containers.RepeatedCompositeFieldContainer[FieldBinlog]
    deltalogs: _containers.RepeatedCompositeFieldContainer[FieldBinlog]
    channel: str
    def __init__(self, planID: _Optional[int] = ..., segmentID: _Optional[int] = ..., num_of_rows: _Optional[int] = ..., insert_logs: _Optional[_Iterable[_Union[FieldBinlog, _Mapping]]] = ..., field2StatslogPaths: _Optional[_Iterable[_Union[FieldBinlog, _Mapping]]] = ..., deltalogs: _Optional[_Iterable[_Union[FieldBinlog, _Mapping]]] = ..., channel: _Optional[str] = ...) -> None: ...

class CompactionPlanResult(_message.Message):
    __slots__ = ("planID", "state", "segments", "channel", "type")
    PLANID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    planID: int
    state: _common_pb2.CompactionState
    segments: _containers.RepeatedCompositeFieldContainer[CompactionSegment]
    channel: str
    type: CompactionType
    def __init__(self, planID: _Optional[int] = ..., state: _Optional[_Union[_common_pb2.CompactionState, str]] = ..., segments: _Optional[_Iterable[_Union[CompactionSegment, _Mapping]]] = ..., channel: _Optional[str] = ..., type: _Optional[_Union[CompactionType, str]] = ...) -> None: ...

class CompactionStateResponse(_message.Message):
    __slots__ = ("status", "results")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    results: _containers.RepeatedCompositeFieldContainer[CompactionPlanResult]
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., results: _Optional[_Iterable[_Union[CompactionPlanResult, _Mapping]]] = ...) -> None: ...

class SegmentFieldBinlogMeta(_message.Message):
    __slots__ = ("fieldID", "binlog_path")
    FIELDID_FIELD_NUMBER: _ClassVar[int]
    BINLOG_PATH_FIELD_NUMBER: _ClassVar[int]
    fieldID: int
    binlog_path: str
    def __init__(self, fieldID: _Optional[int] = ..., binlog_path: _Optional[str] = ...) -> None: ...

class WatchChannelsRequest(_message.Message):
    __slots__ = ("collectionID", "channelNames", "start_positions", "schema", "create_timestamp")
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    CHANNELNAMES_FIELD_NUMBER: _ClassVar[int]
    START_POSITIONS_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    collectionID: int
    channelNames: _containers.RepeatedScalarFieldContainer[str]
    start_positions: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyDataPair]
    schema: _schema_pb2.CollectionSchema
    create_timestamp: int
    def __init__(self, collectionID: _Optional[int] = ..., channelNames: _Optional[_Iterable[str]] = ..., start_positions: _Optional[_Iterable[_Union[_common_pb2.KeyDataPair, _Mapping]]] = ..., schema: _Optional[_Union[_schema_pb2.CollectionSchema, _Mapping]] = ..., create_timestamp: _Optional[int] = ...) -> None: ...

class WatchChannelsResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ...) -> None: ...

class SetSegmentStateRequest(_message.Message):
    __slots__ = ("base", "segment_id", "new_state")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_STATE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    segment_id: int
    new_state: _common_pb2.SegmentState
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., segment_id: _Optional[int] = ..., new_state: _Optional[_Union[_common_pb2.SegmentState, str]] = ...) -> None: ...

class SetSegmentStateResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ...) -> None: ...

class DropVirtualChannelRequest(_message.Message):
    __slots__ = ("base", "channel_name", "segments")
    BASE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    channel_name: str
    segments: _containers.RepeatedCompositeFieldContainer[DropVirtualChannelSegment]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., channel_name: _Optional[str] = ..., segments: _Optional[_Iterable[_Union[DropVirtualChannelSegment, _Mapping]]] = ...) -> None: ...

class DropVirtualChannelSegment(_message.Message):
    __slots__ = ("segmentID", "collectionID", "field2BinlogPaths", "field2StatslogPaths", "deltalogs", "startPosition", "checkPoint", "numOfRows")
    SEGMENTID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    FIELD2BINLOGPATHS_FIELD_NUMBER: _ClassVar[int]
    FIELD2STATSLOGPATHS_FIELD_NUMBER: _ClassVar[int]
    DELTALOGS_FIELD_NUMBER: _ClassVar[int]
    STARTPOSITION_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    NUMOFROWS_FIELD_NUMBER: _ClassVar[int]
    segmentID: int
    collectionID: int
    field2BinlogPaths: _containers.RepeatedCompositeFieldContainer[FieldBinlog]
    field2StatslogPaths: _containers.RepeatedCompositeFieldContainer[FieldBinlog]
    deltalogs: _containers.RepeatedCompositeFieldContainer[FieldBinlog]
    startPosition: _msg_pb2.MsgPosition
    checkPoint: _msg_pb2.MsgPosition
    numOfRows: int
    def __init__(self, segmentID: _Optional[int] = ..., collectionID: _Optional[int] = ..., field2BinlogPaths: _Optional[_Iterable[_Union[FieldBinlog, _Mapping]]] = ..., field2StatslogPaths: _Optional[_Iterable[_Union[FieldBinlog, _Mapping]]] = ..., deltalogs: _Optional[_Iterable[_Union[FieldBinlog, _Mapping]]] = ..., startPosition: _Optional[_Union[_msg_pb2.MsgPosition, _Mapping]] = ..., checkPoint: _Optional[_Union[_msg_pb2.MsgPosition, _Mapping]] = ..., numOfRows: _Optional[int] = ...) -> None: ...

class DropVirtualChannelResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ...) -> None: ...

class ImportTask(_message.Message):
    __slots__ = ("status", "collection_id", "partition_id", "channel_names", "row_based", "task_id", "files", "infos", "database_name")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_NAMES_FIELD_NUMBER: _ClassVar[int]
    ROW_BASED_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    INFOS_FIELD_NUMBER: _ClassVar[int]
    DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    collection_id: int
    partition_id: int
    channel_names: _containers.RepeatedScalarFieldContainer[str]
    row_based: bool
    task_id: int
    files: _containers.RepeatedScalarFieldContainer[str]
    infos: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    database_name: str
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., collection_id: _Optional[int] = ..., partition_id: _Optional[int] = ..., channel_names: _Optional[_Iterable[str]] = ..., row_based: bool = ..., task_id: _Optional[int] = ..., files: _Optional[_Iterable[str]] = ..., infos: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ..., database_name: _Optional[str] = ...) -> None: ...

class ImportTaskState(_message.Message):
    __slots__ = ("stateCode", "segments", "row_ids", "row_count", "error_message")
    STATECODE_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    ROW_IDS_FIELD_NUMBER: _ClassVar[int]
    ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    stateCode: _common_pb2.ImportState
    segments: _containers.RepeatedScalarFieldContainer[int]
    row_ids: _containers.RepeatedScalarFieldContainer[int]
    row_count: int
    error_message: str
    def __init__(self, stateCode: _Optional[_Union[_common_pb2.ImportState, str]] = ..., segments: _Optional[_Iterable[int]] = ..., row_ids: _Optional[_Iterable[int]] = ..., row_count: _Optional[int] = ..., error_message: _Optional[str] = ...) -> None: ...

class ImportTaskInfo(_message.Message):
    __slots__ = ("id", "request_id", "datanode_id", "collection_id", "partition_id", "channel_names", "bucket", "row_based", "files", "create_ts", "state", "collection_name", "partition_name", "infos", "start_ts", "database_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    DATANODE_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_NAMES_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    ROW_BASED_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    PARTITION_NAME_FIELD_NUMBER: _ClassVar[int]
    INFOS_FIELD_NUMBER: _ClassVar[int]
    START_TS_FIELD_NUMBER: _ClassVar[int]
    DATABASE_NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    request_id: int
    datanode_id: int
    collection_id: int
    partition_id: int
    channel_names: _containers.RepeatedScalarFieldContainer[str]
    bucket: str
    row_based: bool
    files: _containers.RepeatedScalarFieldContainer[str]
    create_ts: int
    state: ImportTaskState
    collection_name: str
    partition_name: str
    infos: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    start_ts: int
    database_name: str
    def __init__(self, id: _Optional[int] = ..., request_id: _Optional[int] = ..., datanode_id: _Optional[int] = ..., collection_id: _Optional[int] = ..., partition_id: _Optional[int] = ..., channel_names: _Optional[_Iterable[str]] = ..., bucket: _Optional[str] = ..., row_based: bool = ..., files: _Optional[_Iterable[str]] = ..., create_ts: _Optional[int] = ..., state: _Optional[_Union[ImportTaskState, _Mapping]] = ..., collection_name: _Optional[str] = ..., partition_name: _Optional[str] = ..., infos: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ..., start_ts: _Optional[int] = ..., database_name: _Optional[str] = ...) -> None: ...

class ImportTaskResponse(_message.Message):
    __slots__ = ("status", "datanode_id")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATANODE_ID_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    datanode_id: int
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., datanode_id: _Optional[int] = ...) -> None: ...

class ImportTaskRequest(_message.Message):
    __slots__ = ("base", "import_task", "working_nodes")
    BASE_FIELD_NUMBER: _ClassVar[int]
    IMPORT_TASK_FIELD_NUMBER: _ClassVar[int]
    WORKING_NODES_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    import_task: ImportTask
    working_nodes: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., import_task: _Optional[_Union[ImportTask, _Mapping]] = ..., working_nodes: _Optional[_Iterable[int]] = ...) -> None: ...

class UpdateSegmentStatisticsRequest(_message.Message):
    __slots__ = ("base", "stats")
    BASE_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    stats: _containers.RepeatedCompositeFieldContainer[_common_pb2.SegmentStats]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., stats: _Optional[_Iterable[_Union[_common_pb2.SegmentStats, _Mapping]]] = ...) -> None: ...

class UpdateChannelCheckpointRequest(_message.Message):
    __slots__ = ("base", "vChannel", "position", "channel_checkpoints")
    BASE_FIELD_NUMBER: _ClassVar[int]
    VCHANNEL_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_CHECKPOINTS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    vChannel: str
    position: _msg_pb2.MsgPosition
    channel_checkpoints: _containers.RepeatedCompositeFieldContainer[_msg_pb2.MsgPosition]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., vChannel: _Optional[str] = ..., position: _Optional[_Union[_msg_pb2.MsgPosition, _Mapping]] = ..., channel_checkpoints: _Optional[_Iterable[_Union[_msg_pb2.MsgPosition, _Mapping]]] = ...) -> None: ...

class ResendSegmentStatsRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ...) -> None: ...

class ResendSegmentStatsResponse(_message.Message):
    __slots__ = ("status", "seg_resent")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SEG_RESENT_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    seg_resent: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., seg_resent: _Optional[_Iterable[int]] = ...) -> None: ...

class AddImportSegmentRequest(_message.Message):
    __slots__ = ("base", "segment_id", "channel_name", "collection_id", "partition_id", "row_num", "stats_log")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    ROW_NUM_FIELD_NUMBER: _ClassVar[int]
    STATS_LOG_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    segment_id: int
    channel_name: str
    collection_id: int
    partition_id: int
    row_num: int
    stats_log: _containers.RepeatedCompositeFieldContainer[FieldBinlog]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., segment_id: _Optional[int] = ..., channel_name: _Optional[str] = ..., collection_id: _Optional[int] = ..., partition_id: _Optional[int] = ..., row_num: _Optional[int] = ..., stats_log: _Optional[_Iterable[_Union[FieldBinlog, _Mapping]]] = ...) -> None: ...

class AddImportSegmentResponse(_message.Message):
    __slots__ = ("status", "channel_pos")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_POS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    channel_pos: bytes
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., channel_pos: _Optional[bytes] = ...) -> None: ...

class SaveImportSegmentRequest(_message.Message):
    __slots__ = ("base", "segment_id", "channel_name", "collection_id", "partition_id", "row_num", "save_binlog_path_req", "dml_position_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    ROW_NUM_FIELD_NUMBER: _ClassVar[int]
    SAVE_BINLOG_PATH_REQ_FIELD_NUMBER: _ClassVar[int]
    DML_POSITION_ID_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    segment_id: int
    channel_name: str
    collection_id: int
    partition_id: int
    row_num: int
    save_binlog_path_req: SaveBinlogPathsRequest
    dml_position_id: bytes
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., segment_id: _Optional[int] = ..., channel_name: _Optional[str] = ..., collection_id: _Optional[int] = ..., partition_id: _Optional[int] = ..., row_num: _Optional[int] = ..., save_binlog_path_req: _Optional[_Union[SaveBinlogPathsRequest, _Mapping]] = ..., dml_position_id: _Optional[bytes] = ...) -> None: ...

class UnsetIsImportingStateRequest(_message.Message):
    __slots__ = ("base", "segment_ids")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_IDS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    segment_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., segment_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class MarkSegmentsDroppedRequest(_message.Message):
    __slots__ = ("base", "segment_ids")
    BASE_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_IDS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    segment_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., segment_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class SegmentReferenceLock(_message.Message):
    __slots__ = ("taskID", "nodeID", "segmentIDs")
    TASKID_FIELD_NUMBER: _ClassVar[int]
    NODEID_FIELD_NUMBER: _ClassVar[int]
    SEGMENTIDS_FIELD_NUMBER: _ClassVar[int]
    taskID: int
    nodeID: int
    segmentIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, taskID: _Optional[int] = ..., nodeID: _Optional[int] = ..., segmentIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class AlterCollectionRequest(_message.Message):
    __slots__ = ("collectionID", "schema", "partitionIDs", "start_positions", "properties")
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    PARTITIONIDS_FIELD_NUMBER: _ClassVar[int]
    START_POSITIONS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    collectionID: int
    schema: _schema_pb2.CollectionSchema
    partitionIDs: _containers.RepeatedScalarFieldContainer[int]
    start_positions: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyDataPair]
    properties: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    def __init__(self, collectionID: _Optional[int] = ..., schema: _Optional[_Union[_schema_pb2.CollectionSchema, _Mapping]] = ..., partitionIDs: _Optional[_Iterable[int]] = ..., start_positions: _Optional[_Iterable[_Union[_common_pb2.KeyDataPair, _Mapping]]] = ..., properties: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ...) -> None: ...

class GcConfirmRequest(_message.Message):
    __slots__ = ("collection_id", "partition_id")
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    PARTITION_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: int
    partition_id: int
    def __init__(self, collection_id: _Optional[int] = ..., partition_id: _Optional[int] = ...) -> None: ...

class GcConfirmResponse(_message.Message):
    __slots__ = ("status", "gc_finished")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    GC_FINISHED_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    gc_finished: bool
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., gc_finished: bool = ...) -> None: ...

class ReportDataNodeTtMsgsRequest(_message.Message):
    __slots__ = ("base", "msgs")
    BASE_FIELD_NUMBER: _ClassVar[int]
    MSGS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    msgs: _containers.RepeatedCompositeFieldContainer[_msg_pb2.DataNodeTtMsg]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., msgs: _Optional[_Iterable[_Union[_msg_pb2.DataNodeTtMsg, _Mapping]]] = ...) -> None: ...

class GetFlushStateRequest(_message.Message):
    __slots__ = ("segmentIDs", "flush_ts", "db_name", "collection_name", "collectionID")
    SEGMENTIDS_FIELD_NUMBER: _ClassVar[int]
    FLUSH_TS_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    segmentIDs: _containers.RepeatedScalarFieldContainer[int]
    flush_ts: int
    db_name: str
    collection_name: str
    collectionID: int
    def __init__(self, segmentIDs: _Optional[_Iterable[int]] = ..., flush_ts: _Optional[int] = ..., db_name: _Optional[str] = ..., collection_name: _Optional[str] = ..., collectionID: _Optional[int] = ...) -> None: ...

class ChannelOperationsRequest(_message.Message):
    __slots__ = ("infos",)
    INFOS_FIELD_NUMBER: _ClassVar[int]
    infos: _containers.RepeatedCompositeFieldContainer[ChannelWatchInfo]
    def __init__(self, infos: _Optional[_Iterable[_Union[ChannelWatchInfo, _Mapping]]] = ...) -> None: ...

class ChannelOperationProgressResponse(_message.Message):
    __slots__ = ("status", "opID", "state", "progress")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    OPID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    opID: int
    state: ChannelWatchState
    progress: int
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., opID: _Optional[int] = ..., state: _Optional[_Union[ChannelWatchState, str]] = ..., progress: _Optional[int] = ...) -> None: ...

class PreImportRequest(_message.Message):
    __slots__ = ("clusterID", "jobID", "taskID", "collectionID", "partitionIDs", "vchannels", "schema", "import_files", "options")
    CLUSTERID_FIELD_NUMBER: _ClassVar[int]
    JOBID_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONIDS_FIELD_NUMBER: _ClassVar[int]
    VCHANNELS_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    IMPORT_FILES_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    clusterID: str
    jobID: int
    taskID: int
    collectionID: int
    partitionIDs: _containers.RepeatedScalarFieldContainer[int]
    vchannels: _containers.RepeatedScalarFieldContainer[str]
    schema: _schema_pb2.CollectionSchema
    import_files: _containers.RepeatedCompositeFieldContainer[_internal_pb2.ImportFile]
    options: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    def __init__(self, clusterID: _Optional[str] = ..., jobID: _Optional[int] = ..., taskID: _Optional[int] = ..., collectionID: _Optional[int] = ..., partitionIDs: _Optional[_Iterable[int]] = ..., vchannels: _Optional[_Iterable[str]] = ..., schema: _Optional[_Union[_schema_pb2.CollectionSchema, _Mapping]] = ..., import_files: _Optional[_Iterable[_Union[_internal_pb2.ImportFile, _Mapping]]] = ..., options: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ...) -> None: ...

class autoIDRange(_message.Message):
    __slots__ = ("begin", "end")
    BEGIN_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    begin: int
    end: int
    def __init__(self, begin: _Optional[int] = ..., end: _Optional[int] = ...) -> None: ...

class ImportRequestSegment(_message.Message):
    __slots__ = ("segmentID", "partitionID", "vchannel")
    SEGMENTID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONID_FIELD_NUMBER: _ClassVar[int]
    VCHANNEL_FIELD_NUMBER: _ClassVar[int]
    segmentID: int
    partitionID: int
    vchannel: str
    def __init__(self, segmentID: _Optional[int] = ..., partitionID: _Optional[int] = ..., vchannel: _Optional[str] = ...) -> None: ...

class ImportRequest(_message.Message):
    __slots__ = ("clusterID", "jobID", "taskID", "collectionID", "partitionIDs", "vchannels", "schema", "files", "options", "ts", "autoID_range", "request_segments")
    CLUSTERID_FIELD_NUMBER: _ClassVar[int]
    JOBID_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONIDS_FIELD_NUMBER: _ClassVar[int]
    VCHANNELS_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    TS_FIELD_NUMBER: _ClassVar[int]
    AUTOID_RANGE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    clusterID: str
    jobID: int
    taskID: int
    collectionID: int
    partitionIDs: _containers.RepeatedScalarFieldContainer[int]
    vchannels: _containers.RepeatedScalarFieldContainer[str]
    schema: _schema_pb2.CollectionSchema
    files: _containers.RepeatedCompositeFieldContainer[_internal_pb2.ImportFile]
    options: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    ts: int
    autoID_range: autoIDRange
    request_segments: _containers.RepeatedCompositeFieldContainer[ImportRequestSegment]
    def __init__(self, clusterID: _Optional[str] = ..., jobID: _Optional[int] = ..., taskID: _Optional[int] = ..., collectionID: _Optional[int] = ..., partitionIDs: _Optional[_Iterable[int]] = ..., vchannels: _Optional[_Iterable[str]] = ..., schema: _Optional[_Union[_schema_pb2.CollectionSchema, _Mapping]] = ..., files: _Optional[_Iterable[_Union[_internal_pb2.ImportFile, _Mapping]]] = ..., options: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ..., ts: _Optional[int] = ..., autoID_range: _Optional[_Union[autoIDRange, _Mapping]] = ..., request_segments: _Optional[_Iterable[_Union[ImportRequestSegment, _Mapping]]] = ...) -> None: ...

class QueryPreImportRequest(_message.Message):
    __slots__ = ("clusterID", "jobID", "taskID")
    CLUSTERID_FIELD_NUMBER: _ClassVar[int]
    JOBID_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    clusterID: str
    jobID: int
    taskID: int
    def __init__(self, clusterID: _Optional[str] = ..., jobID: _Optional[int] = ..., taskID: _Optional[int] = ...) -> None: ...

class PartitionImportStats(_message.Message):
    __slots__ = ("partition_rows", "partition_data_size")
    class PartitionRowsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class PartitionDataSizeEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    PARTITION_ROWS_FIELD_NUMBER: _ClassVar[int]
    PARTITION_DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    partition_rows: _containers.ScalarMap[int, int]
    partition_data_size: _containers.ScalarMap[int, int]
    def __init__(self, partition_rows: _Optional[_Mapping[int, int]] = ..., partition_data_size: _Optional[_Mapping[int, int]] = ...) -> None: ...

class ImportFileStats(_message.Message):
    __slots__ = ("import_file", "file_size", "total_rows", "total_memory_size", "hashed_stats")
    class HashedStatsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: PartitionImportStats
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[PartitionImportStats, _Mapping]] = ...) -> None: ...
    IMPORT_FILE_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ROWS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
    HASHED_STATS_FIELD_NUMBER: _ClassVar[int]
    import_file: _internal_pb2.ImportFile
    file_size: int
    total_rows: int
    total_memory_size: int
    hashed_stats: _containers.MessageMap[str, PartitionImportStats]
    def __init__(self, import_file: _Optional[_Union[_internal_pb2.ImportFile, _Mapping]] = ..., file_size: _Optional[int] = ..., total_rows: _Optional[int] = ..., total_memory_size: _Optional[int] = ..., hashed_stats: _Optional[_Mapping[str, PartitionImportStats]] = ...) -> None: ...

class QueryPreImportResponse(_message.Message):
    __slots__ = ("status", "taskID", "state", "reason", "slots", "file_stats")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    SLOTS_FIELD_NUMBER: _ClassVar[int]
    FILE_STATS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    taskID: int
    state: ImportTaskStateV2
    reason: str
    slots: int
    file_stats: _containers.RepeatedCompositeFieldContainer[ImportFileStats]
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., taskID: _Optional[int] = ..., state: _Optional[_Union[ImportTaskStateV2, str]] = ..., reason: _Optional[str] = ..., slots: _Optional[int] = ..., file_stats: _Optional[_Iterable[_Union[ImportFileStats, _Mapping]]] = ...) -> None: ...

class QueryImportRequest(_message.Message):
    __slots__ = ("clusterID", "jobID", "taskID", "querySlot")
    CLUSTERID_FIELD_NUMBER: _ClassVar[int]
    JOBID_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    QUERYSLOT_FIELD_NUMBER: _ClassVar[int]
    clusterID: str
    jobID: int
    taskID: int
    querySlot: bool
    def __init__(self, clusterID: _Optional[str] = ..., jobID: _Optional[int] = ..., taskID: _Optional[int] = ..., querySlot: bool = ...) -> None: ...

class ImportSegmentInfo(_message.Message):
    __slots__ = ("segmentID", "imported_rows", "binlogs", "statslogs")
    SEGMENTID_FIELD_NUMBER: _ClassVar[int]
    IMPORTED_ROWS_FIELD_NUMBER: _ClassVar[int]
    BINLOGS_FIELD_NUMBER: _ClassVar[int]
    STATSLOGS_FIELD_NUMBER: _ClassVar[int]
    segmentID: int
    imported_rows: int
    binlogs: _containers.RepeatedCompositeFieldContainer[FieldBinlog]
    statslogs: _containers.RepeatedCompositeFieldContainer[FieldBinlog]
    def __init__(self, segmentID: _Optional[int] = ..., imported_rows: _Optional[int] = ..., binlogs: _Optional[_Iterable[_Union[FieldBinlog, _Mapping]]] = ..., statslogs: _Optional[_Iterable[_Union[FieldBinlog, _Mapping]]] = ...) -> None: ...

class QueryImportResponse(_message.Message):
    __slots__ = ("status", "taskID", "state", "reason", "slots", "import_segments_info")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    SLOTS_FIELD_NUMBER: _ClassVar[int]
    IMPORT_SEGMENTS_INFO_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    taskID: int
    state: ImportTaskStateV2
    reason: str
    slots: int
    import_segments_info: _containers.RepeatedCompositeFieldContainer[ImportSegmentInfo]
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., taskID: _Optional[int] = ..., state: _Optional[_Union[ImportTaskStateV2, str]] = ..., reason: _Optional[str] = ..., slots: _Optional[int] = ..., import_segments_info: _Optional[_Iterable[_Union[ImportSegmentInfo, _Mapping]]] = ...) -> None: ...

class DropImportRequest(_message.Message):
    __slots__ = ("clusterID", "jobID", "taskID")
    CLUSTERID_FIELD_NUMBER: _ClassVar[int]
    JOBID_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    clusterID: str
    jobID: int
    taskID: int
    def __init__(self, clusterID: _Optional[str] = ..., jobID: _Optional[int] = ..., taskID: _Optional[int] = ...) -> None: ...

class ImportJob(_message.Message):
    __slots__ = ("jobID", "dbID", "collectionID", "partitionIDs", "vchannels", "schema", "timeout_ts", "cleanup_ts", "state", "reason", "files", "options")
    JOBID_FIELD_NUMBER: _ClassVar[int]
    DBID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONIDS_FIELD_NUMBER: _ClassVar[int]
    VCHANNELS_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_TS_FIELD_NUMBER: _ClassVar[int]
    CLEANUP_TS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    jobID: int
    dbID: int
    collectionID: int
    partitionIDs: _containers.RepeatedScalarFieldContainer[int]
    vchannels: _containers.RepeatedScalarFieldContainer[str]
    schema: _schema_pb2.CollectionSchema
    timeout_ts: int
    cleanup_ts: int
    state: _internal_pb2.ImportJobState
    reason: str
    files: _containers.RepeatedCompositeFieldContainer[_internal_pb2.ImportFile]
    options: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    def __init__(self, jobID: _Optional[int] = ..., dbID: _Optional[int] = ..., collectionID: _Optional[int] = ..., partitionIDs: _Optional[_Iterable[int]] = ..., vchannels: _Optional[_Iterable[str]] = ..., schema: _Optional[_Union[_schema_pb2.CollectionSchema, _Mapping]] = ..., timeout_ts: _Optional[int] = ..., cleanup_ts: _Optional[int] = ..., state: _Optional[_Union[_internal_pb2.ImportJobState, str]] = ..., reason: _Optional[str] = ..., files: _Optional[_Iterable[_Union[_internal_pb2.ImportFile, _Mapping]]] = ..., options: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ...) -> None: ...

class PreImportTask(_message.Message):
    __slots__ = ("jobID", "taskID", "collectionID", "nodeID", "state", "reason", "file_stats")
    JOBID_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    NODEID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    FILE_STATS_FIELD_NUMBER: _ClassVar[int]
    jobID: int
    taskID: int
    collectionID: int
    nodeID: int
    state: ImportTaskStateV2
    reason: str
    file_stats: _containers.RepeatedCompositeFieldContainer[ImportFileStats]
    def __init__(self, jobID: _Optional[int] = ..., taskID: _Optional[int] = ..., collectionID: _Optional[int] = ..., nodeID: _Optional[int] = ..., state: _Optional[_Union[ImportTaskStateV2, str]] = ..., reason: _Optional[str] = ..., file_stats: _Optional[_Iterable[_Union[ImportFileStats, _Mapping]]] = ...) -> None: ...

class ImportTaskV2(_message.Message):
    __slots__ = ("jobID", "taskID", "collectionID", "segmentIDs", "nodeID", "state", "reason", "file_stats")
    JOBID_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    SEGMENTIDS_FIELD_NUMBER: _ClassVar[int]
    NODEID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    FILE_STATS_FIELD_NUMBER: _ClassVar[int]
    jobID: int
    taskID: int
    collectionID: int
    segmentIDs: _containers.RepeatedScalarFieldContainer[int]
    nodeID: int
    state: ImportTaskStateV2
    reason: str
    file_stats: _containers.RepeatedCompositeFieldContainer[ImportFileStats]
    def __init__(self, jobID: _Optional[int] = ..., taskID: _Optional[int] = ..., collectionID: _Optional[int] = ..., segmentIDs: _Optional[_Iterable[int]] = ..., nodeID: _Optional[int] = ..., state: _Optional[_Union[ImportTaskStateV2, str]] = ..., reason: _Optional[str] = ..., file_stats: _Optional[_Iterable[_Union[ImportFileStats, _Mapping]]] = ...) -> None: ...

class GcControlRequest(_message.Message):
    __slots__ = ("base", "command", "params")
    BASE_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    command: GcCommand
    params: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., command: _Optional[_Union[GcCommand, str]] = ..., params: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ...) -> None: ...
