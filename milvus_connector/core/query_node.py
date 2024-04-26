import copy
import json
from typing import Any, Optional, Union, Literal, List
from typing_extensions import Self

import grpc
from google.protobuf import json_format
from furl import furl

from ..protocol.query_coord_pb2_grpc import QueryNodeStub
from ..protocol.query_coord_pb2 import *
from ..protocol.internal_pb2 import *
from ..protocol.milvus_pb2 import *
from ..protocol.common_pb2 import *
from ..protocol.schema_pb2 import *
from ..protocol.feder_pb2 import *
from ._const import *
from ._types import *


class QueryNode():
    stub: QueryNodeStub
    style: str

    def __init__(self, *,
                 uri: str = "localhost:21123",
                 response_style: Union[str, Literal[
                     "json",
                     "object",
                     ]] = "object",
                 query_node: Optional[Self] = None,
                 ) -> None:
        if query_node:
            self.stub = query_node.stub
            self.style = query_node.style
            return
        self.style = response_style.lower()
        if not uri.startswith("http"):
            uri = "http://" + uri
        _secure = uri.startswith("https://")

        _netloc = furl(uri).netloc
        if _secure:
            creds = grpc.ssl_channel_credentials()
            _channel = grpc.secure_channel(_netloc, creds)
        else:
            _channel = grpc.insecure_channel(_netloc)

        self.stub = QueryNodeStub(_channel)
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
        m = QueryNode(query_node=self)
        m.style = "json"
        return m

    def get_data_distribution(self) -> Union[GetDataDistributionResponse, str]:
        req = GetDataDistributionRequest()
        resp = self.stub.GetDataDistribution(req)
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToDict(resp)
        return resp

    def get_metric(self, metric_type: str = "system_info") -> Union[GetMetricsResponse, str]:
        req = GetMetricsRequest(request=json.dumps({"metric_type": metric_type}))
        resp = self.stub.GetMetrics(req)
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToDict(resp)
        return resp

    def show_configs(self, pattern: str = "") -> Union[ShowConfigurationsResponse, str]:
        req = ShowConfigurationsRequest(pattern=pattern)
        resp = self.stub.ShowConfigurations(req)
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToDict(resp)
        return resp

    def get_segment_info(self, collection_id: int = 0, segment_ids: List[int] = None) -> Union[GetSegmentInfoResponse, str]:
        req = GetSegmentInfoRequest(collectionID=collection_id, segmentIDs=segment_ids)
        resp = self.stub.GetSegmentInfo(req)
        self._intercept_resp(resp)
        if self._is_json():
            return json_format.MessageToDict(resp)
        return resp
