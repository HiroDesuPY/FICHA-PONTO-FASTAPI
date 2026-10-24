from fastapi import FastAPI



app = FastAPI(title="API de Registro de Ponto", description="API para registro de ponto de funcionários", version="1.0.0", port="8000", host="0.0.0.0")




#-----------------------------


from app.routers.home_routes import home_routers
from app.routers.auth_routes import auth_routers
from app.routers.registros_routes import registros_routers

app.include_router(home_routers)
app.include_router(auth_routers)
app.include_router(registros_routers)