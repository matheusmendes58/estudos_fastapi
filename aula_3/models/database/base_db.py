from aula_3.config import settings
from aula_3.models.database.curso_db import CursoModel

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

ENGINE_ALCHEMY = create_engine(settings.connect_db, echo=True)
DBSESSION = scoped_session(sessionmaker(bind=ENGINE_ALCHEMY, expire_on_commit=False))
SESSION = scoped_session(sessionmaker(bind=ENGINE_ALCHEMY))
BASE = declarative_base()

def create_tables():
    CursoModel()
    BASE.metada.create_tables(ENGINE_ALCHEMY)
