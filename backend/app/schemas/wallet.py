from typing import Annotated

from pydantic import BaseModel, Field


class WalletOut(BaseModel):
    id: Annotated[int, Field(examples=[1])]
    user_id: Annotated[int, Field(
        examples=[1],
        description="ID пользователя"
    )]
    amount_bonus: Annotated[int, Field(
        examples=[0],
        description="Количество бонусных баллов",
    )]
