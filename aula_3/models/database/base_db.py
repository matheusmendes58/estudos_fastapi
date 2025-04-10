from aula_3.config import settings

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

ENGINE_ALCHEMY = create_engine(settings.connect_db, echo=False)
DBSESSION = scoped_session(sessionmaker(bind=ENGINE_ALCHEMY, expire_on_commit=False))
SESSION = scoped_session(sessionmaker(bind=ENGINE_ALCHEMY))
BASE = declarative_base()

def create_all():
    """
    Create table in database.
    However, if it has already been created, it can be used as a connection test.

    :return: None
    """
    from aula_3.models.database.curso_db import CursoModel
    BASE.metadata.create_all(ENGINE_ALCHEMY)
