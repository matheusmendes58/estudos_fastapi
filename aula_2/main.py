
from typing import Any, Optional, List, Dict
from time import sleep

from fastapi import FastAPI, status
from fastapi import Path
from fastapi import Query
from fastapi import Depends
from custom_execptions import ApiKeyErrorExceptions
from models import Curso

#TODO documentar código e personalizar documentação fastapi

#conceito de injeção de dependencias
def fake_db() -> None:
    print('Abrindo conexão com banco de dados..')
    sleep(1)
    print('Conectado...')

app = FastAPI(
    title='API DE APRENDIZADO',
    description='Esta api é apenas para estudar o framework fastapi.',
    version='0.0.9',
    docs_url='/basicdocs',
    redoc_url='/completedocs'
)

cursos = {
    1:Curso(id=1, titulo='Teste testenildo testesan', aulas=112, horas=58),

    2:Curso(id=2, titulo='Teste 2 e 2', aulas=500, horas=800),
}


@app.get('/cursos',
         description='Retorna todos os cursos ou uma lista vazia',
         summary='Retorna todos os curso',
         response_model=Dict[int, Curso],
         response_description='Cursos encontrados com sucesso'
         )

async def get_cursos(db: Any = Depends(fake_db)) -> dict:
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

# Aprendendo conceito de Query Parameters
@app.get('/calculadora')
async def sum_numbers(a: int = Query(title='A number for sum', description='Number greater than 5', gt=5),
              b: int = Query(title='A number for sum', description='Number greater than 5', gt=5),
              c: Optional[int] = None) -> dict:
    #TODO realizar tratamento de erro para inputs menores que 5
    """
    learning concept about it QUERY PARAMETERS

    :param a: a number for sum
    :param b: a number for sum
    :param c: a number for sum

    :return: a json from result of a sum
    """
    result = a + b

    if c:
        result = result + c

    return {'resultado': result}

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app')
