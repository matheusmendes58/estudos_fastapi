from fastapi import FastAPI

app = FastAPI()

'''
    Executando api - com uvicorn instalado através do terminal coloque o seguinte comando estando dentro da pasta
    raiz do projeto uvicorn <nome do arquivo>:<nome do objeto exemplo que esta neste código app>
    ficaria assim: uvicorn first_steps:app
'''


@app.get('/')
async def first_steps() -> dict:
    """
    First steps with FastApi

    :return: A dict
    """

    return {
        'msg': 'Primeiros passos com fast api'
    }
