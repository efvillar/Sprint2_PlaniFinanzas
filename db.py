from pydantic import BaseModel

class Egreso(BaseModel):
    id: int
    fecha: str
    categoria_egreso: str
    valor: float
    forma_pago: str
    descripcion: str

class Ingreso(BaseModel):
    fecha: str
    categoria_ingreso: str
    valor: float
    descripcion: str
    
egresos = {
    1: Egreso(id=1, fecha="08-12-2020", categoria_egreso="vestuario", valor=60000, forma_pago="efectivo", descripcion="camisa verde"),
    2: Egreso(id=2, fecha="08-12-2020", categoria_egreso="transporte", valor=10000, forma_pago="efectivo", descripcion="taxi al trabajo"),
    3: Egreso(id=3, fecha="09-12-2020", categoria_egreso="alimentacion", valor=90000, forma_pago="tarjeta de credito", descripcion="restaurante arabe"),
    4: Egreso(id=4, fecha="12-12-2020", categoria_egreso="educacion", valor=800000, forma_pago="tarjeta de credito", descripcion="colegio"),
    5: Egreso(id=5, fecha="18-12-2020", categoria_egreso="alimentacion", valor=190000, forma_pago="debido", descripcion="rappi")
}

ingresos = {
        1: Egreso(id=1, fecha="07-12-2020", categoria_ingreso="salario", valor=1500000, descripcion="prima"),
        2: Egreso(id=2, fecha="08-12-2020", categoria_ingreso="arrendamiento", valor=500000,  descripcion="casa en la guajira"),
        3: Egreso(id=3, fecha="15-12-2020", categoria_ingreso="salario", valor=1200000,  descripcion="quincena 1 de diciembre"),
        4: Egreso(id=4, fecha="16-12-2020", categoria_ingreso="otros", valor=30000000,  descripcion="venta de carro")

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