from enum import Enum
from typing import Annotated

from pydantic import BaseModel, Field


class RoleEnum(str, Enum):
    local = "Местный"
    tourist = "Турист"


class BaseUser(BaseModel):
    last_name: Annotated[str, Field(max_length=50, examples=["Иванов"])]
    first_name: Annotated[str, Field(max_length=50, examples=["Иван"])]
    middle_name: Annotated[str | None, Field(max_length=50, examples=["Иванович"])] = None
    phone_number: Annotated[str, Field(max_length=12, examples=["+79123456789"])]
    cashback_amount: Annotated[int, Field(examples=["1000"])]
    role: Annotated[RoleEnum, Field(examples=["Местный"])]


class UserOut(BaseUser):
    id: Annotated[int, Field(examples=["1"])]
