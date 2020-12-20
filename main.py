from fastapi import FastAPI
from fastapi import HTTPException
import db, db1, db2

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [

    "http://localhost:8081",
    "https://planifinanzas-front.herokuapp.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)


@app.get("/transacciones/")
async def obtener_transacciones():
    transacciones = db.obtener_Transaciones()
    return transacciones

@app.post("/transacciones/agregar/")
async  def agregar_transaccion(transaccion:db.Transaccion):
    agregada_exitosamente=db.agregar_transaccion(transaccion)
    if agregada_exitosamente:
        return {"mensaje":"Transacción agregada exitosamente"}
    else:
        raise  HTTPException(status_code=400, detail="Error, el id de la transaccion y existe ")


@app.get("/ingresos/")
async def obtener_transacciones_I():
    transacciones_I = db1.obtener_Transaciones_I()
    return transacciones_I


@app.post("/ingresos/agregar/")
async  def agregar_transaccion_I(transaccion:db1.Transaccion_I):
    agregada_exitosamente=db1.agregar_transaccion_I(transaccion)
    if agregada_exitosamente:
        return {"mensaje":"Transacción agregada exitosamente"}
    else:
        raise  HTTPException(status_code=400, detail="Error, el id de la transaccion de ingreso y existe ")


@app.get("/usuarios/")
async def obtener_Usuarios():
    usuarios_DB = db2.obtener_Usuarios()
    return usuarios_DB

