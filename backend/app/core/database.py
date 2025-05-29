from typing import Any, Generator
from sqlalchemy import create_engine, orm
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Database:
    __instance = None
    __initialized = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Database, cls).__new__(cls)
        return cls.__instance

    def __init__(self, db_url: str) -> None:
        if not self.__initialized:
            self.__engine = create_engine(db_url, echo=True)
            self.__session_factory = orm.scoped_session(
                orm.sessionmaker(
                    autocommit=False,
                    autoflush=False,
                    bind=self.__engine
                )
            )
            self.__initialized = True

    def create_database(self) -> None:
        Base.metadata.create_all(self.__engine)

    def get_session(self) -> Generator[Session, Any, Any]:
        session: Session = self.__session_factory()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
