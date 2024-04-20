from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from db.models.base import Base


class Tour(Base):
    __tablename__ = "tours"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    price: Mapped[int]
    cashback_percent: Mapped[int]

    def __repr__(self) -> str:
        return (f"Tour("
                f"id={self.id!r}, "
                f"name={self.name!r}, "
                f"price={self.price!r}, "
                f"cashback_percent={self.cashback_percent!r}, "
                )
