from pydantic import BaseModel


class User(BaseModel):
    id: int
    fechaCreacion:str
    Nombre: str
    NUIP: str
    Uemail: str

 
usuarios_DB= {
    1: User  (id=1, fechaCreacion = "01-11-2020", nombre="Edwin", NUIP="333333333", Uemail="edwin@mintic.co"),
    2: User  (id=2, fechaCreacion = "08-11-2020", nombre="Daniel", NUIP="44444444", Uemail="edwin@mintic.co"),
    3: User  (id=3, fechaCreacion = "15-12-2020", Nombre="Fernando", NUIP="55555555", Uemail="edwin@mintic.co"),
}


def obtener_Usuarios():
    #haga lo que tenga que hacer para conectarse a la base de datos y obtner todas las ordenes
    lista_usuarios=[]
    for u in usuarios_DB:
        lista_usuarios.append(usuarios_DB[u])
    return lista_usuarios


def agregar_usuario(usuarios_N: User):
    if usuarios_N.id in usuarios_DB:
        return False
    else:
        usuarios_DB[usuarios_N.id]= usuarios_N
        return True

