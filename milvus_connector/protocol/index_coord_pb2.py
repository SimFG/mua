# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: index_coord.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import common_pb2 as common__pb2
from . import internal_pb2 as internal__pb2
from . import milvus_pb2 as milvus__pb2
from . import schema_pb2 as schema__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11index_coord.proto\x12\x12milvus.proto.index\x1a\x0c\x63ommon.proto\x1a\x0einternal.proto\x1a\x0cmilvus.proto\x1a\x0cschema.proto\"\xb4\x03\n\tIndexInfo\x12\x14\n\x0c\x63ollectionID\x18\x01 \x01(\x03\x12\x0f\n\x07\x66ieldID\x18\x02 \x01(\x03\x12\x12\n\nindex_name\x18\x03 \x01(\t\x12\x0f\n\x07indexID\x18\x04 \x01(\x03\x12\x36\n\x0btype_params\x18\x05 \x03(\x0b\x32!.milvus.proto.common.KeyValuePair\x12\x37\n\x0cindex_params\x18\x06 \x03(\x0b\x32!.milvus.proto.common.KeyValuePair\x12\x14\n\x0cindexed_rows\x18\x07 \x01(\x03\x12\x12\n\ntotal_rows\x18\x08 \x01(\x03\x12.\n\x05state\x18\t \x01(\x0e\x32\x1f.milvus.proto.common.IndexState\x12\x1f\n\x17index_state_fail_reason\x18\n \x01(\t\x12\x15\n\ris_auto_index\x18\x0b \x01(\x08\x12<\n\x11user_index_params\x18\x0c \x03(\x0b\x32!.milvus.proto.common.KeyValuePair\x12\x1a\n\x12pending_index_rows\x18\r \x01(\x03\"e\n\nFieldIndex\x12\x31\n\nindex_info\x18\x01 \x01(\x0b\x32\x1d.milvus.proto.index.IndexInfo\x12\x0f\n\x07\x64\x65leted\x18\x02 \x01(\x08\x12\x13\n\x0b\x63reate_time\x18\x03 \x01(\x04\"\x96\x03\n\x0cSegmentIndex\x12\x14\n\x0c\x63ollectionID\x18\x01 \x01(\x03\x12\x13\n\x0bpartitionID\x18\x02 \x01(\x03\x12\x11\n\tsegmentID\x18\x03 \x01(\x03\x12\x10\n\x08num_rows\x18\x04 \x01(\x03\x12\x0f\n\x07indexID\x18\x05 \x01(\x03\x12\x0f\n\x07\x62uildID\x18\x06 \x01(\x03\x12\x0e\n\x06nodeID\x18\x07 \x01(\x03\x12\x15\n\rindex_version\x18\x08 \x01(\x03\x12.\n\x05state\x18\t \x01(\x0e\x32\x1f.milvus.proto.common.IndexState\x12\x13\n\x0b\x66\x61il_reason\x18\n \x01(\t\x12\x17\n\x0findex_file_keys\x18\x0b \x03(\t\x12\x0f\n\x07\x64\x65leted\x18\x0c \x01(\x08\x12\x13\n\x0b\x63reate_time\x18\r \x01(\x04\x12\x16\n\x0eserialize_size\x18\x0e \x01(\x04\x12\x15\n\rwrite_handoff\x18\x0f \x01(\x08\x12\x1d\n\x15\x63urrent_index_version\x18\x10 \x01(\x05\x12\x1b\n\x13index_store_version\x18\x11 \x01(\x03\"\x80\x01\n\x13RegisterNodeRequest\x12*\n\x04\x62\x61se\x18\x01 \x01(\x0b\x32\x1c.milvus.proto.common.MsgBase\x12-\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x1c.milvus.proto.common.Address\x12\x0e\n\x06nodeID\x18\x03 \x01(\x03\"{\n\x14RegisterNodeResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.milvus.proto.common.Status\x12\x36\n\x0binit_params\x18\x02 \x01(\x0b\x32!.milvus.proto.internal.InitParams\"@\n\x14GetIndexStateRequest\x12\x14\n\x0c\x63ollectionID\x18\x01 \x01(\x03\x12\x12\n\nindex_name\x18\x02 \x01(\t\"\x89\x01\n\x15GetIndexStateResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.milvus.proto.common.Status\x12.\n\x05state\x18\x02 \x01(\x0e\x32\x1f.milvus.proto.common.IndexState\x12\x13\n\x0b\x66\x61il_reason\x18\x03 \x01(\t\"[\n\x1bGetSegmentIndexStateRequest\x12\x14\n\x0c\x63ollectionID\x18\x01 \x01(\x03\x12\x12\n\nindex_name\x18\x02 \x01(\t\x12\x12\n\nsegmentIDs\x18\x03 \x03(\x03\"\x7f\n\x11SegmentIndexState\x12\x11\n\tsegmentID\x18\x01 \x01(\x03\x12.\n\x05state\x18\x02 \x01(\x0e\x32\x1f.milvus.proto.common.IndexState\x12\x13\n\x0b\x66\x61il_reason\x18\x03 \x01(\t\x12\x12\n\nindex_name\x18\x04 \x01(\t\"\x82\x01\n\x1cGetSegmentIndexStateResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.milvus.proto.common.Status\x12\x35\n\x06states\x18\x02 \x03(\x0b\x32%.milvus.proto.index.SegmentIndexState\"\xa8\x02\n\x12\x43reateIndexRequest\x12\x14\n\x0c\x63ollectionID\x18\x01 \x01(\x03\x12\x0f\n\x07\x66ieldID\x18\x02 \x01(\x03\x12\x12\n\nindex_name\x18\x03 \x01(\t\x12\x36\n\x0btype_params\x18\x04 \x03(\x0b\x32!.milvus.proto.common.KeyValuePair\x12\x37\n\x0cindex_params\x18\x05 \x03(\x0b\x32!.milvus.proto.common.KeyValuePair\x12\x11\n\ttimestamp\x18\x06 \x01(\x04\x12\x15\n\ris_auto_index\x18\x07 \x01(\x08\x12<\n\x11user_index_params\x18\x08 \x03(\x0b\x32!.milvus.proto.common.KeyValuePair\"p\n\x11\x41lterIndexRequest\x12\x14\n\x0c\x63ollectionID\x18\x01 \x01(\x03\x12\x12\n\nindex_name\x18\x02 \x01(\t\x12\x31\n\x06params\x18\x03 \x03(\x0b\x32!.milvus.proto.common.KeyValuePair\"S\n\x13GetIndexInfoRequest\x12\x14\n\x0c\x63ollectionID\x18\x01 \x01(\x03\x12\x12\n\nsegmentIDs\x18\x02 \x03(\x03\x12\x12\n\nindex_name\x18\x03 \x01(\t\"\xa1\x02\n\x11IndexFilePathInfo\x12\x11\n\tsegmentID\x18\x01 \x01(\x03\x12\x0f\n\x07\x66ieldID\x18\x02 \x01(\x03\x12\x0f\n\x07indexID\x18\x03 \x01(\x03\x12\x0f\n\x07\x62uildID\x18\x04 \x01(\x03\x12\x12\n\nindex_name\x18\x05 \x01(\t\x12\x37\n\x0cindex_params\x18\x06 \x03(\x0b\x32!.milvus.proto.common.KeyValuePair\x12\x18\n\x10index_file_paths\x18\x07 \x03(\t\x12\x17\n\x0fserialized_size\x18\x08 \x01(\x04\x12\x15\n\rindex_version\x18\t \x01(\x03\x12\x10\n\x08num_rows\x18\n \x01(\x03\x12\x1d\n\x15\x63urrent_index_version\x18\x0b \x01(\x05\"\x88\x01\n\x0bSegmentInfo\x12\x14\n\x0c\x63ollectionID\x18\x01 \x01(\x03\x12\x11\n\tsegmentID\x18\x02 \x01(\x03\x12\x14\n\x0c\x65nable_index\x18\x03 \x01(\x08\x12:\n\x0bindex_infos\x18\x04 \x03(\x0b\x32%.milvus.proto.index.IndexFilePathInfo\"\xe9\x01\n\x14GetIndexInfoResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.milvus.proto.common.Status\x12O\n\x0csegment_info\x18\x02 \x03(\x0b\x32\x39.milvus.proto.index.GetIndexInfoResponse.SegmentInfoEntry\x1aS\n\x10SegmentInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.milvus.proto.index.SegmentInfo:\x02\x38\x01\"d\n\x10\x44ropIndexRequest\x12\x14\n\x0c\x63ollectionID\x18\x01 \x01(\x03\x12\x14\n\x0cpartitionIDs\x18\x02 \x03(\x03\x12\x12\n\nindex_name\x18\x03 \x01(\t\x12\x10\n\x08\x64rop_all\x18\x04 \x01(\x08\"S\n\x14\x44\x65scribeIndexRequest\x12\x14\n\x0c\x63ollectionID\x18\x01 \x01(\x03\x12\x12\n\nindex_name\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x04\"x\n\x15\x44\x65scribeIndexResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.milvus.proto.common.Status\x12\x32\n\x0bindex_infos\x18\x02 \x03(\x0b\x32\x1d.milvus.proto.index.IndexInfo\"H\n\x1cGetIndexBuildProgressRequest\x12\x14\n\x0c\x63ollectionID\x18\x01 \x01(\x03\x12\x12\n\nindex_name\x18\x02 \x01(\t\"\x92\x01\n\x1dGetIndexBuildProgressResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.milvus.proto.common.Status\x12\x14\n\x0cindexed_rows\x18\x02 \x01(\x03\x12\x12\n\ntotal_rows\x18\x03 \x01(\x03\x12\x1a\n\x12pending_index_rows\x18\x04 \x01(\x03\"\xa2\x02\n\rStorageConfig\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65ss_keyID\x18\x02 \x01(\t\x12\x19\n\x11secret_access_key\x18\x03 \x01(\t\x12\x0e\n\x06useSSL\x18\x04 \x01(\x08\x12\x13\n\x0b\x62ucket_name\x18\x05 \x01(\t\x12\x11\n\troot_path\x18\x06 \x01(\t\x12\x0e\n\x06useIAM\x18\x07 \x01(\x08\x12\x13\n\x0bIAMEndpoint\x18\x08 \x01(\t\x12\x14\n\x0cstorage_type\x18\t \x01(\t\x12\x18\n\x10use_virtual_host\x18\n \x01(\x08\x12\x0e\n\x06region\x18\x0b \x01(\t\x12\x16\n\x0e\x63loud_provider\x18\x0c \x01(\t\x12\x1a\n\x12request_timeout_ms\x18\r \x01(\x03\"r\n\x11OptionalFieldInfo\x12\x0f\n\x07\x66ieldID\x18\x01 \x01(\x03\x12\x12\n\nfield_name\x18\x02 \x01(\t\x12\x12\n\nfield_type\x18\x03 \x01(\x05\x12\x12\n\ndata_paths\x18\x04 \x03(\t\x12\x10\n\x08\x64\x61ta_ids\x18\x05 \x03(\x03\"\xbf\x05\n\x10\x43reateJobRequest\x12\x11\n\tclusterID\x18\x01 \x01(\t\x12\x19\n\x11index_file_prefix\x18\x02 \x01(\t\x12\x0f\n\x07\x62uildID\x18\x03 \x01(\x03\x12\x12\n\ndata_paths\x18\x04 \x03(\t\x12\x15\n\rindex_version\x18\x05 \x01(\x03\x12\x0f\n\x07indexID\x18\x06 \x01(\x03\x12\x12\n\nindex_name\x18\x07 \x01(\t\x12\x39\n\x0estorage_config\x18\x08 \x01(\x0b\x32!.milvus.proto.index.StorageConfig\x12\x37\n\x0cindex_params\x18\t \x03(\x0b\x32!.milvus.proto.common.KeyValuePair\x12\x36\n\x0btype_params\x18\n \x03(\x0b\x32!.milvus.proto.common.KeyValuePair\x12\x10\n\x08num_rows\x18\x0b \x01(\x03\x12\x1d\n\x15\x63urrent_index_version\x18\x0c \x01(\x05\x12\x14\n\x0c\x63ollectionID\x18\r \x01(\x03\x12\x13\n\x0bpartitionID\x18\x0e \x01(\x03\x12\x11\n\tsegmentID\x18\x0f \x01(\x03\x12\x0f\n\x07\x66ieldID\x18\x10 \x01(\x03\x12\x12\n\nfield_name\x18\x11 \x01(\t\x12\x31\n\nfield_type\x18\x12 \x01(\x0e\x32\x1d.milvus.proto.schema.DataType\x12\x12\n\nstore_path\x18\x13 \x01(\t\x12\x15\n\rstore_version\x18\x14 \x01(\x03\x12\x18\n\x10index_store_path\x18\x15 \x01(\t\x12\x0b\n\x03\x64im\x18\x16 \x01(\x03\x12\x10\n\x08\x64\x61ta_ids\x18\x17 \x03(\x03\x12\x45\n\x16optional_scalar_fields\x18\x18 \x03(\x0b\x32%.milvus.proto.index.OptionalFieldInfo\"7\n\x10QueryJobsRequest\x12\x11\n\tclusterID\x18\x01 \x01(\t\x12\x10\n\x08\x62uildIDs\x18\x02 \x03(\x03\"\xd3\x01\n\rIndexTaskInfo\x12\x0f\n\x07\x62uildID\x18\x01 \x01(\x03\x12.\n\x05state\x18\x02 \x01(\x0e\x32\x1f.milvus.proto.common.IndexState\x12\x17\n\x0findex_file_keys\x18\x03 \x03(\t\x12\x17\n\x0fserialized_size\x18\x04 \x01(\x04\x12\x13\n\x0b\x66\x61il_reason\x18\x05 \x01(\t\x12\x1d\n\x15\x63urrent_index_version\x18\x06 \x01(\x05\x12\x1b\n\x13index_store_version\x18\x07 \x01(\x03\"\x8b\x01\n\x11QueryJobsResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.milvus.proto.common.Status\x12\x11\n\tclusterID\x18\x02 \x01(\t\x12\x36\n\x0bindex_infos\x18\x03 \x03(\x0b\x32!.milvus.proto.index.IndexTaskInfo\"6\n\x0f\x44ropJobsRequest\x12\x11\n\tclusterID\x18\x01 \x01(\t\x12\x10\n\x08\x62uildIDs\x18\x02 \x03(\x03\"\x96\x01\n\x07JobInfo\x12\x10\n\x08num_rows\x18\x01 \x01(\x03\x12\x0b\n\x03\x64im\x18\x02 \x01(\x03\x12\x12\n\nstart_time\x18\x03 \x01(\x03\x12\x10\n\x08\x65nd_time\x18\x04 \x01(\x03\x12\x37\n\x0cindex_params\x18\x05 \x03(\x0b\x32!.milvus.proto.common.KeyValuePair\x12\r\n\x05podID\x18\x06 \x01(\x03\"\x14\n\x12GetJobStatsRequest\"\xe8\x01\n\x13GetJobStatsResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.milvus.proto.common.Status\x12\x15\n\rtotal_job_num\x18\x02 \x01(\x03\x12\x1b\n\x13in_progress_job_num\x18\x03 \x01(\x03\x12\x17\n\x0f\x65nqueue_job_num\x18\x04 \x01(\x03\x12\x12\n\ntask_slots\x18\x05 \x01(\x03\x12.\n\tjob_infos\x18\x06 \x03(\x0b\x32\x1b.milvus.proto.index.JobInfo\x12\x13\n\x0b\x65nable_disk\x18\x07 \x01(\x08\"E\n\x19GetIndexStatisticsRequest\x12\x14\n\x0c\x63ollectionID\x18\x01 \x01(\x03\x12\x12\n\nindex_name\x18\x02 \x01(\t\"}\n\x1aGetIndexStatisticsResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.milvus.proto.common.Status\x12\x32\n\x0bindex_infos\x18\x02 \x03(\x0b\x32\x1d.milvus.proto.index.IndexInfo\"*\n\x12ListIndexesRequest\x12\x14\n\x0c\x63ollectionID\x18\x01 \x01(\x03\"v\n\x13ListIndexesResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.milvus.proto.common.Status\x12\x32\n\x0bindex_infos\x18\x02 \x03(\x0b\x32\x1d.milvus.proto.index.IndexInfo2\xd5\x0b\n\nIndexCoord\x12l\n\x12GetComponentStates\x12..milvus.proto.milvus.GetComponentStatesRequest\x1a$.milvus.proto.milvus.ComponentStates\"\x00\x12q\n\x14GetStatisticsChannel\x12\x32.milvus.proto.internal.GetStatisticsChannelRequest\x1a#.milvus.proto.milvus.StringResponse\"\x00\x12T\n\x0b\x43reateIndex\x12&.milvus.proto.index.CreateIndexRequest\x1a\x1b.milvus.proto.common.Status\"\x00\x12R\n\nAlterIndex\x12%.milvus.proto.index.AlterIndexRequest\x1a\x1b.milvus.proto.common.Status\"\x00\x12\x66\n\rGetIndexState\x12(.milvus.proto.index.GetIndexStateRequest\x1a).milvus.proto.index.GetIndexStateResponse\"\x00\x12{\n\x14GetSegmentIndexState\x12/.milvus.proto.index.GetSegmentIndexStateRequest\x1a\x30.milvus.proto.index.GetSegmentIndexStateResponse\"\x00\x12\x64\n\rGetIndexInfos\x12\'.milvus.proto.index.GetIndexInfoRequest\x1a(.milvus.proto.index.GetIndexInfoResponse\"\x00\x12P\n\tDropIndex\x12$.milvus.proto.index.DropIndexRequest\x1a\x1b.milvus.proto.common.Status\"\x00\x12\x66\n\rDescribeIndex\x12(.milvus.proto.index.DescribeIndexRequest\x1a).milvus.proto.index.DescribeIndexResponse\"\x00\x12u\n\x12GetIndexStatistics\x12-.milvus.proto.index.GetIndexStatisticsRequest\x1a..milvus.proto.index.GetIndexStatisticsResponse\"\x00\x12~\n\x15GetIndexBuildProgress\x12\x30.milvus.proto.index.GetIndexBuildProgressRequest\x1a\x31.milvus.proto.index.GetIndexBuildProgressResponse\"\x00\x12{\n\x12ShowConfigurations\x12\x30.milvus.proto.internal.ShowConfigurationsRequest\x1a\x31.milvus.proto.internal.ShowConfigurationsResponse\"\x00\x12_\n\nGetMetrics\x12&.milvus.proto.milvus.GetMetricsRequest\x1a\'.milvus.proto.milvus.GetMetricsResponse\"\x00\x12\x62\n\x0b\x43heckHealth\x12\'.milvus.proto.milvus.CheckHealthRequest\x1a(.milvus.proto.milvus.CheckHealthResponse\"\x00\x32\xaa\x06\n\tIndexNode\x12l\n\x12GetComponentStates\x12..milvus.proto.milvus.GetComponentStatesRequest\x1a$.milvus.proto.milvus.ComponentStates\"\x00\x12q\n\x14GetStatisticsChannel\x12\x32.milvus.proto.internal.GetStatisticsChannelRequest\x1a#.milvus.proto.milvus.StringResponse\"\x00\x12P\n\tCreateJob\x12$.milvus.proto.index.CreateJobRequest\x1a\x1b.milvus.proto.common.Status\"\x00\x12Z\n\tQueryJobs\x12$.milvus.proto.index.QueryJobsRequest\x1a%.milvus.proto.index.QueryJobsResponse\"\x00\x12N\n\x08\x44ropJobs\x12#.milvus.proto.index.DropJobsRequest\x1a\x1b.milvus.proto.common.Status\"\x00\x12`\n\x0bGetJobStats\x12&.milvus.proto.index.GetJobStatsRequest\x1a\'.milvus.proto.index.GetJobStatsResponse\"\x00\x12{\n\x12ShowConfigurations\x12\x30.milvus.proto.internal.ShowConfigurationsRequest\x1a\x31.milvus.proto.internal.ShowConfigurationsResponse\"\x00\x12_\n\nGetMetrics\x12&.milvus.proto.milvus.GetMetricsRequest\x1a\'.milvus.proto.milvus.GetMetricsResponse\"\x00\x42\x34Z2github.com/milvus-io/milvus/internal/proto/indexpbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'index_coord_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z2github.com/milvus-io/milvus/internal/proto/indexpb'
  _globals['_GETINDEXINFORESPONSE_SEGMENTINFOENTRY']._options = None
  _globals['_GETINDEXINFORESPONSE_SEGMENTINFOENTRY']._serialized_options = b'8\001'
  _globals['_INDEXINFO']._serialized_start=100
  _globals['_INDEXINFO']._serialized_end=536
  _globals['_FIELDINDEX']._serialized_start=538
  _globals['_FIELDINDEX']._serialized_end=639
  _globals['_SEGMENTINDEX']._serialized_start=642
  _globals['_SEGMENTINDEX']._serialized_end=1048
  _globals['_REGISTERNODEREQUEST']._serialized_start=1051
  _globals['_REGISTERNODEREQUEST']._serialized_end=1179
  _globals['_REGISTERNODERESPONSE']._serialized_start=1181
  _globals['_REGISTERNODERESPONSE']._serialized_end=1304
  _globals['_GETINDEXSTATEREQUEST']._serialized_start=1306
  _globals['_GETINDEXSTATEREQUEST']._serialized_end=1370
  _globals['_GETINDEXSTATERESPONSE']._serialized_start=1373
  _globals['_GETINDEXSTATERESPONSE']._serialized_end=1510
  _globals['_GETSEGMENTINDEXSTATEREQUEST']._serialized_start=1512
  _globals['_GETSEGMENTINDEXSTATEREQUEST']._serialized_end=1603
  _globals['_SEGMENTINDEXSTATE']._serialized_start=1605
  _globals['_SEGMENTINDEXSTATE']._serialized_end=1732
  _globals['_GETSEGMENTINDEXSTATERESPONSE']._serialized_start=1735
  _globals['_GETSEGMENTINDEXSTATERESPONSE']._serialized_end=1865
  _globals['_CREATEINDEXREQUEST']._serialized_start=1868
  _globals['_CREATEINDEXREQUEST']._serialized_end=2164
  _globals['_ALTERINDEXREQUEST']._serialized_start=2166
  _globals['_ALTERINDEXREQUEST']._serialized_end=2278
  _globals['_GETINDEXINFOREQUEST']._serialized_start=2280
  _globals['_GETINDEXINFOREQUEST']._serialized_end=2363
  _globals['_INDEXFILEPATHINFO']._serialized_start=2366
  _globals['_INDEXFILEPATHINFO']._serialized_end=2655
  _globals['_SEGMENTINFO']._serialized_start=2658
  _globals['_SEGMENTINFO']._serialized_end=2794
  _globals['_GETINDEXINFORESPONSE']._serialized_start=2797
  _globals['_GETINDEXINFORESPONSE']._serialized_end=3030
  _globals['_GETINDEXINFORESPONSE_SEGMENTINFOENTRY']._serialized_start=2947
  _globals['_GETINDEXINFORESPONSE_SEGMENTINFOENTRY']._serialized_end=3030
  _globals['_DROPINDEXREQUEST']._serialized_start=3032
  _globals['_DROPINDEXREQUEST']._serialized_end=3132
  _globals['_DESCRIBEINDEXREQUEST']._serialized_start=3134
  _globals['_DESCRIBEINDEXREQUEST']._serialized_end=3217
  _globals['_DESCRIBEINDEXRESPONSE']._serialized_start=3219
  _globals['_DESCRIBEINDEXRESPONSE']._serialized_end=3339
  _globals['_GETINDEXBUILDPROGRESSREQUEST']._serialized_start=3341
  _globals['_GETINDEXBUILDPROGRESSREQUEST']._serialized_end=3413
  _globals['_GETINDEXBUILDPROGRESSRESPONSE']._serialized_start=3416
  _globals['_GETINDEXBUILDPROGRESSRESPONSE']._serialized_end=3562
  _globals['_STORAGECONFIG']._serialized_start=3565
  _globals['_STORAGECONFIG']._serialized_end=3855
  _globals['_OPTIONALFIELDINFO']._serialized_start=3857
  _globals['_OPTIONALFIELDINFO']._serialized_end=3971
  _globals['_CREATEJOBREQUEST']._serialized_start=3974
  _globals['_CREATEJOBREQUEST']._serialized_end=4677
  _globals['_QUERYJOBSREQUEST']._serialized_start=4679
  _globals['_QUERYJOBSREQUEST']._serialized_end=4734
  _globals['_INDEXTASKINFO']._serialized_start=4737
  _globals['_INDEXTASKINFO']._serialized_end=4948
  _globals['_QUERYJOBSRESPONSE']._serialized_start=4951
  _globals['_QUERYJOBSRESPONSE']._serialized_end=5090
  _globals['_DROPJOBSREQUEST']._serialized_start=5092
  _globals['_DROPJOBSREQUEST']._serialized_end=5146
  _globals['_JOBINFO']._serialized_start=5149
  _globals['_JOBINFO']._serialized_end=5299
  _globals['_GETJOBSTATSREQUEST']._serialized_start=5301
  _globals['_GETJOBSTATSREQUEST']._serialized_end=5321
  _globals['_GETJOBSTATSRESPONSE']._serialized_start=5324
  _globals['_GETJOBSTATSRESPONSE']._serialized_end=5556
  _globals['_GETINDEXSTATISTICSREQUEST']._serialized_start=5558
  _globals['_GETINDEXSTATISTICSREQUEST']._serialized_end=5627
  _globals['_GETINDEXSTATISTICSRESPONSE']._serialized_start=5629
  _globals['_GETINDEXSTATISTICSRESPONSE']._serialized_end=5754
  _globals['_LISTINDEXESREQUEST']._serialized_start=5756
  _globals['_LISTINDEXESREQUEST']._serialized_end=5798
  _globals['_LISTINDEXESRESPONSE']._serialized_start=5800
  _globals['_LISTINDEXESRESPONSE']._serialized_end=5918
  _globals['_INDEXCOORD']._serialized_start=5921
  _globals['_INDEXCOORD']._serialized_end=7414
  _globals['_INDEXNODE']._serialized_start=7417
  _globals['_INDEXNODE']._serialized_end=8227
# @@protoc_insertion_point(module_scope)