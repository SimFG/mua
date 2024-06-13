from functools import wraps
import random
import sys
from typing import Any, Dict, List, Union
from abc import ABCMeta, abstractmethod

import grpc

from ._types import *
from ..protocol.schema_pb2 import *
from ..protocol.common_pb2 import *

class CollectionField:
    obj: FieldSchema

    def __init__(self, *,
                 name: str,
                 is_primary_key: bool = False,
                 dtype: DTYPE = "int64",
                 desc: str = "",
                 dim: int = 0,
                 max_length: int = 0,
                 type_params: Union[None, Dict[str, str]] = None,
                 auto_id: bool = False,
                 is_dynamic: bool = False,
                 is_partition_key: bool = False,
                 is_cluster_key: bool = False,
                 ):
        if dtype in ("binary_vector", "float_vector", "float16_vector", "bfloat16_vector", "sparse_vector") and dim == 0:
            raise ValueError(f"Dimension should be specified for {dtype} field")
        if dtype in ("string", "varchar") and max_length == 0:
            raise ValueError(f"Max length should be specified for {dtype} field")
        type_params = type_params or {}
        if dim > 0:
            type_params["dim"] = str(dim)
        if max_length > 0:
            type_params["max_length"] = str(max_length)
        self.obj = FieldSchema(
            name=name,
            is_primary_key=is_primary_key,
            data_type=get_data_type(dtype),
            description=desc,
            type_params=[KeyValuePair(key=k, value=v) for k, v in (type_params or {}).items()],
            autoID=auto_id,
            is_dynamic=is_dynamic,
            is_partition_key=is_partition_key,
            is_clustering_key=is_cluster_key,
        )

class Data(metaclass=ABCMeta):
    dtype: DataType
    field_name: str
    is_dynamic: bool

    def __init__(self, field_name: str, dtype: DTYPE, is_dynamic: bool = False):
        self.field_name = field_name
        self.is_dynamic = is_dynamic
        self.dtype = get_data_type(dtype)

    @abstractmethod
    def construct_data(self)-> FieldData:
        pass

class VectorData(Data):
    pass

class FloatVectorData(VectorData):
    data: List[List[float]]

    def __init__(self, *,
                 field_name: str,
                 dtype: str,
                 data: List[List[float]],
                 is_dynamic: bool = False):
        if dtype not in ("float_vector", "floatvector"):
            raise ValueError(f"the expect: float_vector, current: {dtype}")
        super().__init__(field_name, dtype, is_dynamic)
        self.data = data

    def construct_data(self) -> FieldData:
        dim = len(self.data[0])
        b :List[float] = []
        for d in self.data:
            b.extend(d)
        return FieldData(
            type=self.dtype,
            field_name=self.field_name,
            vectors=VectorField(
                dim=dim,
                float_vector=FloatArray(data=b),
                ),
            is_dynamic=self.is_dynamic,
        )

class ByteVectorData(VectorData):
    data: List[bytes]
    def __init__(self, *,
                 field_name: str,
                 dtype: str,
                 data: List[bytes],
                 is_dynamic: bool = False):
        if dtype not in ("binary_vector", "float16_vector", "bfloat16_vector"):
            raise ValueError(f"the expect: binary_vector, float16_vector, bfloat16_vector, current: {dtype}")
        super().__init__(field_name, dtype, is_dynamic)
        self.data = data

    def construct_data(self) -> FieldData:
        b :bytes = []
        for d in self.data:
            b.extend(d)

        match self.dtype:
            case "binary_vector":
                return FieldData(
                    type=self.dtype,
                    field_name=self.field_name,
                    vectors=VectorField(
                        dim=len(self.data[0]) * 8,
                        binary_vector=b,
                        ),
                    is_dynamic=self.is_dynamic,
                )
            case "float16_vector":
                return FieldData(
                    type=self.dtype,
                    field_name=self.field_name,
                    vectors=VectorField(
                        dim=len(self.data[0]) // 2,
                        float16_vector=b,
                        ),
                    is_dynamic=self.is_dynamic,
                )
            case "bfloat16_vector":
                return FieldData(
                    type=self.dtype,
                    field_name=self.field_name,
                    vectors=VectorField(
                        dim=len(self.data[0]) // 2,
                        bfloat16_vector=b,
                        ),
                    is_dynamic=self.is_dynamic,
                )
            case (_):
                raise ValueError(f"Invalid data type: {self.dtype}")

class ScalarData(Data):
    pass

class BoolData(ScalarData):
    data: List[bool]

    def __init__(self, *,
                 field_name: str,
                 dtype: str,
                 data: List[bool],
                 is_dynamic: bool = False):
        if dtype not in ("bool"):
            raise ValueError(f"the expect: bool, current: {dtype}")
        super().__init__(field_name, dtype, is_dynamic)
        self.data = data

    def construct_data(self) -> FieldData:
        return FieldData(
            type=self.dtype,
            field_name=self.field_name,
            scalars=ScalarField(
                bool_data=BoolArray(data=self.data),
                ),
            is_dynamic=self.is_dynamic,
        )

class IntData(ScalarData):
    data: List[int]

    def __init__(self, *,
                 field_name: str,
                 dtype: str,
                 data: List[int],
                 is_dynamic: bool = False):
        if dtype not in ("int8", "int16", "int32"):
            raise ValueError(f"the expect: int8, int16, int32, current: {dtype}")
        super().__init__(field_name, dtype, is_dynamic)
        self.data = data

    def construct_data(self) -> FieldData:
        return FieldData(
            type=self.dtype,
            field_name=self.field_name,
            scalars=ScalarField(
                int_data=IntArray(data=self.data),
                ),
            is_dynamic=self.is_dynamic,
        )

class LongData(ScalarData):
    data: List[int]

    def __init__(self, *,
                 field_name: str,
                 dtype: str,
                 data: List[int],
                 is_dynamic: bool = False):
        if dtype not in ("int64"):
            raise ValueError(f"the expect: int64, current: {dtype}")
        super().__init__(field_name, dtype, is_dynamic)
        self.data = data

    def construct_data(self) -> FieldData:
        return FieldData(
            type=self.dtype,
            field_name=self.field_name,
            scalars=ScalarField(
                long_data=LongArray(data=self.data),
                ),
            is_dynamic=self.is_dynamic,
        )

class FloatData(ScalarData):
    data: List[float]

    def __init__(self, *,
                 field_name: str,
                 dtype: str,
                 data: List[float],
                 is_dynamic: bool = False):
        if dtype not in ("float"):
            raise ValueError(f"the expect: float, current: {dtype}")
        super().__init__(field_name, dtype, is_dynamic)
        self.data = data

    def construct_data(self) -> FieldData:
        return FieldData(
            type=self.dtype,
            field_name=self.field_name,
            scalars=ScalarField(
                float_data=FloatArray(data=self.data),
                ),
            is_dynamic=self.is_dynamic,
        )

class DoubleData(ScalarData):
    data: List[float]

    def __init__(self, *,
                 field_name: str,
                 dtype: str,
                 data: List[float],
                 is_dynamic: bool = False):
        if dtype not in ("double"):
            raise ValueError(f"the expect: double, current: {dtype}")
        super().__init__(field_name, dtype, is_dynamic)
        self.data = data

    def construct_data(self) -> FieldData:
        return FieldData(
            type=self.dtype,
            field_name=self.field_name,
            scalars=ScalarField(
                double_data=DoubleArray(data=self.data),
                ),
            is_dynamic=self.is_dynamic,
        )

class StringData(ScalarData):
    data: List[str]

    def __init__(self, *,
                 field_name: str,
                 dtype: str,
                 data: List[str],
                 is_dynamic: bool = False):
        if dtype not in ("string", "varchar"):
            raise ValueError(f"the expect: string, varchar, current: {dtype}")
        super().__init__(field_name, dtype, is_dynamic)
        self.data = data

    def construct_data(self) -> FieldData:
        return FieldData(
            type=self.dtype,
            field_name=self.field_name,
            scalars=ScalarField(
                string_data=StringArray(data=self.data),
                ),
            is_dynamic=self.is_dynamic,
        )

class JSONData(ScalarData):
    data: List[str]

    def __init__(self, *,
                 field_name: str,
                 dtype: str,
                 data: List[str],
                 is_dynamic: bool = False):
        if dtype not in ("json"):
            raise ValueError(f"the expect: json, current: {dtype}")
        super().__init__(field_name, dtype, is_dynamic)
        self.data = data

    def construct_data(self) -> FieldData:
        return FieldData(
            type=self.dtype,
            field_name=self.field_name,
            scalars=ScalarField(
                json_data=JSONArray(data=[bytes(d, "utf-8") for d in self.data]),
                ),
            is_dynamic=self.is_dynamic,
        )

class ArrayData(ScalarData):
    data: List[ScalarData]

    def __init__(self, *,
                 field_name: str,
                 dtype: str,
                 element_type: str,
                 data: List[ScalarData],
                 is_dynamic: bool = False):
        if dtype not in ("array"):
            raise ValueError(f"the expect: array, current: {dtype}")
        super().__init__(field_name, dtype, is_dynamic)
        self.data = data

    def construct_data(self) -> FieldData:
        return FieldData(
            type=self.dtype,
            field_name=self.field_name,
            scalars=ScalarField(
                array_data=ArrayArray(
                    element_type=get_data_type(self.element_type),
                    data=self.data,
                    ),
                ),
            is_dynamic=self.is_dynamic,
        )

def ok(s: Status) -> bool:
    return s.code == 0 and s.error_code == Success

def grpc_error_handler(func):
    """
    Decorator to handle gRPC errors.
    
    This decorator will capture any gRPC errors that occur within the decorated function
    and print the error message, then exit the program.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except grpc.RpcError as e:
            if isinstance(e, grpc.Call):
                print(f"gRPC error code: {e.code()}")
                print(f"gRPC error message: {e.details()}")
            else:
                print(f"gRPC error occurred: {e}")
            sys.exit(1)
    return wrapper

def construct_data(field_name: str, data_type: DataType, data: List) -> Data:
    dtype_str = DataType.Name(data_type).lower()
    match data_type:
        case DataType.Bool:
            return BoolData(field_name=field_name,
                            dtype=dtype_str,
                            data=data)
        case DataType.Int8 | DataType.Int16 | DataType.Int32:
            return IntData(field_name=field_name,
                            dtype=dtype_str,
                            data=data)
        case DataType.Int64:
            return LongData(field_name=field_name,
                            dtype=dtype_str,
                            data=data)
        case DataType.Float:
            return FloatData(field_name=field_name,
                                dtype=dtype_str,
                                data=data)
        case DataType.Double:
            return DoubleData(field_name=field_name,
                                dtype=dtype_str,
                                data=data)
        case DataType.String | DataType.VarChar:
            return StringData(field_name=field_name,
                                dtype=dtype_str,
                                data=data)
        case DataType.FloatVector:
            return FloatVectorData(field_name=field_name,
                                dtype=dtype_str,
                                data=data)
        case (_):
            raise ValueError(f"Invalid data type: {data_type}")

def generate_random_data(row_num: int, field_name: str, data_type: DataType, dim: int = 0) -> Data:
    dtype_str = DataType.Name(data_type).lower()
    match data_type:
        case DataType.Bool:
            return BoolData(field_name=field_name,
                            dtype=dtype_str,
                            data=[random.choice([True, False]) for _ in range(row_num)])
        case DataType.Int8 | DataType.Int16 | DataType.Int32:
            return IntData(field_name=field_name,
                           dtype=dtype_str,
                           data=[random.randint(-128, 127) for _ in range(row_num)])
        case DataType.Int64:
            return LongData(field_name=field_name,
                            dtype=dtype_str,
                            data=[random.randint(-2048, 2048) for _ in range(row_num)])
        case DataType.Float:
            return FloatData(field_name=field_name,
                             dtype=dtype_str,
                             data=[random.random() for _ in range(row_num)])
        case DataType.Double:
            return DoubleData(field_name=field_name,
                              dtype=dtype_str,
                              data=[random.random() for _ in range(row_num)])
        case DataType.String | DataType.VarChar:
            return StringData(field_name=field_name,
                              dtype=dtype_str,
                              data=[str(random.randint(0, 1000)) for _ in range(row_num)])
        case DataType.FloatVector:
            if dim <= 0:
                raise ValueError("Dimension should be specified for float_vector field")
            return FloatVectorData(field_name=field_name,
                                   dtype=dtype_str,
                                   data=[[random.random() for _ in range(dim)] for _ in range(row_num)])
        case (_):
            raise ValueError(f"Random generation, not support data type: {dtype_str}")

def convert_data(data_type: DataType, data_str: str) -> Any:
    match data_type:
        case DataType.Bool:
            return bool(data_str)
        case DataType.Int8 | DataType.Int16 | DataType.Int32 | DataType.Int64:
            return int(data_str)
        case DataType.Float | DataType.Double:
            return float(data_str)
        case DataType.String | DataType.VarChar:
            return data_str
        case DataType.FloatVector:
            return [[float(d) for d in data_str.split(",")]]
        case (_):
            raise ValueError(f"Invalid data type: {data_type}")