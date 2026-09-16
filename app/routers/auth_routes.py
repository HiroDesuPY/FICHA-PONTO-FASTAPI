from http import HTTPStatus

from fastapi import APIRouter
from app.models.usuarios import Funcionario, PublicFuncionario

auth_routers = APIRouter(prefix='/auth', tags=['auth'])


@auth_routers.post(
    '/login',
    response_model=PublicFuncionario,
    status_code=HTTPStatus.CREATED
)
def login(user: Funcionario):
    return user