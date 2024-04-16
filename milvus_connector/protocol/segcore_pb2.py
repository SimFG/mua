# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: segcore.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import schema_pb2 as schema__pb2
from . import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rsegcore.proto\x12\x14milvus.proto.segcore\x1a\x0cschema.proto\x1a\x0c\x63ommon.proto\"\x99\x01\n\x0fRetrieveResults\x12%\n\x03ids\x18\x01 \x01(\x0b\x32\x18.milvus.proto.schema.IDs\x12\x0e\n\x06offset\x18\x02 \x03(\x03\x12\x33\n\x0b\x66ields_data\x18\x03 \x03(\x0b\x32\x1e.milvus.proto.schema.FieldData\x12\x1a\n\x12\x61ll_retrieve_count\x18\x04 \x01(\x03\"P\n\rLoadFieldMeta\x12\x15\n\rmin_timestamp\x18\x01 \x01(\x03\x12\x15\n\rmax_timestamp\x18\x02 \x01(\x03\x12\x11\n\trow_count\x18\x03 \x01(\x03\"Y\n\x0fLoadSegmentMeta\x12\x32\n\x05metas\x18\x01 \x03(\x0b\x32#.milvus.proto.segcore.LoadFieldMeta\x12\x12\n\ntotal_size\x18\x02 \x01(\x03\"U\n\x0cInsertRecord\x12\x33\n\x0b\x66ields_data\x18\x01 \x03(\x0b\x32\x1e.milvus.proto.schema.FieldData\x12\x10\n\x08num_rows\x18\x02 \x01(\x03\"\x91\x02\n\x0e\x46ieldIndexMeta\x12\x0f\n\x07\x66ieldID\x18\x01 \x01(\x03\x12\x14\n\x0c\x63ollectionID\x18\x02 \x01(\x03\x12\x12\n\nindex_name\x18\x03 \x01(\t\x12\x36\n\x0btype_params\x18\x04 \x03(\x0b\x32!.milvus.proto.common.KeyValuePair\x12\x37\n\x0cindex_params\x18\x05 \x03(\x0b\x32!.milvus.proto.common.KeyValuePair\x12\x15\n\ris_auto_index\x18\x06 \x01(\x08\x12<\n\x11user_index_params\x18\x07 \x03(\x0b\x32!.milvus.proto.common.KeyValuePair\"j\n\x13\x43ollectionIndexMeta\x12\x18\n\x10maxIndexRowCount\x18\x01 \x01(\x03\x12\x39\n\x0bindex_metas\x18\x02 \x03(\x0b\x32$.milvus.proto.segcore.FieldIndexMetaB6Z4github.com/milvus-io/milvus/internal/proto/segcorepbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'segcore_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z4github.com/milvus-io/milvus/internal/proto/segcorepb'
  _globals['_RETRIEVERESULTS']._serialized_start=68
  _globals['_RETRIEVERESULTS']._serialized_end=221
  _globals['_LOADFIELDMETA']._serialized_start=223
  _globals['_LOADFIELDMETA']._serialized_end=303
  _globals['_LOADSEGMENTMETA']._serialized_start=305
  _globals['_LOADSEGMENTMETA']._serialized_end=394
  _globals['_INSERTRECORD']._serialized_start=396
  _globals['_INSERTRECORD']._serialized_end=481
  _globals['_FIELDINDEXMETA']._serialized_start=484
  _globals['_FIELDINDEXMETA']._serialized_end=757
  _globals['_COLLECTIONINDEXMETA']._serialized_start=759
  _globals['_COLLECTIONINDEXMETA']._serialized_end=865
# @@protoc_insertion_point(module_scope)