
from typing import List
from fastapi import APIRouter
from fastapi import status
from fastapi import Response
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from aula_3.models.database.curso_db import CursoModel
from aula_3.schema.curso_schema import CursoSchema
from aula_3.custom_exception.api_custom_exceptions import ApiInvalidFieldInDatabase, ApiResponseValidationError

router = APIRouter()

@router.post('/maneira2', status_code=status.HTTP_201_CREATED, response_model=CursoSchema)

async def post_curso2(curso: CursoSchema) -> CursoSchema:
    """
    Specific endpoint for send new curso in database.
    example:

    {
    "id_curso": 10,
    "titulo": "tratamento de excessão",
    "aulas": 8000,
    "horas": 1250
    }

    :param curso: Object CursoSchema
    :return: Object CursoSchema
    """

    db = CursoModel()
    try:
        db.insert_curso(
            titulo=curso.titulo,
            aulas=curso.aulas,
            horas=curso.horas
        )

        return curso

    except IntegrityError:
        raise ApiInvalidFieldInDatabase()

#Get
@router.get('/', status_code=status.HTTP_200_OK, response_model=List[CursoSchema])

async def get_cursos() -> list:
    """
    Specific endpoint for return all cursos in database

    :return: A list of cursos
    """

    db = CursoModel()

    list_cursos = db.select_all_cursos()

    if not list_cursos:
        return [{'msg': 'Nenhum curso encontrado'}]

    return list_cursos

@router.get('/{curso_id}', status_code=status.HTTP_200_OK, response_model=CursoSchema)

async def get_unique_curso(curso_id: int) -> dict:
    """
    Specific endpoint for return a unique curso in database

    :param curso_id: ID of curso
    :return: A dict curso with titulo, horas, etc

    """

    curso = CursoModel.select_curso(curso_id=curso_id)

    if curso:
        return curso
    else:
        raise ApiResponseValidationError()

#PUT
@router.put('/{curso_id}', status_code=status.HTTP_202_ACCEPTED, response_model=CursoSchema)

async def update_curso(curso_id: int, curso: CursoSchema) -> CursoSchema:
    """
    Specific endpoint for update cursos in database.
    example:

    {
    "id_curso": 20,
    "titulo": "tratamento",
    "aulas": 350,
    "horas": 65468
    }

    :param curso_id: ID of curso
    :param curso: Object of CursoSchema
    :return: Object of CursoSchema
    """

    try:
        CursoModel.update_curso(
            id_curso=curso_id,
            titulo=curso.titulo,
            aulas=curso.aulas,
            horas=curso.horas
        )

        return curso
    except IntegrityError:
        raise ApiInvalidFieldInDatabase()

    except Exception as e:
        raise e

#DELETE
@router.delete('/{curso_id}', status_code=status.HTTP_204_NO_CONTENT)

async def delete_a_course(curso_id: int) -> Response:
    """
    Specific endpoint for delete curso in database.

    :param curso_id: ID of curso in database
    :return: Api response
    """

    try:
        curso = CursoModel.select_curso(curso_id=curso_id)

        if not curso:
            raise ApiResponseValidationError()

        CursoModel.delete_a_row(
            id_curso=curso_id
        )

        return Response(status_code=status.HTTP_204_NO_CONTENT)

    except SQLAlchemyError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro ao tentar remover o curso do banco de dados."
        )
