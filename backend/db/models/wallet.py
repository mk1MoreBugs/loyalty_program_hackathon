from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from db.models.base import Base


class Wallet(Base):
    __tablename__ = "wallets"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount_bonus: Mapped[int]
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", onupdate="CASCADE", ondelete="CASCADE")
    )

    user: Mapped["User"] = relationship(back_populates="wallet")

    def __repr__(self) -> str:
        return (f"Wallet("
                f"id={self.id!r}, "
                f"amount_bonus={self.amount_bonus!r}, "
                f"user_id={self.user_id!r}, "
                )
