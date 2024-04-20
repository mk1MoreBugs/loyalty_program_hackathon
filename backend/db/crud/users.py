from sqlalchemy import select
from sqlalchemy.orm import Session

from db.models.user import User


def create_user(
        db_session: Session,
        last_name: str,
        first_name: str,
        phone_number: str,
        cashback_amount: int,
        middle_name: str | None = None,
):
    db_session.add(
        User(
            last_name=last_name,
            first_name=first_name,
            middle_name=middle_name,
            phone_number=phone_number,
            cashback_amount=cashback_amount,
        )
    )
    db_session.commit()


def read_user(db_session: Session):
    stmt = select(User)

    return db_session.execute(stmt).scalars().all()
