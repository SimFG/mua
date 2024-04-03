from . import common_pb2 as _common_pb2
from . import schema_pb2 as _schema_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DatabaseState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DatabaseUnknown: _ClassVar[DatabaseState]
    DatabaseCreated: _ClassVar[DatabaseState]
    DatabaseCreating: _ClassVar[DatabaseState]
    DatabaseDropping: _ClassVar[DatabaseState]
    DatabaseDropped: _ClassVar[DatabaseState]

class CollectionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CollectionCreated: _ClassVar[CollectionState]
    CollectionCreating: _ClassVar[CollectionState]
    CollectionDropping: _ClassVar[CollectionState]
    CollectionDropped: _ClassVar[CollectionState]

class PartitionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PartitionCreated: _ClassVar[PartitionState]
    PartitionCreating: _ClassVar[PartitionState]
    PartitionDropping: _ClassVar[PartitionState]
    PartitionDropped: _ClassVar[PartitionState]

class AliasState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AliasCreated: _ClassVar[AliasState]
    AliasCreating: _ClassVar[AliasState]
    AliasDropping: _ClassVar[AliasState]
    AliasDropped: _ClassVar[AliasState]
DatabaseUnknown: DatabaseState
DatabaseCreated: DatabaseState
DatabaseCreating: DatabaseState
DatabaseDropping: DatabaseState
DatabaseDropped: DatabaseState
CollectionCreated: CollectionState
CollectionCreating: CollectionState
CollectionDropping: CollectionState
CollectionDropped: CollectionState
PartitionCreated: PartitionState
PartitionCreating: PartitionState
PartitionDropping: PartitionState
PartitionDropped: PartitionState
AliasCreated: AliasState
AliasCreating: AliasState
AliasDropping: AliasState
AliasDropped: AliasState

class IndexInfo(_message.Message):
    __slots__ = ("index_name", "indexID", "index_params", "deleted", "create_time")
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    INDEXID_FIELD_NUMBER: _ClassVar[int]
    INDEX_PARAMS_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    index_name: str
    indexID: int
    index_params: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    deleted: bool
    create_time: int
    def __init__(self, index_name: _Optional[str] = ..., indexID: _Optional[int] = ..., index_params: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ..., deleted: bool = ..., create_time: _Optional[int] = ...) -> None: ...

class FieldIndexInfo(_message.Message):
    __slots__ = ("filedID", "indexID")
    FILEDID_FIELD_NUMBER: _ClassVar[int]
    INDEXID_FIELD_NUMBER: _ClassVar[int]
    filedID: int
    indexID: int
    def __init__(self, filedID: _Optional[int] = ..., indexID: _Optional[int] = ...) -> None: ...

class CollectionInfo(_message.Message):
    __slots__ = ("ID", "schema", "create_time", "partitionIDs", "partitionNames", "field_indexes", "virtual_channel_names", "physical_channel_names", "partition_created_timestamps", "shards_num", "start_positions", "consistency_level", "state", "properties", "db_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PARTITIONIDS_FIELD_NUMBER: _ClassVar[int]
    PARTITIONNAMES_FIELD_NUMBER: _ClassVar[int]
    FIELD_INDEXES_FIELD_NUMBER: _ClassVar[int]
    VIRTUAL_CHANNEL_NAMES_FIELD_NUMBER: _ClassVar[int]
    PHYSICAL_CHANNEL_NAMES_FIELD_NUMBER: _ClassVar[int]
    PARTITION_CREATED_TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    SHARDS_NUM_FIELD_NUMBER: _ClassVar[int]
    START_POSITIONS_FIELD_NUMBER: _ClassVar[int]
    CONSISTENCY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    DB_ID_FIELD_NUMBER: _ClassVar[int]
    ID: int
    schema: _schema_pb2.CollectionSchema
    create_time: int
    partitionIDs: _containers.RepeatedScalarFieldContainer[int]
    partitionNames: _containers.RepeatedScalarFieldContainer[str]
    field_indexes: _containers.RepeatedCompositeFieldContainer[FieldIndexInfo]
    virtual_channel_names: _containers.RepeatedScalarFieldContainer[str]
    physical_channel_names: _containers.RepeatedScalarFieldContainer[str]
    partition_created_timestamps: _containers.RepeatedScalarFieldContainer[int]
    shards_num: int
    start_positions: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyDataPair]
    consistency_level: _common_pb2.ConsistencyLevel
    state: CollectionState
    properties: _containers.RepeatedCompositeFieldContainer[_common_pb2.KeyValuePair]
    db_id: int
    def __init__(self, ID: _Optional[int] = ..., schema: _Optional[_Union[_schema_pb2.CollectionSchema, _Mapping]] = ..., create_time: _Optional[int] = ..., partitionIDs: _Optional[_Iterable[int]] = ..., partitionNames: _Optional[_Iterable[str]] = ..., field_indexes: _Optional[_Iterable[_Union[FieldIndexInfo, _Mapping]]] = ..., virtual_channel_names: _Optional[_Iterable[str]] = ..., physical_channel_names: _Optional[_Iterable[str]] = ..., partition_created_timestamps: _Optional[_Iterable[int]] = ..., shards_num: _Optional[int] = ..., start_positions: _Optional[_Iterable[_Union[_common_pb2.KeyDataPair, _Mapping]]] = ..., consistency_level: _Optional[_Union[_common_pb2.ConsistencyLevel, str]] = ..., state: _Optional[_Union[CollectionState, str]] = ..., properties: _Optional[_Iterable[_Union[_common_pb2.KeyValuePair, _Mapping]]] = ..., db_id: _Optional[int] = ...) -> None: ...

class PartitionInfo(_message.Message):
    __slots__ = ("partitionID", "partitionName", "partition_created_timestamp", "collection_id", "state")
    PARTITIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONNAME_FIELD_NUMBER: _ClassVar[int]
    PARTITION_CREATED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    partitionID: int
    partitionName: str
    partition_created_timestamp: int
    collection_id: int
    state: PartitionState
    def __init__(self, partitionID: _Optional[int] = ..., partitionName: _Optional[str] = ..., partition_created_timestamp: _Optional[int] = ..., collection_id: _Optional[int] = ..., state: _Optional[_Union[PartitionState, str]] = ...) -> None: ...

class AliasInfo(_message.Message):
    __slots__ = ("alias_name", "collection_id", "created_time", "state", "db_id")
    ALIAS_NAME_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DB_ID_FIELD_NUMBER: _ClassVar[int]
    alias_name: str
    collection_id: int
    created_time: int
    state: AliasState
    db_id: int
    def __init__(self, alias_name: _Optional[str] = ..., collection_id: _Optional[int] = ..., created_time: _Optional[int] = ..., state: _Optional[_Union[AliasState, str]] = ..., db_id: _Optional[int] = ...) -> None: ...

class DatabaseInfo(_message.Message):
    __slots__ = ("tenant_id", "name", "id", "state", "created_time")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIME_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    name: str
    id: int
    state: DatabaseState
    created_time: int
    def __init__(self, tenant_id: _Optional[str] = ..., name: _Optional[str] = ..., id: _Optional[int] = ..., state: _Optional[_Union[DatabaseState, str]] = ..., created_time: _Optional[int] = ...) -> None: ...

class SegmentIndexInfo(_message.Message):
    __slots__ = ("collectionID", "partitionID", "segmentID", "fieldID", "indexID", "buildID", "enable_index", "create_time")
    COLLECTIONID_FIELD_NUMBER: _ClassVar[int]
    PARTITIONID_FIELD_NUMBER: _ClassVar[int]
    SEGMENTID_FIELD_NUMBER: _ClassVar[int]
    FIELDID_FIELD_NUMBER: _ClassVar[int]
    INDEXID_FIELD_NUMBER: _ClassVar[int]
    BUILDID_FIELD_NUMBER: _ClassVar[int]
    ENABLE_INDEX_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    collectionID: int
    partitionID: int
    segmentID: int
    fieldID: int
    indexID: int
    buildID: int
    enable_index: bool
    create_time: int
    def __init__(self, collectionID: _Optional[int] = ..., partitionID: _Optional[int] = ..., segmentID: _Optional[int] = ..., fieldID: _Optional[int] = ..., indexID: _Optional[int] = ..., buildID: _Optional[int] = ..., enable_index: bool = ..., create_time: _Optional[int] = ...) -> None: ...

class CollectionMeta(_message.Message):
    __slots__ = ("ID", "schema", "create_time", "segmentIDs", "partition_tags", "partitionIDs")
    ID_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SEGMENTIDS_FIELD_NUMBER: _ClassVar[int]
    PARTITION_TAGS_FIELD_NUMBER: _ClassVar[int]
    PARTITIONIDS_FIELD_NUMBER: _ClassVar[int]
    ID: int
    schema: _schema_pb2.CollectionSchema
    create_time: int
    segmentIDs: _containers.RepeatedScalarFieldContainer[int]
    partition_tags: _containers.RepeatedScalarFieldContainer[str]
    partitionIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, ID: _Optional[int] = ..., schema: _Optional[_Union[_schema_pb2.CollectionSchema, _Mapping]] = ..., create_time: _Optional[int] = ..., segmentIDs: _Optional[_Iterable[int]] = ..., partition_tags: _Optional[_Iterable[str]] = ..., partitionIDs: _Optional[_Iterable[int]] = ...) -> None: ...

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
