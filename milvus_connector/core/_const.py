from typing_extensions import Annotated
from pydantic import Field

DB_NAME = "db_name"
COLLECTION_NAME = "collection_name"
PARTITION_NAME = "partition_name"
PARTITION_NAMES = "partition_names"
USER_NAME = "user_name"
USER_NAME2 = "username"
ROLE_NAME = "role_name"

VERSION = "0.0.1"

# validator
NOT_EMPTY_STR = Annotated[str, Field(min_length=1)]