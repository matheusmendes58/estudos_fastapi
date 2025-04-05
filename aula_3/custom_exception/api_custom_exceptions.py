from fastapi import HTTPException
from fastapi import status


class InputInvalidError(HTTPException):

    def __init__(self, msg_error: str = 'Input deve ser valido verifique o json'):

        super().__init__(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=msg_error)

class ApiInvalidFieldInDatabase(HTTPException):

    def __init__(self, msg_error: str = 'Violação de integridade no banco de dados (campo duplicado ou inválido).'):

        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=msg_error)

class ApiResponseValidationError(HTTPException):

    def __init__(self, msg_error: str = 'Nenhum curso encontrado'):

        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=msg_error)