from pydantic import BaseModel



class Transaccion_I(BaseModel):
    id_I: int
    fechaTransaccion_I:str
    categoria_I: str
    valor_I: float
    descripcion_I: str 



transaciones_I = {
    1: Transaccion_I (id_I=3 , fechaTransaccion_I = "01-12-2020", categoria_I="salario",valor_I=2000000,  descripcion= "Quincena 1"),
    2: Transaccion_I (id_I=2 , fechaTransaccion_I = "08-12-2020", categoria_I="prima",valor_I=1200000,  descripcion= "Prima de Diciembre"),
    3: Transaccion_I (id_I=3 , fechaTransaccion_I = "15-12-2020", categoria_I="salario",valor_I=2000000,  descripcion= "Quincena 2"),
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