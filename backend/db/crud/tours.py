from sqlalchemy import select
from sqlalchemy.orm import Session

from db.models.tour import Tour


def create_tour(
        db_session: Session,
        name: str,
        price: int,
        cashback_percent: int,
):
    db_session.add(
        Tour(
            name=name,
            price=price,
            cashback_percent=cashback_percent,
        )
    )
    db_session.commit()


def read_tour(db_session: Session):
    stmt = select(Tour)

    return db_session.execute(stmt).scalars().all()
