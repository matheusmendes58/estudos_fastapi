from typing import Optional

from pydantic import BaseModel as SCBasemodel


class CursoSchema(SCBasemodel):

    id_curso: Optional[int]
    titulo: str
    aulas: int
    horas: int

    class Config:
        from_attributes = True
