from sqlalchemy.orm import Session

import pytest

from .. import Beach, User
from ..database import create_db_tables_and_engine
from ..models.wallet import Wallet


@pytest.fixture()
def db_session():
    engine = create_db_tables_and_engine("sqlite://", echo=True)
    with Session(engine) as session:
        return session


@pytest.fixture()
def wallet():
    return Wallet(
        id=1,
        amount_bonus=100,
        user_id=1
    )


@pytest.fixture()
def beach():
    return Beach(
        name="Пляж 1",
        number_sunbeds=15,
        number_sunbeds_available=1000,
        price_sunbeds=300,
    )


@pytest.fixture()
def user():
    return User(
        id=1,
        last_name="Foo",
        first_name="Bar",
        phone_number="+79000000000",
        cashback_amount=0,
        role="Местный",
    )
