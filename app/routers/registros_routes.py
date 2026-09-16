from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from http import HTTPStatus
from app.models.registros import Registro_entrada, Registro_time
from app.utils.data_utils import current_date, current_date, current_time


registros_routers = APIRouter(prefix='/registros', tags=['registros'])



@registros_routers.get(
    '/',
    response_model=Registro_time,
    status_code=HTTPStatus.OK
)
def registro_horario(time: str = current_time(), data: str = current_date()):
    return {
        "time": time,
        "data": data
    }


@registros_routers.post('/entrada', response_class=HTMLResponse, status_code=HTTPStatus.CREATED)
def registro_entrada():
    return "<p>Registro de entrada realizado com sucesso</p>"

