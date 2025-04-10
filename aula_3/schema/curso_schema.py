from typing import Optional

from pydantic import BaseModel as SCBasemodel, Field


class CursoSchema(SCBasemodel):

    id_curso: Optional[int] = Field(description='ID único do curso')
    titulo: str = Field(description='Título do curso')
    aulas: int = Field(description='Número total de aulas')
    horas: int = Field(description='Carga horária total em horas')

    class Config:
        from_attributes = True

        schema_extra = {
            "example": {
                "id_curso": 10,
                "titulo": "Tratamento de exceção",
                "aulas": 8000,
                "horas": 1250
            }
        }
