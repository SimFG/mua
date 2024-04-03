from . import schema_pb2 as _schema_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OpType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Invalid: _ClassVar[OpType]
    GreaterThan: _ClassVar[OpType]
    GreaterEqual: _ClassVar[OpType]
    LessThan: _ClassVar[OpType]
    LessEqual: _ClassVar[OpType]
    Equal: _ClassVar[OpType]
    NotEqual: _ClassVar[OpType]
    PrefixMatch: _ClassVar[OpType]
    PostfixMatch: _ClassVar[OpType]
    Match: _ClassVar[OpType]
    Range: _ClassVar[OpType]
    In: _ClassVar[OpType]
    NotIn: _ClassVar[OpType]

class ArithOpType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Unknown: _ClassVar[ArithOpType]
    Add: _ClassVar[ArithOpType]
    Sub: _ClassVar[ArithOpType]
    Mul: _ClassVar[ArithOpType]
    Div: _ClassVar[ArithOpType]
    Mod: _ClassVar[ArithOpType]
    ArrayLength: _ClassVar[ArithOpType]

class VectorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BinaryVector: _ClassVar[VectorType]
    FloatVector: _ClassVar[VectorType]
    Float16Vector: _ClassVar[VectorType]
    BFloat16Vector: _ClassVar[VectorType]
    SparseFloatVector: _ClassVar[VectorType]
Invalid: OpType
GreaterThan: OpType
GreaterEqual: OpType
LessThan: OpType
LessEqual: OpType
Equal: OpType
NotEqual: OpType
PrefixMatch: OpType
PostfixMatch: OpType
Match: OpType
Range: OpType
In: OpType
NotIn: OpType
Unknown: ArithOpType
Add: ArithOpType
Sub: ArithOpType
Mul: ArithOpType
Div: ArithOpType
Mod: ArithOpType
ArrayLength: ArithOpType
BinaryVector: VectorType
FloatVector: VectorType
Float16Vector: VectorType
BFloat16Vector: VectorType
SparseFloatVector: VectorType

class GenericValue(_message.Message):
    __slots__ = ("bool_val", "int64_val", "float_val", "string_val", "array_val")
    BOOL_VAL_FIELD_NUMBER: _ClassVar[int]
    INT64_VAL_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VAL_FIELD_NUMBER: _ClassVar[int]
    STRING_VAL_FIELD_NUMBER: _ClassVar[int]
    ARRAY_VAL_FIELD_NUMBER: _ClassVar[int]
    bool_val: bool
    int64_val: int
    float_val: float
    string_val: str
    array_val: Array
    def __init__(self, bool_val: bool = ..., int64_val: _Optional[int] = ..., float_val: _Optional[float] = ..., string_val: _Optional[str] = ..., array_val: _Optional[_Union[Array, _Mapping]] = ...) -> None: ...

class Array(_message.Message):
    __slots__ = ("array", "same_type", "element_type")
    ARRAY_FIELD_NUMBER: _ClassVar[int]
    SAME_TYPE_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    array: _containers.RepeatedCompositeFieldContainer[GenericValue]
    same_type: bool
    element_type: _schema_pb2.DataType
    def __init__(self, array: _Optional[_Iterable[_Union[GenericValue, _Mapping]]] = ..., same_type: bool = ..., element_type: _Optional[_Union[_schema_pb2.DataType, str]] = ...) -> None: ...

class QueryInfo(_message.Message):
    __slots__ = ("topk", "metric_type", "search_params", "round_decimal", "group_by_field_id")
    TOPK_FIELD_NUMBER: _ClassVar[int]
    METRIC_TYPE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_PARAMS_FIELD_NUMBER: _ClassVar[int]
    ROUND_DECIMAL_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_ID_FIELD_NUMBER: _ClassVar[int]
    topk: int
    metric_type: str
    search_params: str
    round_decimal: int
    group_by_field_id: int
    def __init__(self, topk: _Optional[int] = ..., metric_type: _Optional[str] = ..., search_params: _Optional[str] = ..., round_decimal: _Optional[int] = ..., group_by_field_id: _Optional[int] = ...) -> None: ...

class ColumnInfo(_message.Message):
    __slots__ = ("field_id", "data_type", "is_primary_key", "is_autoID", "nested_path", "is_partition_key", "element_type")
    FIELD_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
    IS_AUTOID_FIELD_NUMBER: _ClassVar[int]
    NESTED_PATH_FIELD_NUMBER: _ClassVar[int]
    IS_PARTITION_KEY_FIELD_NUMBER: _ClassVar[int]
    ELEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    field_id: int
    data_type: _schema_pb2.DataType
    is_primary_key: bool
    is_autoID: bool
    nested_path: _containers.RepeatedScalarFieldContainer[str]
    is_partition_key: bool
    element_type: _schema_pb2.DataType
    def __init__(self, field_id: _Optional[int] = ..., data_type: _Optional[_Union[_schema_pb2.DataType, str]] = ..., is_primary_key: bool = ..., is_autoID: bool = ..., nested_path: _Optional[_Iterable[str]] = ..., is_partition_key: bool = ..., element_type: _Optional[_Union[_schema_pb2.DataType, str]] = ...) -> None: ...

class ColumnExpr(_message.Message):
    __slots__ = ("info",)
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: ColumnInfo
    def __init__(self, info: _Optional[_Union[ColumnInfo, _Mapping]] = ...) -> None: ...

class ExistsExpr(_message.Message):
    __slots__ = ("info",)
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: ColumnInfo
    def __init__(self, info: _Optional[_Union[ColumnInfo, _Mapping]] = ...) -> None: ...

class ValueExpr(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: GenericValue
    def __init__(self, value: _Optional[_Union[GenericValue, _Mapping]] = ...) -> None: ...

class UnaryRangeExpr(_message.Message):
    __slots__ = ("column_info", "op", "value")
    COLUMN_INFO_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    column_info: ColumnInfo
    op: OpType
    value: GenericValue
    def __init__(self, column_info: _Optional[_Union[ColumnInfo, _Mapping]] = ..., op: _Optional[_Union[OpType, str]] = ..., value: _Optional[_Union[GenericValue, _Mapping]] = ...) -> None: ...

class BinaryRangeExpr(_message.Message):
    __slots__ = ("column_info", "lower_inclusive", "upper_inclusive", "lower_value", "upper_value")
    COLUMN_INFO_FIELD_NUMBER: _ClassVar[int]
    LOWER_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    UPPER_INCLUSIVE_FIELD_NUMBER: _ClassVar[int]
    LOWER_VALUE_FIELD_NUMBER: _ClassVar[int]
    UPPER_VALUE_FIELD_NUMBER: _ClassVar[int]
    column_info: ColumnInfo
    lower_inclusive: bool
    upper_inclusive: bool
    lower_value: GenericValue
    upper_value: GenericValue
    def __init__(self, column_info: _Optional[_Union[ColumnInfo, _Mapping]] = ..., lower_inclusive: bool = ..., upper_inclusive: bool = ..., lower_value: _Optional[_Union[GenericValue, _Mapping]] = ..., upper_value: _Optional[_Union[GenericValue, _Mapping]] = ...) -> None: ...

class CompareExpr(_message.Message):
    __slots__ = ("left_column_info", "right_column_info", "op")
    LEFT_COLUMN_INFO_FIELD_NUMBER: _ClassVar[int]
    RIGHT_COLUMN_INFO_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    left_column_info: ColumnInfo
    right_column_info: ColumnInfo
    op: OpType
    def __init__(self, left_column_info: _Optional[_Union[ColumnInfo, _Mapping]] = ..., right_column_info: _Optional[_Union[ColumnInfo, _Mapping]] = ..., op: _Optional[_Union[OpType, str]] = ...) -> None: ...

class TermExpr(_message.Message):
    __slots__ = ("column_info", "values", "is_in_field")
    COLUMN_INFO_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    IS_IN_FIELD_FIELD_NUMBER: _ClassVar[int]
    column_info: ColumnInfo
    values: _containers.RepeatedCompositeFieldContainer[GenericValue]
    is_in_field: bool
    def __init__(self, column_info: _Optional[_Union[ColumnInfo, _Mapping]] = ..., values: _Optional[_Iterable[_Union[GenericValue, _Mapping]]] = ..., is_in_field: bool = ...) -> None: ...

class JSONContainsExpr(_message.Message):
    __slots__ = ("column_info", "elements", "op", "elements_same_type")
    class JSONOp(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Invalid: _ClassVar[JSONContainsExpr.JSONOp]
        Contains: _ClassVar[JSONContainsExpr.JSONOp]
        ContainsAll: _ClassVar[JSONContainsExpr.JSONOp]
        ContainsAny: _ClassVar[JSONContainsExpr.JSONOp]
    Invalid: JSONContainsExpr.JSONOp
    Contains: JSONContainsExpr.JSONOp
    ContainsAll: JSONContainsExpr.JSONOp
    ContainsAny: JSONContainsExpr.JSONOp
    COLUMN_INFO_FIELD_NUMBER: _ClassVar[int]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    ELEMENTS_SAME_TYPE_FIELD_NUMBER: _ClassVar[int]
    column_info: ColumnInfo
    elements: _containers.RepeatedCompositeFieldContainer[GenericValue]
    op: JSONContainsExpr.JSONOp
    elements_same_type: bool
    def __init__(self, column_info: _Optional[_Union[ColumnInfo, _Mapping]] = ..., elements: _Optional[_Iterable[_Union[GenericValue, _Mapping]]] = ..., op: _Optional[_Union[JSONContainsExpr.JSONOp, str]] = ..., elements_same_type: bool = ...) -> None: ...

class UnaryExpr(_message.Message):
    __slots__ = ("op", "child")
    class UnaryOp(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Invalid: _ClassVar[UnaryExpr.UnaryOp]
        Not: _ClassVar[UnaryExpr.UnaryOp]
    Invalid: UnaryExpr.UnaryOp
    Not: UnaryExpr.UnaryOp
    OP_FIELD_NUMBER: _ClassVar[int]
    CHILD_FIELD_NUMBER: _ClassVar[int]
    op: UnaryExpr.UnaryOp
    child: Expr
    def __init__(self, op: _Optional[_Union[UnaryExpr.UnaryOp, str]] = ..., child: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...

class BinaryExpr(_message.Message):
    __slots__ = ("op", "left", "right")
    class BinaryOp(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Invalid: _ClassVar[BinaryExpr.BinaryOp]
        LogicalAnd: _ClassVar[BinaryExpr.BinaryOp]
        LogicalOr: _ClassVar[BinaryExpr.BinaryOp]
    Invalid: BinaryExpr.BinaryOp
    LogicalAnd: BinaryExpr.BinaryOp
    LogicalOr: BinaryExpr.BinaryOp
    OP_FIELD_NUMBER: _ClassVar[int]
    LEFT_FIELD_NUMBER: _ClassVar[int]
    RIGHT_FIELD_NUMBER: _ClassVar[int]
    op: BinaryExpr.BinaryOp
    left: Expr
    right: Expr
    def __init__(self, op: _Optional[_Union[BinaryExpr.BinaryOp, str]] = ..., left: _Optional[_Union[Expr, _Mapping]] = ..., right: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...

class BinaryArithOp(_message.Message):
    __slots__ = ("column_info", "arith_op", "right_operand")
    COLUMN_INFO_FIELD_NUMBER: _ClassVar[int]
    ARITH_OP_FIELD_NUMBER: _ClassVar[int]
    RIGHT_OPERAND_FIELD_NUMBER: _ClassVar[int]
    column_info: ColumnInfo
    arith_op: ArithOpType
    right_operand: GenericValue
    def __init__(self, column_info: _Optional[_Union[ColumnInfo, _Mapping]] = ..., arith_op: _Optional[_Union[ArithOpType, str]] = ..., right_operand: _Optional[_Union[GenericValue, _Mapping]] = ...) -> None: ...

class BinaryArithExpr(_message.Message):
    __slots__ = ("left", "right", "op")
    LEFT_FIELD_NUMBER: _ClassVar[int]
    RIGHT_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    left: Expr
    right: Expr
    op: ArithOpType
    def __init__(self, left: _Optional[_Union[Expr, _Mapping]] = ..., right: _Optional[_Union[Expr, _Mapping]] = ..., op: _Optional[_Union[ArithOpType, str]] = ...) -> None: ...

class BinaryArithOpEvalRangeExpr(_message.Message):
    __slots__ = ("column_info", "arith_op", "right_operand", "op", "value")
    COLUMN_INFO_FIELD_NUMBER: _ClassVar[int]
    ARITH_OP_FIELD_NUMBER: _ClassVar[int]
    RIGHT_OPERAND_FIELD_NUMBER: _ClassVar[int]
    OP_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    column_info: ColumnInfo
    arith_op: ArithOpType
    right_operand: GenericValue
    op: OpType
    value: GenericValue
    def __init__(self, column_info: _Optional[_Union[ColumnInfo, _Mapping]] = ..., arith_op: _Optional[_Union[ArithOpType, str]] = ..., right_operand: _Optional[_Union[GenericValue, _Mapping]] = ..., op: _Optional[_Union[OpType, str]] = ..., value: _Optional[_Union[GenericValue, _Mapping]] = ...) -> None: ...

class AlwaysTrueExpr(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Expr(_message.Message):
    __slots__ = ("term_expr", "unary_expr", "binary_expr", "compare_expr", "unary_range_expr", "binary_range_expr", "binary_arith_op_eval_range_expr", "binary_arith_expr", "value_expr", "column_expr", "exists_expr", "always_true_expr", "json_contains_expr")
    TERM_EXPR_FIELD_NUMBER: _ClassVar[int]
    UNARY_EXPR_FIELD_NUMBER: _ClassVar[int]
    BINARY_EXPR_FIELD_NUMBER: _ClassVar[int]
    COMPARE_EXPR_FIELD_NUMBER: _ClassVar[int]
    UNARY_RANGE_EXPR_FIELD_NUMBER: _ClassVar[int]
    BINARY_RANGE_EXPR_FIELD_NUMBER: _ClassVar[int]
    BINARY_ARITH_OP_EVAL_RANGE_EXPR_FIELD_NUMBER: _ClassVar[int]
    BINARY_ARITH_EXPR_FIELD_NUMBER: _ClassVar[int]
    VALUE_EXPR_FIELD_NUMBER: _ClassVar[int]
    COLUMN_EXPR_FIELD_NUMBER: _ClassVar[int]
    EXISTS_EXPR_FIELD_NUMBER: _ClassVar[int]
    ALWAYS_TRUE_EXPR_FIELD_NUMBER: _ClassVar[int]
    JSON_CONTAINS_EXPR_FIELD_NUMBER: _ClassVar[int]
    term_expr: TermExpr
    unary_expr: UnaryExpr
    binary_expr: BinaryExpr
    compare_expr: CompareExpr
    unary_range_expr: UnaryRangeExpr
    binary_range_expr: BinaryRangeExpr
    binary_arith_op_eval_range_expr: BinaryArithOpEvalRangeExpr
    binary_arith_expr: BinaryArithExpr
    value_expr: ValueExpr
    column_expr: ColumnExpr
    exists_expr: ExistsExpr
    always_true_expr: AlwaysTrueExpr
    json_contains_expr: JSONContainsExpr
    def __init__(self, term_expr: _Optional[_Union[TermExpr, _Mapping]] = ..., unary_expr: _Optional[_Union[UnaryExpr, _Mapping]] = ..., binary_expr: _Optional[_Union[BinaryExpr, _Mapping]] = ..., compare_expr: _Optional[_Union[CompareExpr, _Mapping]] = ..., unary_range_expr: _Optional[_Union[UnaryRangeExpr, _Mapping]] = ..., binary_range_expr: _Optional[_Union[BinaryRangeExpr, _Mapping]] = ..., binary_arith_op_eval_range_expr: _Optional[_Union[BinaryArithOpEvalRangeExpr, _Mapping]] = ..., binary_arith_expr: _Optional[_Union[BinaryArithExpr, _Mapping]] = ..., value_expr: _Optional[_Union[ValueExpr, _Mapping]] = ..., column_expr: _Optional[_Union[ColumnExpr, _Mapping]] = ..., exists_expr: _Optional[_Union[ExistsExpr, _Mapping]] = ..., always_true_expr: _Optional[_Union[AlwaysTrueExpr, _Mapping]] = ..., json_contains_expr: _Optional[_Union[JSONContainsExpr, _Mapping]] = ...) -> None: ...

class VectorANNS(_message.Message):
    __slots__ = ("vector_type", "field_id", "predicates", "query_info", "placeholder_tag")
    VECTOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIELD_ID_FIELD_NUMBER: _ClassVar[int]
    PREDICATES_FIELD_NUMBER: _ClassVar[int]
    QUERY_INFO_FIELD_NUMBER: _ClassVar[int]
    PLACEHOLDER_TAG_FIELD_NUMBER: _ClassVar[int]
    vector_type: VectorType
    field_id: int
    predicates: Expr
    query_info: QueryInfo
    placeholder_tag: str
    def __init__(self, vector_type: _Optional[_Union[VectorType, str]] = ..., field_id: _Optional[int] = ..., predicates: _Optional[_Union[Expr, _Mapping]] = ..., query_info: _Optional[_Union[QueryInfo, _Mapping]] = ..., placeholder_tag: _Optional[str] = ...) -> None: ...

class QueryPlanNode(_message.Message):
    __slots__ = ("predicates", "is_count", "limit")
    PREDICATES_FIELD_NUMBER: _ClassVar[int]
    IS_COUNT_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    predicates: Expr
    is_count: bool
    limit: int
    def __init__(self, predicates: _Optional[_Union[Expr, _Mapping]] = ..., is_count: bool = ..., limit: _Optional[int] = ...) -> None: ...

class PlanNode(_message.Message):
    __slots__ = ("vector_anns", "predicates", "query", "output_field_ids")
    VECTOR_ANNS_FIELD_NUMBER: _ClassVar[int]
    PREDICATES_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_IDS_FIELD_NUMBER: _ClassVar[int]
    vector_anns: VectorANNS
    predicates: Expr
    query: QueryPlanNode
    output_field_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, vector_anns: _Optional[_Union[VectorANNS, _Mapping]] = ..., predicates: _Optional[_Union[Expr, _Mapping]] = ..., query: _Optional[_Union[QueryPlanNode, _Mapping]] = ..., output_field_ids: _Optional[_Iterable[int]] = ...) -> None: ...
