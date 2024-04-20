from sqlalchemy.orm import Session

import pytest

from ..database import create_db_tables_and_engine


@pytest.fixture()
def db_session():
    engine = create_db_tables_and_engine("sqlite://", echo=True)
    with Session(engine) as session:
        return session
