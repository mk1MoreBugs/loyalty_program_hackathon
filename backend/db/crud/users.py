from sqlalchemy import select, insert, delete
from sqlalchemy.orm import Session

from db.models.user import User
from db.models.wallet import Wallet


def create_user(
        db_session: Session,
        last_name: str,
        first_name: str,
        phone_number: str,
        cashback_amount: int,
        role: str,
        middle_name: str | None = None,
):
    stmt = insert(User).values(
        last_name=last_name,
        first_name=first_name,
        middle_name=middle_name,
        phone_number=phone_number,
        cashback_amount=cashback_amount,
        role=role,
    )
    user_id = db_session.execute(stmt).inserted_primary_key[0]
    create_wallet(
        db_session=db_session,
        amount_bonus=0,
        user_id=user_id,
    )
    db_session.commit()


def create_wallet(
        db_session: Session,
        amount_bonus: int,
        user_id: int,
):
    db_session.add(
        Wallet(
            amount_bonus=amount_bonus,
            user_id=user_id
        )
    )


def read_users(db_session: Session):
    stmt = select(User)

    return db_session.execute(stmt).scalars().all()


def delete_user(db_session: Session, user_id: int):
    stmt = delete(User).where(User.id == user_id)
    db_session.execute(stmt)
    db_session.commit()
