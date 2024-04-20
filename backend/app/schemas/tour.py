from typing import Annotated

from pydantic import BaseModel, Field


class BaseTour(BaseModel):
    name: Annotated[str, Field(
        examples=["По Бугазской косе"],
        description="Название маршрута",
    )]
    price: Annotated[int, Field(
        examples=["1000"],
        description="Цена маршрута"
    )]
    cashback_percent: Annotated[int, Field(
        ge=0, le=100,
        examples=[10],
        description="Кэшбэк в %",
    )]


class TourOut(BaseTour):
    id: Annotated[int, Field(examples=[1])]
