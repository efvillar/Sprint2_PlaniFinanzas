from pydantic import BaseModel


class Transaccion_I(BaseModel):
    id: int
    fechaTransaccion:str
    categoria: str
    valor: float
    formaPago:str
    descripcion: str


    
transaciones_I = {
    1: Transaccion_I (id=1 , fechaTransaccion = "20-11-2020", categoria="Alimentación",valor=200000, formaPago="tarjeta_débito", descripcion= "Almuerzo restaurante Carne de Res"),
    2: Transaccion_I (id=2 , fechaTransaccion = "22-11-2020", categoria="Vestuario",valor=980000, formaPago="tajerta_crédito", descripcion= "Uniformes dotación trabajadores"),
    3: Transaccion_I (id=3 , fechaTransaccion = "01-12-2020", categoria="Viveres",valor=600000, formaPago="efectivo", descripcion= "Mercado mensual familiar"),
}

"""
def obtener_Transaciones_I():
    #haga lo que tenga que hacer para conectarse a la base de datos y obtner todas las ordenes
    lista_transacciones_I=[]
    for i in transaciones_I:
        lista_transacciones_I.append(transaciones_I[i])
    return lista_transacciones_I


def agregar_transaccion_I(transaccion: Transaccion_I):
    if transaccion.id in transaciones_I:
        return False
    else:
        transaciones_I[transaccion_I.id]= transaccion
        return True
"""