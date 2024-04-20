from typing import Optional

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String

from db.models.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    last_name: Mapped[str] = mapped_column(String(50))
    first_name: Mapped[str] = mapped_column(String(50))
    middle_name: Mapped[Optional[str]] = mapped_column(String(50))
    phone_number: Mapped[str] = mapped_column(String(12))
    cashback_amount: Mapped[int]
    role: Mapped[str]  # Местный / Турист

    def __repr__(self) -> str:
        return (f"User("
                f"id={self.id!r}, "
                f"last_name={self.last_name!r}, "
                f"first_name={self.first_name!r}, "
                f"middle_name={self.middle_name!r}, "
                f"phone_number={self.phone_number!r}, "
                f"cashback_amount={self.cashback_amount!r}, "
                f"role={self.role!r}, "
                )
