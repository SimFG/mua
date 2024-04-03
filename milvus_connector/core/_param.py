from typing import Any, Dict, List

from ._const import *


class RPCParam:
    params: Dict[str, Any] = {}

    def add_param(self, key: str, value: Any) -> None:
        self.params[key] = value

    def extend_params(self, params: Dict[str, Any]) -> None:
        self.params.update(params)

    def clear_param(self) -> None:
        self.params.clear()

    def get_params(self) -> Dict[str, Any]:
        # some key should be converted
        return self.params

    def _db_name(self) -> str:
        return self.params.get(DB_NAME, "")

    def _collection_name(self) -> str:
        return self.params.get(COLLECTION_NAME, "")

    def _partition_name(self) -> str:
        return self.params.get(PARTITION_NAME, "")

    def _partition_names(self) -> List[str]:
        _partition = self.params.get(PARTITION_NAME, "")
        return [_partition] if _partition else []

    def _partition_names(self) -> str:
        return self.params.get(PARTITION_NAMES, "")

    def _user_name(self) -> str:
        return self.params.get(USER_NAME, self.params.get(USER_NAME2, ""))

    def _role_name(self) -> str:
        return self.params.get(ROLE_NAME, "")