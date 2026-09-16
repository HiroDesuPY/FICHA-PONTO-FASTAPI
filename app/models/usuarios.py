from pydantic import BaseModel
from typing import Optional


class Funcionario(BaseModel):
    id: int
    nome: str
    senha: str
    ativo: bool
    admin: Optional[bool] = False



class PublicFuncionario(Funcionario):
    id: int
    nome: str
    ativo: bool
    admin: Optional[bool] = False


