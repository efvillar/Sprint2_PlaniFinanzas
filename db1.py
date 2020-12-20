from pydantic import BaseModel


class Transaccion_I(BaseModel):
    id: int
    fechaTransaccion:str
    categoria: str
    valor: float
    formaPago:str
    descripcion: str


    
transaciones_I = {
    1: Transaccion_I (id=1 , fechaTransaccion = "01-11-2020", categoria="salario",valor=2000000, formaPago="transferencia", descripcion= "Quincena 1"),
    2: Transaccion_I (id=2 , fechaTransaccion = "08-11-2020", categoria="prima",valor=1200000, formaPago="transferencia", descripcion= "Prima"),
    3: Transaccion_I (id=3 , fechaTransaccion = "15-12-2020", categoria="salario",valor=2000000, formaPago="transferencia", descripcion= "Quincena 2"),
}


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
