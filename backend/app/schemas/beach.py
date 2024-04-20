from typing import Annotated

from pydantic import BaseModel, Field


class BaseBeach(BaseModel):
    name: Annotated[str, Field(
        description="Название пляжа",
        examples=["Пляж Кристалл Уют"],
    )]
    number_sunbeds: Annotated[int, Field(
        description="Количество свободных шезлонгов",
        examples=[100],
    )]
    number_sunbeds_available: Annotated[int, Field(
        description="Всего шезлонгов",
        examples=[500],
    )]
    price_sunbeds: Annotated[int, Field(
        description="Цена аренды шезлонга",
        examples=[1000],
    )]


class BreachOut(BaseBeach):
    id: Annotated[int, Field(examples=[1])]
