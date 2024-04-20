from typing import Annotated

from pydantic import BaseModel, Field


class BaseTour(BaseModel):
    name: Annotated[str, Field(max_length=50, examples=["По Бугазской косе"])]
    price: Annotated[int, Field(examples=["1000"])]
    cashback_percent: Annotated[int, Field(ge=0, le=100, examples=["10"])]


class TourOut(BaseTour):
    id: Annotated[int, Field(examples=["1"])]
