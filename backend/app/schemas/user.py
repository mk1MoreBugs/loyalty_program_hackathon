from enum import Enum
from typing import Annotated

from pydantic import BaseModel, Field


class RoleEnum(str, Enum):
    local = "Местный"
    tourist = "Турист"


class BaseUser(BaseModel):
    last_name: Annotated[str, Field(
        max_length=50,
        examples=["Иванов"],
        description="Фамилия",
    )]
    first_name: Annotated[str, Field(
        max_length=50,
        examples=["Иван"],
        description="Имя",
    )]
    middle_name: Annotated[str | None, Field(
        max_length=50,
        examples=["Иванович"],
        description="Отчество",
    )] = None
    phone_number: Annotated[str, Field(
        max_length=12,
        examples=["+79123456789"],
        description="Номер телефона",
    )]
    cashback_amount: Annotated[int, Field(
        examples=["0"],
        description="Количество бонусных баллов",

    )]
    role: Annotated[RoleEnum, Field(
        examples=["Местный"],
        description="Роль пользователя",
    )]


class UserOut(BaseUser):
    id: Annotated[int, Field(examples=["1"])]
