import os #Lib para abrir explorador de archivos Windows

def  contarElementosLista(lista): #Creamos un metodo para recorrer y almacenar la llave de todos los metodos
    return {i:lista.count(i) for i in lista} #Recorremos y retornamos en i

def from_list(f, l): #Ciclo para recorrer GPS(Produccion)
    return[f(y) for y in l]

def valid_file(path_file): #Metodo para validar extensiones
    extensiones = [".netxml", ".gpsxml"] #Agregamos las extensiones que soporta el software
    _,ext=os.path.splitext(path_file)
    for i in extensiones:
        if i == ext:#Validamos si son iguales con las extensiones
            return True
    return False

