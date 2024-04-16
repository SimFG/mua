import base64
import copy
import datetime
import json
import struct
from typing import Any, Dict, List, Optional, Union, Literal
from typing_extensions import Self, deprecated

import grpc
from google.protobuf import json_format
from furl import furl
from pydantic import validate_call

from ..protocol.milvus_pb2_grpc import MilvusServiceStub
from ..protocol.milvus_pb2 import *
from ..protocol.common_pb2 import *
from ..protocol.schema_pb2 import *
from ..protocol.feder_pb2 import *
from ._param import RPCParam
from ._const import *
from ._types import *
from .util import CollectionField, Data
from .._interceptor import header_adder_interceptor


class Milvus(RPCParam):
    stub: MilvusServiceStub
    channel: Optional[grpc.Channel] = None
    style: str

    def __init__(self, *,
                 uri: str = "localhost:19530",
                 token: str = "root:Milvus",
                 database: str = "default",
                 response_style: Union[str, Literal[
                     "json",
                     "object",
                     ]] = "object",
                 milvus: Optional[Self] = None,
                 ) -> None:
        if milvus:
            self.stub = milvus.stub
            self.style = milvus.style
            self.params = copy.deepcopy(milvus.params)
            return
        self.style = response_style.lower()
        if not uri.startswith("http"):
            uri = "http://" + uri
        _secure = uri.startswith("https://")
        _header_key = list()
        _header_value = list()
        if token:
            _header_key.append("authorization")
            _header_value.append(base64.b64encode(f"{token}".encode()))
        if database:
            _header_key.append("dbname")
            _header_value.append(database)

        _netloc = furl(uri).netloc
        if _secure:
            creds = grpc.ssl_channel_credentials()
            _channel = grpc.secure_channel(_netloc, creds)
        else:
            _channel = grpc.insecure_channel(_netloc)

        if _header_key:
            interceptor = header_adder_interceptor(_header_key, _header_value)
            _channel = grpc.intercept_channel(_channel, interceptor)
        self.stub = MilvusServiceStub(_channel)
        self.channel = _channel

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.channel:
            self.channel.close()

    def _is_json(self) -> bool:
        return self.style == "json"

    def _intercept_resp(self, resp: Any)->None:
        pass

    def json(self) -> Self:
        m = Milvus(milvus=self)
        m.style = "json"
        return m

    def with_params(self, *, params: Dict[str, Any] = dict()) -> Self:
        m = Milvus(milvus=self)
        m.extend_params(params)
        return m

    @validate_call
    def with_db(self, *, name: NOT_EMPTY_STR) -> Self:
        m = Milvus(milvus=self)
        m.add_param(DB_NAME, name)
        return m

    @validate_call
    def with_collection(self, *, name: NOT_EMPTY_STR) -> Self:
        m = Milvus(milvus=self)
        m.add_param(COLLECTION_NAME, name)
        return m

    @validate_call
    def with_partition(self, *, name: NOT_EMPTY_STR) -> Self:
        m = Milvus(milvus=self)
        m.add_param(PARTITION_NAME, name)
        return m

    def create_collection(self, *,
                          db_name: str = "",
                          collection_name: str = "",
                          shard_num: int = 1,
                          consistency_level: CONSISTENCY_LEVEL = "bounded",
                          properties: Optional[Dict[str, str]] = None,
                          num_partitions: int = 0,
                          collection_description: str = "",
                          auto_id: bool = False,
                          enable_dynamic_field: bool = False,
                          schema_properties: Optional[Dict[str, str]] = None,
                          fields: List[CollectionField] = [],
                          ) -> Union[Status, str]:
        if len(fields) == 0:
            raise ValueError("Fields should not be empty")
        pk_cnt = 0
        for field in fields:
            if field.obj.is_primary_key:
                pk_cnt += 1
        if pk_cnt > 1:
            raise ValueError("There should be only one primary key")
        if pk_cnt == 0:
            raise ValueError("There should be at least one primary key")

        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        schema = CollectionSchema(
            name=_collection_name,
            description=collection_description,
            autoID=auto_id,
            fields=[field.obj for field in fields],
            enable_dynamic_field=enable_dynamic_field,
            properties=[KeyValuePair(key=k, value=v) for k, v in (schema_properties or {}).items()],
        )
        resp = self.stub.CreateCollection(
            CreateCollectionRequest(
                db_name=_db_name,
                collection_name=_collection_name,
                schema=bytes(schema.SerializeToString()),
                shards_num=shard_num,
                consistency_level=get_consistency_level(consistency_level),
                properties=[KeyValuePair(key=k, value=v) for k, v in (properties or {}).items()],
                num_partitions=num_partitions,
            )
        )
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def drop_collection(self, *,
                        db_name: str = "",
                        collection_name: str = "",
                        ) -> Union[Status, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        resp = self.stub.DropCollection(DropCollectionRequest(db_name=_db_name, collection_name=_collection_name))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def alter_collection(self, *,
                         db_name: str = "",
                         collection_name: str = "",
                         collection_id: int = 0,
                         properties: Dict[str, str] = None,
                         ) -> Union[Status, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        resp = self.stub.AlterCollection(AlterCollectionRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            collectionID=collection_id,
            properties=[KeyValuePair(key=k, value=v) for k, v in (properties or {}).items()],
            ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    @deprecated("Use describe_collection instead")
    def has_collection(self, *,
                          db_name: str = "",
                          collection_name: str = "",
                          time_stamp: int = 0,
                          ) -> Union[BoolResponse, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        resp = self.stub.HasCollection(HasCollectionRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            time_stamp=time_stamp,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def describe_collection(self, *,
                            db_name: str = "",
                            collection_name: str = "",
                            collection_id: int = 0,
                            time_stamp: int = 0,
                            ) -> Union[DescribeCollectionResponse, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        resp = self.stub.DescribeCollection(DescribeCollectionRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            collectionID=collection_id,
            time_stamp=time_stamp,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def load_collection(self, *,
                        db_name: str = "",
                        collection_name: str = "",
                        replica_number: int = 1,
                        resource_groups: Optional[List[str]] = None,
                        refresh: bool = False,
                        ) -> Union[Status, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        resp = self.stub.LoadCollection(LoadCollectionRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            replica_number=replica_number,
            resource_groups=resource_groups or [],
            refresh=refresh,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def release_collection(self, *,
                           db_name: str = "",
                           collection_name: str = "",
                           ) -> Union[Status, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        resp = self.stub.ReleaseCollection(ReleaseCollectionRequest(db_name=_db_name, collection_name=_collection_name))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def get_collection_statistics(self, *,
                                    db_name: str = "",
                                    collection_name: str = "",
                                    ) -> Union[GetCollectionStatisticsResponse, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        resp = self.stub.GetCollectionStatistics(GetCollectionStatisticsRequest(db_name=_db_name, collection_name=_collection_name))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def show_collections(self, *,
                         db_name: str = "",
                         ) -> Union[ShowCollectionsResponse, str]:
        _db_name = db_name or self._db_name()
        resp = self.stub.ShowCollections(ShowCollectionsRequest(db_name=_db_name))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def insert(self, *,
               db_name: str = "",
               collection_name: str = "",
               partition_name: str = "",
               fields_data: List[Data] = None,
               num_rows: int = 0,
               ) -> Union[MutationResult, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        _partition_name = partition_name or self._partition_name()
        req = InsertRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            partition_name=_partition_name,
            fields_data=[d.construct_data() for d in fields_data],
            num_rows=num_rows,
        )
        resp = self.stub.Insert(req)
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def delete(self, *,
               db_name: str = "",
               collection_name: str = "",
               partition_name: str = "",
               expr: str = "",
               consistency_level: CONSISTENCY_LEVEL = "strong",
               ) -> Union[MutationResult, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        _partition_name = partition_name or self._partition_name()
        req = DeleteRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            partition_name=_partition_name,
            expr=expr,
            consistency_level=get_consistency_level(consistency_level),
        )
        resp = self.stub.Delete(req)
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def upsert(self, *,
               db_name: str = "",
               collection_name: str = "",
               partition_name: str = "",
               fields_data: List[Data] = None,
               num_rows: int = 0,
               ) -> Union[MutationResult, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        _partition_name = partition_name or self._partition_name()
        req = UpsertRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            partition_name=_partition_name,
            fields_data=[d.construct_data() for d in fields_data],
            num_rows=num_rows,
        )
        resp = self.stub.Upsert(req)
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def construct_search_request(self, *,
               # common params
               db_name: str = "",
               collection_name: str = "",
               partition_names: List[str] = [],
               expr: str = "",
               output_fields: List[str] = None,
               vector_field: str = None,
               top_k: int = 10,
               metric_type: str = "L2",
               search_data: List[Union[List[float], bytes]] = None,
               # more params
               search_params: Dict[str, Any] = None,
               round_decimal: int = -1,
               ignore_growing: bool = False,
               offset: int = 0,
               extra_params: Optional[Dict[str, Any]] = None,
               iterator: str = "",
               group_by_field: str = "",
               guarantee_timestamp: int = 0,
               not_return_all_meta: bool = False,
               consistency_level: CONSISTENCY_LEVEL = "strong",
               use_default_consistency: bool = False,
               search_by_primary_keys: bool = False,
               ) -> SearchRequest:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        search_params = search_params or {}
        search_params["round_decimal"] = round_decimal
        search_params["ignore_growing"] = ignore_growing
        search_params["topk"] = top_k
        search_params["params"] = extra_params or {}
        search_params["anns_field"] = vector_field
        if offset > 0:
            search_params["offset"] = offset
        if iterator:
            search_params["iterator"] = iterator
        if group_by_field:
            search_params["group_by_field"] = group_by_field
        if metric_type:
            search_params["metric_type"] = metric_type
        is_binary, pl_type = (True, PlaceholderType.BinaryVector) if isinstance(search_data[0], bytes) else (False, PlaceholderType.FloatVector)
        nq, tag = len(search_data), "$0"
        plg = PlaceholderGroup(
            placeholders=[PlaceholderValue(
                tag=tag,
                type=pl_type,
                values=[bytes(d) if is_binary else struct.pack(f"{len(d)}f", *d) for d in search_data],
                )],
        )

        return SearchRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            partition_names=partition_names,
            dsl=expr,
            dsl_type=DslType.BoolExprV1,
            placeholder_group=PlaceholderGroup.SerializeToString(plg),
            output_fields=output_fields,
            search_params=[KeyValuePair(key=k, value=json.dumps(v) if isinstance(v, dict) else str(v)) for k, v in search_params.items()],
            travel_timestamp=0,
            guarantee_timestamp=guarantee_timestamp,
            nq=nq,
            not_return_all_meta=not_return_all_meta,
            consistency_level=get_consistency_level(consistency_level),
            use_default_consistency=use_default_consistency,
            search_by_primary_keys=search_by_primary_keys,
        )

    def search(self, *, req: SearchRequest) -> Union[SearchResults, str]:
        resp = self.stub.Search(req)
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def hybrid_search(self, *,
                      db_name: str = "",
                      collection_name: str = "",
                      partition_names: List[str] = [],
                      reqs: List[SearchRequest] = None,
                      rank_params: Dict[str, str] = None,
                      guarantee_timestamp: int = 0,
                      not_return_all_meta: bool = False,
                      output_fields: List[str] = None,
                      consistency_level: CONSISTENCY_LEVEL = "bounded",
                      use_default_consistency: bool = False,
                      ) -> Union[SearchResults, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        resp = self.stub.HybridSearch(HybridSearchRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            partition_names=partition_names,
            requests=reqs,
            rank_params=[KeyValuePair(key=k, value=v) for k, v in (rank_params or {}).items()],
            guarantee_timestamp=guarantee_timestamp,
            not_return_all_meta=not_return_all_meta,
            output_fields=output_fields,
            consistency_level=get_consistency_level(consistency_level),
            use_default_consistency=use_default_consistency,
            ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def flush(self, *,
              db_name: str = "",
              collection_names: List[str] = [],
              ) -> Union[FlushResponse, str]:
        _db_name = db_name or self._db_name()
        _collection_names = [self._collection_name()] if len(collection_names) == 0 else collection_names
        resp = self.stub.Flush(FlushRequest(db_name=_db_name, collection_names=_collection_names))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def get_flush_state(self, *,
                        db_name: str = "",
                        collection_name: str = "",
                        segmentIDs: List[int] = [],
                        flush_ts: int = 0,
                        ) -> Union[GetFlushStateResponse, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        resp = self.stub.GetFlushState(GetFlushStateRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            segmentIDs=segmentIDs,
            flush_ts=flush_ts,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def query(self, *,
              db_name: str = "",
              collection_name: str = "",
              partition_names: List[str] = [],
              expr: str = "",
              output_fields: List[str] = None,
              limit: int = -1,
              ignore_growing: bool = False,
              reduce_stop_for_best: bool = False,
              offset: int = 0,
              query_params: Dict[str, Any] = None,
              guarantee_timestamp: int = 0,
              not_return_all_meta: bool = False,
              consistency_level: CONSISTENCY_LEVEL = "bounded",
              use_default_consistency: bool = False,
              ) -> Union[SearchResults, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        _query_params = query_params or {}
        _query_params["reduce_stop_for_best"] = reduce_stop_for_best
        _query_params["ignore_growing"] = ignore_growing
        if offset > 0:
            _query_params["offset"] = offset
        if limit > 0:
            _query_params["limit"] = limit
        resp = self.stub.Query(QueryRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            partition_names=partition_names,
            expr=expr,
            output_fields=output_fields,
            query_params=[KeyValuePair(key=k, value=str(v) if isinstance(v, dict) else str(v)) for k, v in _query_params.items()],
            guarantee_timestamp=guarantee_timestamp,
            not_return_all_meta=not_return_all_meta,
            consistency_level=get_consistency_level(consistency_level),
            use_default_consistency=use_default_consistency,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def flush_all(self, *,
                  db_name: str = "",
                  ) -> Union[Status, str]:
        _db_name = db_name or self._db_name()
        resp = self.stub.Flush(FlushRequest(db_name=_db_name))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def get_flush_all_state(self, *,
                            db_name: str = "",
                            flush_all_ts: int = 0,
                            ) -> Union[GetFlushAllStateResponse, str]:
        _db_name = db_name or self._db_name()
        resp = self.stub.GetFlushAllState(GetFlushAllStateRequest(
            db_name=_db_name,
            flush_all_ts=flush_all_ts,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def create_partition(self, *,
                         db_name: str = "",
                         collection_name: str = "",
                         partition_name: str = "",
                         ) -> Union[Status, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        _partition_name = partition_name or self._partition_name()
        resp = self.stub.CreatePartition(CreatePartitionRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            partition_name=_partition_name,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def drop_partition(self, *,
                       db_name: str = "",
                       collection_name: str = "",
                       partition_name: str = "",
                       ) -> Union[Status, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        _partition_name = partition_name or self._partition_name()
        resp = self.stub.DropPartition(DropPartitionRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            partition_name=_partition_name,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    @deprecated("Use show_partitions instead")
    def has_partition(self, *,
                      db_name: str = "",
                      collection_name: str = "",
                      partition_name: str = "",
                      time_stamp: int = 0,
                      ) -> Union[BoolResponse, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        _partition_name = partition_name or self._partition_name()
        resp = self.stub.HasPartition(HasPartitionRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            partition_name=_partition_name,
            time_stamp=time_stamp,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def load_partitions(self, *,
                       db_name: str = "",
                       collection_name: str = "",
                       partition_names: List[str] = None,
                       replica_number: int = 1,
                       resource_groups: Optional[List[str]] = None,
                       refresh: bool = False,
                       ) -> Union[Status, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        _partition_names = [self._partition_name()] if len(partition_names) == 0 else partition_names
        resp = self.stub.LoadPartitions(LoadPartitionsRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            partition_names=_partition_names,
            replica_number=replica_number,
            resource_groups=resource_groups or [],
            refresh=refresh,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def release_partitions(self, *,
                          db_name: str = "",
                          collection_name: str = "",
                          partition_names: List[str] = None,
                          ) -> Union[Status, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        _partition_names = [self._partition_name()] if len(partition_names) == 0 else partition_names
        resp = self.stub.ReleasePartitions(ReleasePartitionsRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            partition_names=_partition_names,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def get_partition_statistics(self, *,
                                 db_name: str = "",
                                 collection_name: str = "",
                                 partition_name: str = "",
                                 ) -> Union[GetPartitionStatisticsResponse, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        _partition_name = partition_name or self._partition_name()
        resp = self.stub.GetPartitionStatistics(GetPartitionStatisticsRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            partition_name=_partition_name,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def show_partitions(self, *,
                        db_name: str = "",
                        collection_name: str = "",
                        collection_id: int = 0,
                        ) -> Union[ShowPartitionsResponse, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        resp = self.stub.ShowPartitions(ShowPartitionsRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            collectionID=collection_id,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def get_loading_progress(self, *,
                            db_name: str = "",
                            collection_name: str = "",
                            partition_names: Optional[List[str]] = None,
                            ) -> Union[GetLoadingProgressResponse, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        _partition_names = self._partition_names() if not partition_names else partition_names
        resp = self.stub.GetLoadingProgress(GetLoadingProgressRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            partition_names=_partition_names,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def get_load_state(self, *,
                       db_name: str = "",
                       collection_name: str = "",
                       partition_names: Optional[List[str]] = None,
                       ) -> Union[GetLoadStateResponse, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        _partition_names = self._partition_names() if not partition_names else partition_names
        resp = self.stub.GetLoadState(GetLoadStateRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            partition_names=_partition_names,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def create_alias(self, *,
                     db_name: str = "",
                     collection_name: str = "",
                     alias_name: str = "",
                     ) -> Union[Status, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        resp = self.stub.CreateAlias(CreateAliasRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            alias=alias_name,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def drop_alias(self, *,
                   db_name: str = "",
                   alias_name: str = "",
                   ) -> Union[Status, str]:
        _db_name = db_name or self._db_name()
        resp = self.stub.DropAlias(DropAliasRequest(
            db_name=_db_name,
            alias=alias_name,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def alter_alias(self, *,
                    db_name: str = "",
                    collection_name: str = "",
                    alias_name: str = "",
                    ) -> Union[Status, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        resp = self.stub.AlterAlias(AlterAliasRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            alias=alias_name,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def describe_alias(self, *,
                       db_name: str = "",
                       alias_name: str = "",
                       ) -> Union[DescribeAliasResponse, str]:
        _db_name = db_name or self._db_name()
        resp = self.stub.DescribeAlias(DescribeAliasRequest(
            db_name=_db_name,
            alias=alias_name,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def list_aliases(self, *,
                     db_name: str = "",
                     collection_name: str = "",
                     ) -> Union[ListAliasesResponse, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        resp = self.stub.ListAliases(ListAliasesRequest(
            db_name=_db_name,
            collection_name=_collection_name,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def create_index(self, *,
                     db_name: str = "",
                     collection_name: str = "",
                     field_name: str = "",
                     index_name: str = "",
                     index_type: INDEX_TYPE = "IVF_FLAT",
                     metric_type: METRIC_TYPE = "L2",
                     params: Optional[Dict[str, str]] = None,
                     nlist: int = 128,
                     ) -> Union[Status, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        params = params or {}
        params["nlist"] = nlist
        extra_params = {
            "index_type": index_type,
            "metric_type": metric_type,
            "params": json.dumps(params),
        }
        resp = self.stub.CreateIndex(CreateIndexRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            field_name=field_name,
            index_name=index_name,
            extra_params=[KeyValuePair(key=k, value=str(v)) for k, v in (extra_params or {}).items()],
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def alter_index(self, *,
                    db_name: str = "",
                    collection_name: str = "",
                    index_name: str = "",
                    params: Dict[str, str] = None,
                    ) -> Union[Status, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        resp = self.stub.AlterIndex(AlterIndexRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            index_name=index_name,
            extra_params=[KeyValuePair(key=k, value=str(v)) for k, v in (params or {}).items()],
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def describe_index(self, *,
                       db_name: str = "",
                       collection_name: str = "",
                       field_name: str = "",
                       index_name: str = "",
                       timestamp: int = 0,
                       ) -> Union[DescribeIndexResponse, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        resp = self.stub.DescribeIndex(DescribeIndexRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            index_name=index_name,
            field_name=field_name,
            timestamp=timestamp,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def get_index_statistics(self, *,
                             db_name: str = "",
                             collection_name: str = "",
                             index_name: str = "",
                             timestamp: int = 0,
                             ) -> Union[GetIndexStatisticsResponse, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        resp = self.stub.GetIndexStatistics(GetIndexStatisticsRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            index_name=index_name,
            timestamp=timestamp,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def drop_index(self, *,
                   db_name: str = "",
                   collection_name: str = "",
                   index_name: str = "",
                   ) -> Union[Status, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        resp = self.stub.DropIndex(DropIndexRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            index_name=index_name,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def get_persistent_segment_info(self, *,
                            db_name: str = "",
                            collection_name: str = "",
                            ) -> Union[GetPersistentSegmentInfoResponse, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        resp = self.stub.GetPersistentSegmentInfo(GetPersistentSegmentInfoRequest(
            dbName=_db_name,
            collectionName=_collection_name,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def get_query_segment_info(self, *,
                            db_name: str = "",
                            collection_name: str = "",
                            ) -> Union[GetQuerySegmentInfoResponse, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        resp = self.stub.GetQuerySegmentInfo(GetQuerySegmentInfoRequest(
            dbName=_db_name,
            collectionName=_collection_name,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def get_replicas(self, *,
                     db_name: str = "",
                     collection_name: str = "",
                     collection_id: int = 0,
                     with_shard_nodes: bool = False,
                     ) -> Union[GetReplicasResponse, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        resp = self.stub.GetReplica(GetReplicasRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            collectionID=collection_id,
            with_shard_nodes=with_shard_nodes,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def get_metric(self) -> Union[GetMetricsResponse, str]:
        resp = self.stub.GetMetrics(GetMetricsRequest(
            request="system_info",
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def get_component_states(self) -> Union[ComponentStates, str]:
        resp = self.stub.GetComponentStates(GetComponentStatesRequest())
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def load_banlance(self, *,
                      db_name: str = "",
                      collection_name: str = "",
                      src_node_id: int = 0,
                      dst_node_ids: List[int] = [],
                      segment_ids: List[int] = [],
                      ) -> Union[Status, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        resp = self.stub.LoadBalance(LoadBalanceRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            src_nodeID=src_node_id,
            dst_nodeIDs=dst_node_ids,
            sealed_segmentIDs=segment_ids,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def compaction(self, *,
                   collection_id: int = 0,
                   time_travel: int = 0,
                   ) -> Union[Status, str]:
        resp = self.stub.ManualCompaction(ManualCompactionRequest(
            collectionID=collection_id,
            timeTravel=time_travel,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def get_compaction_state(self, *,
                             compaction_id: int = 0,
                             ) -> Union[GetCompactionStateResponse, str]:
        resp = self.stub.GetCompactionState(GetCompactionStateRequest(
            compactionID=compaction_id,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def get_compaction_state_with_plans(self, *,
                                       compaction_id: int = 0,
                                       ) -> Union[GetCompactionPlansResponse, str]:
        resp = self.stub.GetCompactionStateWithPlans(GetCompactionPlansRequest(
            compactionID=compaction_id,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def bulk_insert(self, *,
                    db_name: str = "",
                    collection_name: str = "",
                    partition_name: str = "",
                    channel_names: List[str] = [],
                    row_base: bool = False,
                    files: List[str] = [],
                    options: Dict[str, str] = None,
                    scalar_fields: List[str] = [],
                    vector_fields: Dict[str, int] = {},
                    ) -> Union[MutationResult, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        _partition_name = partition_name or self._partition_name()
        c = ClusteringInfo(
            scalar_clustering_infos=[ScalarClusteringInfo(field=f) for f in scalar_fields],
            vector_clustering_infos=[VectorClusteringInfo(field=f, centroid=VectorField(dim=d)) for f, d in vector_fields.items()],
        )
        resp = self.stub.Import(ImportRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            partition_name=_partition_name,
            channel_names=channel_names,
            row_base=row_base,
            files=files,
            options=[KeyValuePair(key=k, value=v) for k, v in (options or {}).items()],
            clustering_info=ClusteringInfo.SerializeToString(c),
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def get_bulk_insert_state(self, *,
                              task_id: str = "",
                              ) -> Union[GetImportStateResponse, str]:
        resp = self.stub.GetImportState(GetImportStateRequest(
            task=task_id,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def list_bulk_insert_tasks(self, *,
                              db_name: str = "",
                              collection_name: str = "",
                              limit: int = 0,
                              ) -> Union[ListImportTasksResponse, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        resp = self.stub.ListImportTasks(ListImportTasksRequest(
            db_name=_db_name,
            collection_name=_collection_name,
            limit=limit,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def create_user(self, *,
                    username: str = "",
                    password: str = "",
                    ) -> Union[Status, str]:
        resp = self.stub.CreateCredential(CreateCredentialRequest(
            username=username,
            password=base64.b64encode(password.encode("utf-8")),
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def update_user(self, *,
                    username: str = "",
                    old_password: str = "",
                    new_password: str = "",
                    ) -> Union[Status, str]:
        resp = self.stub.UpdateCredential(UpdateCredentialRequest(
            username=username,
            oldPassword=base64.b64encode(old_password.encode("utf-8")),
            newPassword=base64.b64encode(new_password.encode("utf-8")),
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def delete_user(self, *,
                    username: str = "",
                    ) -> Union[Status, str]:
        resp = self.stub.DeleteCredential(DeleteCredentialRequest(
            username=username,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def list_users(self) -> Union[ListCredUsersResponse, str]:
        resp = self.stub.ListCredentials(ListCredUsersRequest())
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def create_role(self, *,
                    role_name: str = "",
                    ) -> Union[Status, str]:
        resp = self.stub.CreateRole(CreateRoleRequest(
            entity=RoleEntity(name=role_name),
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def drop_role(self, *,
                    role_name: str = "",
                    ) -> Union[Status, str]:
        resp = self.stub.DropRole(DropRoleRequest(
            role_name=role_name,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def operate_user_role(self, *,
                          username: str = "",
                          role_name: str = "",
                          action: Union[str, Literal[
                              "add_user_to_role",
                              "remove_user_from_role",
                              ]] = "add_user_to_role",
                          ) -> Union[Status, str]:
        if action not in ["add_user_to_role", "remove_user_from_role"]:
            raise ValueError(f"Invalid action: {action}")
        resp = self.stub.OperateUserRole(OperateUserRoleRequest(
            username=username,
            role_name=role_name,
            type=OperateUserRoleType.AddUserToRole if action == "add_user_to_role" else OperateUserRoleType.RemoveUserFromRole,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def select_user(self, *,
                    username: str = "",
                    include_role_info: bool = False,
                    ) -> Union[SelectUserResponse, str]:
        resp = self.stub.SelectUser(SelectUserRequest(
            user=UserEntity(name=username) if username else None,
            include_role_info=include_role_info,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def select_role(self, *,
                    role_name: str = "",
                    include_user_info: bool = False,
                    ) -> Union[SelectRoleResponse, str]:
        resp = self.stub.SelectRole(SelectRoleRequest(
            role=RoleEntity(name=role_name) if role_name else None,
            include_user_info=include_user_info,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def operate_privilege(self, *,
                          db_name: str = "",
                          role_name: str = "",
                          object_type: Union[str, Literal[
                              "collection",
                              "global",
                              "user",
                              ]] = "collection",
                          object_name: str = "",
                          privilege: Union[COLLECTION_PRIVILEGE,
                                           GLOBAL_PRIVILEGE,
                                           USER_PRIVILEGE] = "DescribeCollection",
                          action: Union[str, Literal[
                              "grant",
                              "revoke",
                              ]] = "grant",
                          ) -> Union[Status, str]:
        if action not in ["grant", "revoke"]:
            raise ValueError(f"Invalid action: {action}")
        if not privilege:
            raise ValueError("Privilege is required, more details: https://milvus.io/docs/users_and_roles.md#Users-and-Roles")
        _db_name = db_name or self._db_name()
        resp = self.stub.OperatePrivilege(OperatePrivilegeRequest(
            entity=GrantEntity(
                db_name=_db_name,
                role=RoleEntity(name=role_name),
                object=ObjectEntity(name=object_type.capitalize()),
                object_name=object_name,
                grantor=GrantorEntity(
                    privilege=PrivilegeEntity(name=privilege),
                    ),
                ),
            type=OperatePrivilegeType.Grant if action == "grant" else OperatePrivilegeType.Revoke,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def select_grant(self, *,
                     db_name: str = "",
                     role_name: str = "",
                     object_type: Union[str, Literal[
                         "collection",
                         "global",
                         "user",
                         ]] = "collection",
                     object_name: str = "",
                     privilege: Union[COLLECTION_PRIVILEGE,
                                     GLOBAL_PRIVILEGE,
                                     USER_PRIVILEGE] = "",
                     ) -> Union[SelectGrantResponse, str]:
        _db_name = db_name or self._db_name()
        resp = self.stub.SelectGrant(SelectGrantRequest(
            entity=GrantEntity(
                db_name=_db_name,
                role=RoleEntity(name=role_name) if role_name else None,
                object=ObjectEntity(name=object_type) if object_type else None,
                object_name=object_name if object_name else None,
                grantor=GrantorEntity(
                    privilege=PrivilegeEntity(name=privilege),
                    ) if privilege else None,
                ),
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def get_version(self) -> Union[GetVersionResponse, str]:
        resp = self.stub.GetVersion(GetVersionRequest())
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def check_health(self) -> Union[CheckHealthResponse, str]:
        resp = self.stub.CheckHealth(CheckHealthRequest())
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def create_resource_group(self, *,
                              name: str = "",
                              ) -> Union[Status, str]:
        resp = self.stub.CreateResourceGroup(CreateResourceGroupRequest(
            resource_group=name,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def drop_resource_group(self, *,
                            name: str = "",
                            ) -> Union[Status, str]:
        resp = self.stub.DropResourceGroup(DropResourceGroupRequest(
            resource_group=name,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def transfer_node(self, *,
                      source_resource_group: str = "",
                      dst_resource_group: str = "",
                      num_node: int = 0,
                      ) -> Union[Status, str]:
        resp = self.stub.TransferNode(TransferNodeRequest(
            source_resource_group=source_resource_group,
            dst_resource_group=dst_resource_group,
            num_node=num_node,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def transfer_replica(self, *,
                         db_name: str = "",
                         collection_name: str = "",
                         source_resource_group: str = "",
                         dst_resource_group: str = "",
                         num_replica: int = 0,
                         ) -> Union[Status, str]:
        _db_name = db_name or self._db_name()
        _collection_name = collection_name or self._collection_name()
        resp = self.stub.TransferReplica(TransferReplicaRequest(
            source_resource_group=source_resource_group,
            dst_resource_group=dst_resource_group,
            num_replica=num_replica,
            db_name=_db_name,
            collection_name=_collection_name,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def list_resource_groups(self) -> Union[ListResourceGroupsResponse, str]:
        resp = self.stub.ListResourceGroups(ListResourceGroupsRequest())
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def describe_resource_group(self, *,
                                resource_group: str = "",
                                ) -> Union[DescribeResourceGroupResponse, str]:
        resp = self.stub.DescribeResourceGroup(DescribeResourceGroupRequest(
            resource_group=resource_group,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def rename_collection(self, *,
                          db_name: str = "",
                          new_db_name: str = "",
                          old_collection_name: str = "",
                          new_collection_name: str = "",
                          ) -> Union[Status, str]:
        _db_name = db_name or self._db_name()
        resp = self.stub.RenameCollection(RenameCollectionRequest(
            db_name=_db_name,
            newDBName=new_db_name,
            oldName=old_collection_name,
            newName=new_collection_name,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def list_indexed_segment(self, *,
                              collection_name: str = "",
                              index_name: str = "",
                              ) -> Union[ListIndexedSegmentResponse, str]:
        _collection_name = collection_name or self._collection_name()
        resp = self.stub.ListIndexedSegment(ListIndexedSegmentRequest(
            collection_name=_collection_name,
            index_name=index_name,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def describe_segment_index_data(self, *,
                                    collection_name: str = "",
                                    index_name: str = "",
                                    segment_ids: List[int] = [],
                                    ) -> Union[DescribeSegmentIndexDataResponse, str]:
        _collection_name = collection_name or self._collection_name()
        resp = self.stub.DescribeSegmentIndexData(DescribeSegmentIndexDataRequest(
            collection_name=_collection_name,
            index_name=index_name,
            segmentsIDs=segment_ids,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    # TODO it need to more information
    def connect(self) -> Union[ConnectResponse, str]:
        now = datetime.datetime.now()
        resp = self.stub.Connect(ConnectRequest(
            client_info=ClientInfo(
                sdk_type="python",
                sdk_version=f"connector-{VERSION}",
                local_time=str(now),
                ),
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def alloc_timestamp(self) -> Union[AllocTimestampResponse, str]:
        resp = self.stub.AllocTimestamp(AllocTimestampRequest())
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def create_database(self, *,
                        db_name: str = "",
                        ) -> Union[Status, str]:
        _db_name = db_name or self._db_name()
        resp = self.stub.CreateDatabase(CreateDatabaseRequest(
            db_name=_db_name,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def drop_database(self, *,
                      db_name: str = "",
                      ) -> Union[Status, str]:
        _db_name = db_name or self._db_name()
        resp = self.stub.DropDatabase(DropDatabaseRequest(
            db_name=_db_name,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def list_databases(self) -> Union[ListDatabasesResponse, str]:
        resp = self.stub.ListDatabases(ListDatabasesRequest())
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp

    def replicate_message(self, *,
                          channel_name: str = "",
                          ) -> Union[ReplicateMessageResponse, str]:
        resp = self.stub.ReplicateMessage(ReplicateMessageRequest(
            channel_name=channel_name,
        ))
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToJson(resp)
        return resp