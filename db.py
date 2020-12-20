from pydantic import BaseModel


class Transaccion(BaseModel):
    id: int
    fechaTransaccion:str
    categoria: str
    valor: float
    formaPago:str
    descripcion: str

"""

class Ingreso(BaseModel):
    fecha: str
    categoria_ingreso: str
    valor: float
    descripcion: str
"""
    
transaciones = {
    1: Transaccion (id=1 , fechaTransaccion = "20-11-2020", categoria="Alimentación",valor=200000, formaPago="tarjeta_débito", descripcion= "Almuerzo restaurante Carne de Res"),
    2: Transaccion (id=2 , fechaTransaccion = "22-11-2020", categoria="Vestuario",valor=980000, formaPago="tajerta_crédito", descripcion= "Uniformes dotación trabajadores"),
    3: Transaccion (id=3 , fechaTransaccion = "01-12-2020", categoria="Viveres",valor=600000, formaPago="efectivo", descripcion= "Mercado mensual familiar"),
}

"""

ingresos = {
        1: Egreso(id=1, fecha="07-12-2020", categoria_ingreso="salario", valor=1500000, descripcion="prima"),
        2: Egreso(id=2, fecha="08-12-2020", categoria_ingreso="arrendamiento", valor=500000,  descripcion="casa en la guajira"),
        3: Egreso(id=3, fecha="15-12-2020", categoria_ingreso="salario", valor=1200000,  descripcion="quincena 1 de diciembre"),
        4: Egreso(id=4, fecha="16-12-2020", categoria_ingreso="otros", valor=30000000,  descripcion="venta de carro")
}
"""

def obtener_Transaciones():
    #haga lo que tenga que hacer para conectarse a la base de datos y obtner todas las ordenes
    lista_transacciones=[]

    for e in transaciones:
        lista_transacciones.append(transaciones[e])
    return lista_transacciones


def agregar_transaccion(transaccion: Transaccion):
    if transaccion.id in transaciones:
        return False
    else:
        transaciones[transaccion.id]= transaccion
        return True



"""

def obtener_ingresos():
    #haga lo que tenga que hacer para conectarse a la base de datos
    lista_ingresos = []
    for i in ingresos:
        lista_ingresos.append(egresos[i])
    return lista_ingresos

def crear_ingresos(ingreso: Ingreso):
    if ingreso.id in ingresos:
        return False
    else:
        ingresos[ingreso.id] = ingreso
        return True
"""