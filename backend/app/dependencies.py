from sqlalchemy.orm import Session

from app.config import SQLALCHEMY_DATABASE_URL
from db.database import create_db_tables_and_engine


engine = create_db_tables_and_engine(
    database_url=SQLALCHEMY_DATABASE_URL,
)


def session_db():
    with Session(engine) as session:
        yield session
