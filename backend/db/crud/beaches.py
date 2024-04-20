from sqlalchemy import insert
from sqlalchemy import select, update
from sqlalchemy.orm import Session

from db import Beach
from db.models.user import User


def create_beach(
        db_session: Session,
        name: str,
        number_sunbeds: int,
        number_sunbeds_available: int,
        price_sunbeds: int,
):
    stmt = insert(Beach).values(
        name=name,
        number_sunbeds=number_sunbeds,
        number_sunbeds_available=number_sunbeds_available,
        price_sunbeds=price_sunbeds,
    )
    db_session.execute(stmt)
    db_session.commit()


def read_beaches(db_session: Session):
    stmt = select(Beach)
    return db_session.execute(stmt).scalars().all()


def update_beach(
        db_session: Session,
        beach_id: int,
        new_number_sunbeds: int,
):
    stmt = (
        update(Beach)
        .where(Beach.id == beach_id)
        .values(number_sunbeds=new_number_sunbeds)
    )
    db_session.execute(stmt)
    db_session.commit()
