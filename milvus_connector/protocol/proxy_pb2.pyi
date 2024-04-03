from . import common_pb2 as _common_pb2
from . import internal_pb2 as _internal_pb2
from . import milvus_pb2 as _milvus_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InvalidateCollMetaCacheRequest(_message.Message):
    __slots__ = ("base", "db_name", "collection_name", "collectionID", "partition_name")
    BASE_FIELD_NUMBER: _ClassVar[int]
    DB_NAME_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITION_NAME_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    db_name: str
    collection_name: str
    collectionID: int
    partition_name: str
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., db_name: _Optional[str] = ..., collection_name: _Optional[str] = ..., collectionID: _Optional[int] = ..., partition_name: _Optional[str] = ...) -> None: ...

class InvalidateCredCacheRequest(_message.Message):
    __slots__ = ("base", "username")
    BASE_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    username: str
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., username: _Optional[str] = ...) -> None: ...

class UpdateCredCacheRequest(_message.Message):
    __slots__ = ("base", "username", "password")
    BASE_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    username: str
    password: str
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class RefreshPolicyInfoCacheRequest(_message.Message):
    __slots__ = ("base", "opType", "opKey")
    BASE_FIELD_NUMBER: _ClassVar[int]
    OPTYPE_FIELD_NUMBER: _ClassVar[int]
    OPKEY_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    opType: int
    opKey: str
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., opType: _Optional[int] = ..., opKey: _Optional[str] = ...) -> None: ...

class CollectionRate(_message.Message):
    __slots__ = ("collection", "rates", "states", "codes")
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    RATES_FIELD_NUMBER: _ClassVar[int]
    STATES_FIELD_NUMBER: _ClassVar[int]
    CODES_FIELD_NUMBER: _ClassVar[int]
    collection: int
    rates: _containers.RepeatedCompositeFieldContainer[_internal_pb2.Rate]
    states: _containers.RepeatedScalarFieldContainer[_milvus_pb2.QuotaState]
    codes: _containers.RepeatedScalarFieldContainer[_common_pb2.ErrorCode]
    def __init__(self, collection: _Optional[int] = ..., rates: _Optional[_Iterable[_Union[_internal_pb2.Rate, _Mapping]]] = ..., states: _Optional[_Iterable[_Union[_milvus_pb2.QuotaState, str]]] = ..., codes: _Optional[_Iterable[_Union[_common_pb2.ErrorCode, str]]] = ...) -> None: ...

class SetRatesRequest(_message.Message):
    __slots__ = ("base", "rates")
    BASE_FIELD_NUMBER: _ClassVar[int]
    RATES_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    rates: _containers.RepeatedCompositeFieldContainer[CollectionRate]
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ..., rates: _Optional[_Iterable[_Union[CollectionRate, _Mapping]]] = ...) -> None: ...

class ListClientInfosRequest(_message.Message):
    __slots__ = ("base",)
    BASE_FIELD_NUMBER: _ClassVar[int]
    base: _common_pb2.MsgBase
    def __init__(self, base: _Optional[_Union[_common_pb2.MsgBase, _Mapping]] = ...) -> None: ...

class ListClientInfosResponse(_message.Message):
    __slots__ = ("status", "client_infos")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_INFOS_FIELD_NUMBER: _ClassVar[int]
    status: _common_pb2.Status
    client_infos: _containers.RepeatedCompositeFieldContainer[_common_pb2.ClientInfo]
    def __init__(self, status: _Optional[_Union[_common_pb2.Status, _Mapping]] = ..., client_infos: _Optional[_Iterable[_Union[_common_pb2.ClientInfo, _Mapping]]] = ...) -> None: ...
