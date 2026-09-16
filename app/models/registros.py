from pydantic import BaseModel
from app.models.usuarios import Funcionario


class Registro_entrada(Funcionario):
    id: int
    data: str
    time: str
    tipo: str
    funcionario_id: int

class Registro_time(BaseModel):
    time: str
    data: str