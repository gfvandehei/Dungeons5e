from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from Dungeons5e.Model.SQLAlchemyModels import Base
import logging


class DungeonsDBBaseSession(object):

    def __init__(self, session_maker):
        self._maker = session_maker
        self._session: Session = None
        self._in_context = False
        self._logger = logging.getLogger(__name__)

    @property
    def session(self):
        if self._session is None:
            self._session = self._maker()
        return self._session
    
    def close(self):
        if self._session is not None:
            self._session.close()

    def __enter__(self) -> Session:
        self._in_context = True
        return self.session
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.close()


class DungeonsDBBaseHandler(object):

    def __init__(self, connection_string: str):
        self._engine = create_engine(connection_string)
        Base.metadata.create_all(self._engine)
        self._session_maker = sessionmaker(bind=self._engine)

    def get_session(self):
        return DungeonsDBBaseSession(self._session_maker)
        