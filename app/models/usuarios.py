from pydantic import BaseModel
from typing import Optional


class Funcionario_Schemas(BaseModel):
    id: int
    nome: str
    senha: str
    ativo: bool
    admin: Optional[bool] = False



class PublicFuncionario_Schemas(Funcionario_Schemas):
    id: int
    nome: str
    ativo: bool
    admin: Optional[bool] = False


