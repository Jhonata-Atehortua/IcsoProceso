from fastapi import FastAPI
from routes.route_click import Routas_Click_Activo

app = FastAPI()

app.include_router(Routas_Click_Activo,prefix="/ClickActivo")

