from fastapi import APIRouter

from aula_3.api.v1.endpoints import curso

api_router = APIRouter()
api_router.include_router(curso.router, prefix='/cursos', tags=['cursos'])
