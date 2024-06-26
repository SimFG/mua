"""Copy from the pymilvus."""

from typing import Any, Callable, List, NamedTuple

import grpc


class _GenericClientInterceptor(
    grpc.UnaryUnaryClientInterceptor,
    grpc.UnaryStreamClientInterceptor,
    grpc.StreamUnaryClientInterceptor,
    grpc.StreamStreamClientInterceptor,
):
    def __init__(self, interceptor_function: Callable) -> None:
        super().__init__()
        self._fn = interceptor_function

    def intercept_unary_unary(self, continuation: Callable, client_call_details: Any, request: Any):
        new_details, new_request_iterator, postprocess = self._fn(
            client_call_details, iter((request,))
        )
        response = continuation(new_details, next(new_request_iterator))
        return postprocess(response) if postprocess else response

    def intercept_unary_stream(
        self,
        continuation: Callable,
        client_call_details: Any,
        request: Any,
    ):
        new_details, new_request_iterator, postprocess = self._fn(
            client_call_details, iter((request,))
        )
        response_it = continuation(new_details, next(new_request_iterator))
        return postprocess(response_it) if postprocess else response_it

    def intercept_stream_unary(
        self,
        continuation: Callable,
        client_call_details: Any,
        request_iterator: Any,
    ):
        new_details, new_request_iterator, postprocess = self._fn(
            client_call_details, request_iterator
        )
        response = continuation(new_details, new_request_iterator)
        return postprocess(response) if postprocess else response

    def intercept_stream_stream(
        self,
        continuation: Callable,
        client_call_details: Any,
        request_iterator: Any,
    ):
        new_details, new_request_iterator, postprocess = self._fn(
            client_call_details, request_iterator
        )
        response_it = continuation(new_details, new_request_iterator)
        return postprocess(response_it) if postprocess else response_it


class ClientCallDetailsTuple(NamedTuple):
    method: Any
    timeout: Any
    metadata: Any
    credentials: Any


class _ClientCallDetails(ClientCallDetailsTuple, grpc.ClientCallDetails):
    pass


def header_adder_interceptor(headers: List, values: List):
    def intercept_call(
        client_call_details: Any,
        request_iterator: Any,
    ):
        metadata = []
        if client_call_details.metadata is not None:
            metadata = list(client_call_details.metadata)
        for item in zip(headers, values):
            metadata.append(item)
        client_call_details = _ClientCallDetails(
            client_call_details.method,
            client_call_details.timeout,
            metadata,
            client_call_details.credentials,
        )
        return client_call_details, request_iterator, None

    return _GenericClientInterceptor(intercept_call)
