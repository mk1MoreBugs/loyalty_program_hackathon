from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from db.models.base import Base


class Beach(Base):
    __tablename__ = "beaches"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    number_sunbeds: Mapped[int]
    number_sunbeds_available: Mapped[int]
    price_sunbeds: Mapped[int]
