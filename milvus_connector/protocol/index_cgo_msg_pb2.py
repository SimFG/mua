# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: index_cgo_msg.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13index_cgo_msg.proto\x12\x15milvus.proto.indexcgo\x1a\x0c\x63ommon.proto\"?\n\nTypeParams\x12\x31\n\x06params\x18\x01 \x03(\x0b\x32!.milvus.proto.common.KeyValuePair\"@\n\x0bIndexParams\x12\x31\n\x06params\x18\x01 \x03(\x0b\x32!.milvus.proto.common.KeyValuePair\">\n\tMapParams\x12\x31\n\x06params\x18\x01 \x03(\x0b\x32!.milvus.proto.common.KeyValuePair\"|\n\x0bMapParamsV2\x12>\n\x06params\x18\x01 \x03(\x0b\x32..milvus.proto.indexcgo.MapParamsV2.ParamsEntry\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"$\n\x06\x42inary\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\"9\n\tBinarySet\x12,\n\x05\x64\x61tas\x18\x01 \x03(\x0b\x32\x1d.milvus.proto.indexcgo.BinaryB7Z5github.com/milvus-io/milvus/internal/proto/indexcgopbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'index_cgo_msg_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z5github.com/milvus-io/milvus/internal/proto/indexcgopb'
  _globals['_MAPPARAMSV2_PARAMSENTRY']._options = None
  _globals['_MAPPARAMSV2_PARAMSENTRY']._serialized_options = b'8\001'
  _globals['_TYPEPARAMS']._serialized_start=60
  _globals['_TYPEPARAMS']._serialized_end=123
  _globals['_INDEXPARAMS']._serialized_start=125
  _globals['_INDEXPARAMS']._serialized_end=189
  _globals['_MAPPARAMS']._serialized_start=191
  _globals['_MAPPARAMS']._serialized_end=253
  _globals['_MAPPARAMSV2']._serialized_start=255
  _globals['_MAPPARAMSV2']._serialized_end=379
  _globals['_MAPPARAMSV2_PARAMSENTRY']._serialized_start=334
  _globals['_MAPPARAMSV2_PARAMSENTRY']._serialized_end=379
  _globals['_BINARY']._serialized_start=381
  _globals['_BINARY']._serialized_end=417
  _globals['_BINARYSET']._serialized_start=419
  _globals['_BINARYSET']._serialized_end=476
# @@protoc_insertion_point(module_scope)
