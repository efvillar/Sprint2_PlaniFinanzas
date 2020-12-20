from fastapi import FastAPI, HTTPException
import db

app = FastAPI()

@app.get("/egresos/")
async def obtener_egresos():
    egresos = db.obtener_egresos()
    return  egresos

@app.post("/egresos/crear/")
async def crear_egreso(egreso: db.Egreso):
    creada_exitosamente = db.crear_egreso(egreso)
    if creada_exitosamente:
        return {"mensaje": "Egreso creado correctamente"}
    else:
        raise HTTPException(status_code=400, detail="error, egreso con ese id ya existe")

@app.get("/ingresos/")
async def obtener_ingresos():
    ingresos = db.obtener_ingresos()
    return  ingresos

@app.post("/ingresos/crear/")
async def crear_ingreso(ingreso: db.Ingreso):
    creada_exitosamente = db.crear_ingreso(ingreso)
    if creada_exitosamente:
        return {"mensaje": "Ingreso creado correctamente"}
    else:
        raise HTTPException(status_code=400, detail="error, ingreso con ese id ya existe")
