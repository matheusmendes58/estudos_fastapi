from aula_3.models.database.base_db import BASE

from sqlalchemy import Column, INTEGER, VARCHAR


class CursoModel(BASE):

    __tablename__ = 'cursos'

    id_curso = Column(INTEGER, primary_key=True, autoincrement=True)
    titulo = Column(VARCHAR(255))
    aulas = Column(INTEGER)
    horas = Column(INTEGER)
