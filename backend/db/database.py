from sqlalchemy import create_engine

from db.models.base import Base


def create_db_tables_and_engine(database_url, echo=False):
    engine = create_engine(database_url, echo=echo)
    Base.metadata.create_all(engine)
    return engine
