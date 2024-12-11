from fastapi import HTTPException
from fastapi import status


class Myerror(HTTPException):
    pass
