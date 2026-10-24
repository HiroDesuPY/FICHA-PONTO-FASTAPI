from http import HTTPStatus

from fastapi import APIRouter
from app.models.usuarios import Funcionario_Schemas, PublicFuncionario_Schemas, PublicFuncionario_Schemas
from app.database.funcionario_models import Funcionario
auth_routers = APIRouter(prefix='/auth', tags=['auth'])


@auth_routers.post(
    '/login',
    response_model=PublicFuncionario_Schemas,
    status_code=HTTPStatus.OK
)
def login(user: Funcionario_Schemas):
    """
    Endpoint para autenticar um usuário (funcionário) no sistema.
    """
    return user


@auth_routers.post(
    '/signin',
    response_model=PublicFuncionario_Schemas,
    status_code=HTTPStatus.CREATED
)
def signin(user: Funcionario_Schemas):
    """
    Endpoint para registrar um novo usuário (funcionário) no sistema. Recebe os dados do funcionário no corpo da requisição e retorna os dados do funcionário registrado.
    """
    register_user = Funcionario_Schemas(
        id=user.id,
        nome=user.nome,
        email=user.email,
        senha=user.senha,
        admin=user.admin
    )
    return register_user
