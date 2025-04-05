from sqlalchemy.exc import SQLAlchemyError

from aula_3.models.database.base_db import BASE, DBSESSION

from sqlalchemy import Column, INTEGER, VARCHAR

class CursoModel(BASE):

    __tablename__ = 'cursos'

    id_curso = Column(INTEGER, primary_key=True, autoincrement=True)
    titulo = Column(VARCHAR(255))
    aulas = Column(INTEGER)
    horas = Column(INTEGER)

    @classmethod
    def insert_curso(cls,
                     titulo: str = None,
                     aulas: int = None,
                     horas: int = None
                     ) -> None:

        """
        Insert into in DB

        :param titulo: A string, name of course
        :param aulas: A int, total numbers of classes in course
        :param horas: A int, total course hours
        :return: None
        """

        try:
            DBSESSION.merge(
                CursoModel(
                    titulo=titulo,
                    aulas=aulas,
                    horas=horas
                )
            )
            DBSESSION.commit()
        except Exception as e:
            DBSESSION.rollback()
            raise e
        finally:
            DBSESSION.close()

    @classmethod
    def select_all_cursos(cls) -> list:
        """
        select all courses

        :return: A list of courses
        """

        try:
            return DBSESSION.query(CursoModel).all()
        except Exception as e:
            raise e

    @classmethod
    def select_curso(cls, curso_id: int) -> dict:
        """
        Get a curso

        :param curso_id: Number of course
        :return: A dict with information of course
        """

        try:
             return DBSESSION.query(CursoModel).filter(CursoModel.id_curso == curso_id).first()
        except Exception as e:
            raise e

    @classmethod
    def update_curso(cls, id_curso: int, titulo: str = None, aulas: int = None, horas: int = None) -> None:
        """
        Update in database

        :param id_curso: id of course
        :param titulo: Name of course
        :param aulas: total class of course
        :param horas: total hours of course
        :return: None
        """

        course_update = {
            'titulo': titulo,
            'aulas': aulas,
            'horas': horas
        }

        course = {key: value for key, value in course_update.items() if value is not None}

        try:
            DBSESSION.query(CursoModel).filter(CursoModel.id_curso == id_curso).update(course)
            DBSESSION.commit()
        except Exception as e:
            DBSESSION.rollback()
            raise e

    @classmethod
    def delete_a_row(cls, id_curso: int) -> None:
        """
        delete a row in database

        :param id_curso: id of course
        :return: A None
        """

        try:
            DBSESSION.query(CursoModel).filter(CursoModel.id_curso == id_curso).delete(synchronize_session=False)
            DBSESSION.commit()

        except SQLAlchemyError as e:
            DBSESSION.rollback()
            raise e
