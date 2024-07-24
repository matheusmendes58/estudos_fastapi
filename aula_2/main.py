from fastapi import FastAPI, status
from fastapi import Path
from custom_execptions import ApiKeyErrorExceptions
from models import Curso
from typing import Any

app = FastAPI()

cursos = {
    1: {
        'titulo': 'Teste',
        'aulas': 112,
        'horas': 58
    },

    2: {
        'titulo': 'teste 2',
        'aulas': 1144,
        'horas': 2000
    }
}


@app.get('/cursos')
async def get_cursos() -> dict:
    """
    get dict of course

    :return: a list of course
    """

    return cursos


@app.get('/curso/{curso_id}')
async def get_curso(curso_id: int = Path(title='ID do curso',
                                         description='Números entre 1 e 3',
                                         gt=0,
                                         lt=3)) -> dict:
    """
    search a course by unique id

    :param curso_id: int, id of course
    :return: a dict
    """

    try:
        return cursos[curso_id]

    except KeyError:
        raise ApiKeyErrorExceptions()


@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso) -> Curso:
    #TODO colocar tratamento para não repita conteudo ja inserido
    """
    Send a new curso to the api. Example to send:

    {
        'titulo': str,
        'aulas': int,
        'horas': int
    }

    :param curso: object from Curso
    :return: object from Curso
    """

    next_id = len(cursos) + 1

    cursos[next_id] = curso

    return curso


@app.put('/curso/{curso_id}', status_code=status.HTTP_201_CREATED)
async def update_curso(curso_id: int, curso: Curso) -> Curso:
    #TODO COLOCAR TRATAMENTO DE ERRO
    """
    update a curso. Example to the send in api - json

    {
        'titulo': str,
        'aulas': int,
        'horas': int
    }

    :param curso_id: int of id
    :param curso: object from Curso
    :return: object from Curso
    """

    if curso_id in cursos:
        cursos[curso_id] = curso
        return curso


@app.delete('/curso/{curso_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_curso(curso_id: int):
    #TODO COLOCAR TRATAMENTO DE ERRO CASO NÂO HOUVER ID DO CURSO PARA DELETAR
    """
    delete a curso in api
    :param curso_id: int of id
    :return:
    """

    if curso_id in cursos:

        del cursos[curso_id]

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app')
