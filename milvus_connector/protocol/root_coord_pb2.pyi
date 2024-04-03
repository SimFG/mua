from . import common_pb2 as _common_pb2
from . import milvus_pb2 as _milvus_pb2
from . import internal_pb2 as _internal_pb2
from . import proxy_pb2 as _proxy_pb2
from . import etcd_meta_pb2 as _etcd_meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AllocTimestampRequest(_message.Message):
    __slots__ = ("base", "count")
    BASE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    count: int
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

class AllocTimestampResponse(_message.Message):
    __slots__ = ("status", "timestamp", "count")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    timestamp: int
    count: int
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., timestamp: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...

class AllocIDRequest(_message.Message):
    __slots__ = ("base", "count")
    BASE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    count: int
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...

class AllocIDResponse(_message.Message):
    __slots__ = ("status", "ID", "count")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    ID: int
    count: int
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., ID: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...

class ImportResult(_message.Message):
    __slots__ = ("status", "task_id", "datanode_id", "state", "segments", "auto_ids", "row_count", "infos")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    DATANODE_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    AUTO_IDS_FIELD_NUMBER: _ClassVar[int]
    ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    INFOS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    task_id: int
    datanode_id: int
    state: _common_pb2.ImportState
    segments: _containers.RepeatedScalarFieldContainer[int]
    auto_ids: _containers.RepeatedScalarFieldContainer[int]
    row_count: int
    infos: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., task_id: _Optional[int] = ..., datanode_id: _Optional[int] = ..., state: _Optional[_Union[_common_pb2.ImportState, str]] = ..., segments: _Optional[_Iterable[int]] = ..., auto_ids: _Optional[_Iterable[int]] = ..., row_count: _Optional[int] = ..., infos: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ...) -> None: ...

class DescribeSegmentsRequest(_message.Message):
    __slots__ = ("base", "collectionID", "segmentIDs")
    BASE_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    SEGMENTIDS_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    collectionID: int
    segmentIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., collectionID: _Optional[int] = ..., segmentIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class SegmentBaseInfo(_message.Message):
    __slots__ = ("collectionID", "partitionID", "segmentID")
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONID_FIELD_NUMBER: _ClassVar[int]
    SEGMENTID_FIELD_NUMBER: _ClassVar[int]
    collectionID: int
    partitionID: int
    segmentID: int
    def __init__(self, collectionID: _Optional[int] = ..., partitionID: _Optional[int] = ..., segmentID: _Optional[int] = ...) -> None: ...

class SegmentInfos(_message.Message):
    __slots__ = ("base_info", "index_infos", "extra_index_infos")
    class ExtraIndexInfosEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _etcd_meta_pb2.IndexInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_etcd_meta_pb2.IndexInfo, _Mapping]] = ...) -> None: ...
    BASE_INFO_FIELD_NUMBER: _ClassVar[int]
    INDEX_INFOS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_INDEX_INFOS_FIELD_NUMBER: _ClassVar[int]
    base_info: SegmentBaseInfo
    index_infos: _containers.RepeatedCompositeFieldContainer[_etcd_meta_pb2.SegmentIndexInfo]
    extra_index_infos: _containers.MessageMap[int, _etcd_meta_pb2.IndexInfo]
    def __init__(self, base_info: _Optional[_Union[SegmentBaseInfo, _Mapping]] = ..., index_infos: _Optional[_Iterable[_Union[_etcd_meta_pb2.SegmentIndexInfo, _Mapping]]] = ..., extra_index_infos: _Optional[_Mapping[int, _etcd_meta_pb2.IndexInfo]] = ...) -> None: ...

class DescribeSegmentsResponse(_message.Message):
    __slots__ = ("status", "collectionID", "segment_infos")
    class SegmentInfosEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: SegmentInfos
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[SegmentInfos, _Mapping]] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_INFOS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    collectionID: int
    segment_infos: _containers.MessageMap[int, SegmentInfos]
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., collectionID: _Optional[int] = ..., segment_infos: _Optional[_Mapping[int, SegmentInfos]] = ...) -> None: ...

class GetCredentialRequest(_message.Message):
    __slots__ = ("base", "username")
    BASE_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    username: str
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., username: _Optional[str] = ...) -> None: ...

class GetCredentialResponse(_message.Message):
    __slots__ = ("status", "username", "password")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    username: str
    password: str
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...
