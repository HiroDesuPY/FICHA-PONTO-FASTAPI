from fastapi import APIRouter
from fastapi.responses import HTMLResponse

home_routers = APIRouter(prefix='/home', tags=['home'])


@home_routers.get('/', response_class=HTMLResponse)
def home():
    return HTMLResponse(content=open("templates/index.html").read())