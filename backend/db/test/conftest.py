from sqlalchemy.orm import Session

import pytest

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
