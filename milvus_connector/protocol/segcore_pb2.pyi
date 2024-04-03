from . import schema_pb2 as _schema_pb2
from . import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RetrieveResults(_message.Message):
    __slots__ = ("ids", "offset", "fields_data", "all_retrieve_count")
    IDS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    FIELDS_DATA_FIELD_NUMBER: _ClassVar[int]
    ALL_RETRIEVE_COUNT_FIELD_NUMBER: _ClassVar[int]
    ids: _schema_pb2.IDs
    offset: _containers.RepeatedScalarFieldContainer[int]
    fields_data: _containers.RepeatedCompositeFieldContainer[_schema_pb2.FieldData]
    all_retrieve_count: int
    def __init__(self, ids: _Optional[_Union[_schema_pb2.IDs, _Mapping]] = ..., offset: _Optional[_Iterable[int]] = ..., fields_data: _Optional[_Iterable[_Union[_schema_pb2.FieldData, _Mapping]]] = ..., all_retrieve_count: _Optional[int] = ...) -> None: ...

class LoadFieldMeta(_message.Message):
    __slots__ = ("min_timestamp", "max_timestamp", "row_count")
    MIN_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    MAX_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ROW_COUNT_FIELD_NUMBER: _ClassVar[int]
    min_timestamp: int
    max_timestamp: int
    row_count: int
    def __init__(self, min_timestamp: _Optional[int] = ..., max_timestamp: _Optional[int] = ..., row_count: _Optional[int] = ...) -> None: ...

class LoadSegmentMeta(_message.Message):
    __slots__ = ("metas", "total_size")
    METAS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    metas: _containers.RepeatedCompositeFieldContainer[LoadFieldMeta]
    total_size: int
    def __init__(self, metas: _Optional[_Iterable[_Union[LoadFieldMeta, _Mapping]]] = ..., total_size: _Optional[int] = ...) -> None: ...

class InsertRecord(_message.Message):
    __slots__ = ("fields_data", "num_rows")
    FIELDS_DATA_FIELD_NUMBER: _ClassVar[int]
    NUM_ROWS_FIELD_NUMBER: _ClassVar[int]
    fields_data: _containers.RepeatedCompositeFieldContainer[_schema_pb2.FieldData]
    num_rows: int
    def __init__(self, fields_data: _Optional[_Iterable[_Union[_schema_pb2.FieldData, _Mapping]]] = ..., num_rows: _Optional[int] = ...) -> None: ...

class FieldIndexMeta(_message.Message):
    __slots__ = ("fieldID", "collectionID", "index_name", "type_params", "index_params", "is_auto_index", "user_index_params")
    FIELDID_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    INDEX_PARAMS_FIELD_NUMBER: _ClassVar[int]
    IS_AUTO_INDEX_FIELD_NUMBER: _ClassVar[int]
    USER_INDEX_PARAMS_FIELD_NUMBER: _ClassVar[int]
    fieldID: int
    collectionID: int
    index_name: str
    type_params: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    index_params: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    is_auto_index: bool
    user_index_params: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    def __init__(self, fieldID: _Optional[int] = ..., collectionID: _Optional[int] = ..., index_name: _Optional[str] = ..., type_params: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ..., index_params: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ..., is_auto_index: bool = ..., user_index_params: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ...) -> None: ...

class CollectionIndexMeta(_message.Message):
    __slots__ = ("maxIndexRowCount", "index_metas")
    MAXINDEXROWCOUNT_FIELD_NUMBER: _ClassVar[int]
    INDEX_METAS_FIELD_NUMBER: _ClassVar[int]
    maxIndexRowCount: int
    index_metas: _containers.RepeatedCompositeFieldContainer[FieldIndexMeta]
    def __init__(self, maxIndexRowCount: _Optional[int] = ..., index_metas: _Optional[_Iterable[_Union[FieldIndexMeta, _Mapping]]] = ...) -> None: ...
