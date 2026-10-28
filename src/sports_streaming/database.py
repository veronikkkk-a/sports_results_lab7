"""SQLAlchemy engine, session factory and SQLite FK enforcement."""
from __future__ import annotations
from pathlib import Path
from sqlalchemy import Engine, create_engine, event
from sqlalchemy.orm import Session, sessionmaker
from sports_streaming.db_models import Base

def make_engine(url: str = "sqlite:///sports_results.db", *, echo: bool = False) -> Engine:
    engine = create_engine(url, echo=echo)
    if url.startswith("sqlite"):
        @event.listens_for(engine, "connect")
        def enable_foreign_keys(dbapi_connection, _connection_record) -> None:
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA foreign_keys=ON")
            cursor.close()
    return engine

def make_session_factory(engine: Engine) -> sessionmaker[Session]:
    return sessionmaker(bind=engine, expire_on_commit=False)

def initialize_database(engine: Engine) -> None:
    Base.metadata.create_all(engine)
