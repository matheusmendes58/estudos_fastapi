from typing import Optional
from pydantic import BaseModel, field_validator
from aula_2.custom_execptions import ApiValidatorWordPost


class Curso(BaseModel):

    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @field_validator('titulo')
    @classmethod
    def validate_number_word(cls, value: str) -> str:
        """
        This function performs validation by counting the number of words in the sentence,
        if there are less than 3, an error will occur.

        :param value: Object for validate
        :return: A string
        """

        words = value.split(' ')
        if len(words) < 3:
            raise ApiValidatorWordPost()

        return value
