from sqlalchemy import select, update
from sqlalchemy.orm import Session

from db import User
from db.models.wallet import Wallet


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
    db_session.commit()


def read_wallets(db_session: Session):
    stmt = select(Wallet)
    return db_session.execute(stmt).scalars().all()


def read_wallets_by_id(db_session: Session, user_id: int):
    stmt = select(Wallet).where(user_id=user_id)
    return db_session.execute(stmt).scalars().one()


def update_wallet(db_session: Session, user_id: int, new_amount: int):
    stmt = (
        update(Wallet)
        .where(Wallet.user_id == user_id)
        .values(amount_bonus=new_amount)
    )
    db_session.execute(stmt)
    db_session.commit()
