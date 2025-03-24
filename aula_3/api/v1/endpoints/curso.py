#TODO Colocar docstrings nas funções
#TODO Melhorar funções post e get
#TODO Colocar tratativa de erros
from typing import List
from fastapi import APIRouter
from fastapi import status
from fastapi import Response
from aula_3.models.database.curso_db import CursoModel
from aula_3.schema.curso_schema import CursoSchema

router = APIRouter()

@router.post('/maneira2', status_code=status.HTTP_201_CREATED, response_model=CursoSchema)

async def post_curso2(curso: CursoSchema) -> CursoSchema:

    db = CursoModel()

    db.insert_curso(
        titulo=curso.titulo,
        aulas=curso.aulas,
        horas=curso.horas
    )

    return curso

#Get
@router.get('/', status_code=status.HTTP_200_OK, response_model=List[CursoSchema])

async def get_cursos() -> list:
    
    db = CursoModel()
    
    list_cursos = db.select_all_cursos()

    return list_cursos

@router.get('/{curso_id}', status_code=status.HTTP_200_OK, response_model=CursoSchema)

async def get_unique_curso(curso_id: int) -> dict:

    curso = CursoModel.select_curso(curso_id=curso_id)

    if curso:
        return curso
    else:
        raise 'colocar erro aqui'


#PUT
@router.put('/{curso_id}', status_code=status.HTTP_202_ACCEPTED, response_model=CursoSchema)

async def update_curso(curso_id: int, curso: CursoSchema) -> CursoSchema:

    try:
        CursoModel.update_curso(
            id_curso=curso_id,
            titulo=curso.titulo,
            aulas=curso.aulas,
            horas=curso.horas
        )

        return curso
    except Exception as e:
        raise 'colocar erro aqui'

#DELETE
@router.delete('/{curso_id}', status_code=status.HTTP_204_NO_CONTENT)

async def delete_a_course(curso_id: int) -> Response:

    try:
        CursoModel.delete_a_row(
            id_curso=curso_id
        )

        return Response(status_code=status.HTTP_204_NO_CONTENT)

    except Exception as e:
        raise e
