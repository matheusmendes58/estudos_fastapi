from fastapi import HTTPException
from fastapi import status


class ApiKeyErrorExceptions(HTTPException):

    def __init__(self, msg_error: str = 'Curso não indentificado, coloque o id correto.'):

        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=msg_error)
