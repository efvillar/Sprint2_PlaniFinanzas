from pydantic import BaseModel

class Egreso(BaseModel):
    id: int
    fecha: str
    categoria_egreso: str
    valor: float
    forma_pago: str
    descripcion: str
    
egresos = {
    1: Egreso(id=1, fecha="08-12-2020", categoria_egreso="vestuario", valor=60000, forma_pago="efectivo", descripcion="camisa verde"),
    2: Egreso(id=2, fecha="08-12-2020", categoria_egreso="transporte", valor=10000, forma_pago="efectivo", descripcion="taxi al trabajo"),
    3: Egreso(id=3, fecha="09-12-2020", categoria_egreso="alimentacion", valor=90000, forma_pago="tarjeta de credito", descripcion="restaurante arabe")
}

def obtener_egresos():
    #haga lo que tenga que hacer para conectarse a la base de datos
    lista_egresos = []
    for e in egresos:
        lista_egresos.append(egresos[e])
    return lista_egresos

def crear_egreso(egreso: Egreso):
    if egreso.id in egresos:
        return False
    else:
        egresos[egreso.id] = egreso
        return True