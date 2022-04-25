import xmltodict #Lib para convertir el archivo a un json
import json #Lib para convertir el archivo a un diccionario
import pandas as pd #Lib para crea columnas y filas
from utils import contarElementosLista #Clase de utilidades
from graficas import graphBarh, graphBar #Clase para realizar Graficas
from custom_error import custom_error, key_error #Clase para manejar errores



def cargar_file(file): #Metodo para cargar y convertir el archivo
    try:
        with open(file) as fd: #Lo abrimos y asignamos un alias(fd)
            doc = xmltodict.parse(fd.read()) #Realizamos la conversion
        return doc #Retornamos el documento convertido
    except Exception: #Manejo de error
        raise custom_error("Error en convertir el archivo") #Mensaje de error
    finally:
        fd.close() #Y finalizamos cerrando el archivo para que no se presente errores


def init(path_file): #Metodo Principal de Kismet_code ya que distribuimos_todo desde aqui
    doc_xml = cargar_file(path_file) #Llamamos el metodo cargar_file como parametro la variable de Interface para ser convertida
    json_doc = json.loads(json.dumps(doc_xml)) #Convertimos a DICT
    return json_doc #Retornamos el documento convertido
    try: #Validacion de Errores
        run(json_doc) #Llamamos el metodo run y enviamos como paramentro el documento convertido(json_doc)

    except key_error as e:#Manejo de error
        return e #Retornamos el error


def run(json_doc):#Metodo para la llamada de otro metodo por si se produce algun error
    try:#Validacion de Errores
        load_key_dataframe(json_doc)#Llamamos el metodo load_key_dataframe y enviamos como paramentro el documento convertido(json_doc)
    except key_error as e:#Manejo de error
        return e #Retornamos el error


def load_key_dataframe(json_doc): #Metodo de asignacion de llaves y contenido
    wireless_network = json_doc["detection-run"]["wireless-network"] #Almacenamos la llave y su respectivo contenido
    panda_network = pd.DataFrame(wireless_network)#Creamos las columnas y filas
    try:#Validacion de Errores
        print_key_type(wireless_network) #metodo para realizar cada tabla y como parametro su llave y contenido para acceder a ella
        print_key_bssid(wireless_network)#metodo para realizar cada tabla y como parametro su llave y contenido para acceder a ella
        print_key_bsstimestamp(wireless_network)#metodo para realizar cada tabla y como parametro su llave y contenido para acceder a ella
        print_key_channel(wireless_network)#metodo para realizar cada tabla y como parametro su llave y contenido para acceder a ella
        print_key_manuf(wireless_network)#metodo para realizar cada tabla y como parametro su llave y contenido para acceder a ella
    except key_error as e:#Manejo de error
        return e#Retornamos el error


def print_key_type(wireless_network): #Metodo para realizar tablas y graficas de Tipo
    try:
        typeCol = []  # Creamos una lista para almacear los datos de type
        for i in wireless_network: #Recorremos la lista
            typeCol.append(i["@type"])#Agregamos un campo para el tipo
        typeVal = contarElementosLista(typeCol)#Llamamos al metodo contarElementosLista(utils) para que nos recorra
        df_type = pd.DataFrame([[key, typeVal[key]] for key in typeVal.keys()], columns=[
                               'Tipo', 'Cantidad'])  # Cremamos el DataFrame de Manuf
        panda_type = pd.DataFrame([[key, df_type[key]] for key in df_type.keys()],
                                columns=['TIPO', 'Cantidad']) # Cremamos el DataFrame de Type para columnas y filas
        panda_type.show() #Visalizamos las columnas y filas
    except Exception:#Manejo de error
        raise key_error("Fallo llave: @type") #Mensaje de error


def print_key_bssid(wireless_network): #Metodo para realizar tablas y graficas de BSSID
    try:
        bssidCol = []# Creamos una lista para almacear los datos de BSSID
        for i in wireless_network:#Recorremos la lista
            bssidCol.append(i["BSSID"])#Agregamos un campo para el BSSID
        bssid_table = contarElementosLista(bssidCol)#Llamamos al metodo contarElementosLista(utils) para que nos recorra
        df_bssid = pd.DataFrame([[key, bssid_table[key]] for key in bssid_table.keys()],
                                columns=['BSSID', 'Cantidad'])# Cremamos el DataFrame de BSSID para columnas y filas
        df_bssid #Visalizamos las columnas y filas
    except Exception:#Manejo de error
        raise key_error("Fallo llave: BSSID")#Mensaje de error


def print_key_bsstimestamp(wireless_network, ): #Metodo para realizar tablas y graficas de Dia/Hora
    try:
        bsstimestampCol = []# Creamos una lista para almacear los datos de Dia/Hora
        for i in wireless_network:#Recorremos la lista
            bsstimestampCol.append(i["bsstimestamp"])#Agregamos un campo para el Dia/Hora
        bsstimestampCol_table = contarElementosLista(bsstimestampCol)#Llamamos al metodo contarElementosLista(utils) para que nos recorra
        df_bsstimestampCol = pd.DataFrame([[key, bsstimestampCol_table[key]] for key in bsstimestampCol_table.keys()],
                                          columns=['Dia/hora', 'Cantidad'])# Cremamos el DataFrame de Dia/Hora para columnas y filas
        df_bsstimestampCol#Visalizamos las columnas y filas
    except Exception:#Manejo de error
        raise key_error("Fallo llave: bsstimestamp")#Mensaje de error


def print_key_channel(wireless_network):#Metodo para realizar tablas y graficas de Canal
    try:
        channelCol = []# Creamos una lista para almacear los datos de Canal
        for i in wireless_network:#Recorremos la lista
            channelCol.append(i["channel"])#Agregamos un campo para el Canal
        channelVal = contarElementosLista(channelCol)#Llamamos al metodo contarElementosLista(utils) para que nos recorra
        df_channel = pd.DataFrame(
            [[key, channelVal[key]] for key in channelVal.keys()], columns=['Canal', 'Cantidad'])# Cremamos el DataFrame de Canal para columnas y filas
        df_channel#Visalizamos las columnas y filas
    except Exception:#Manejo de error
        raise key_error("Fallo llave: channel")#Mensaje de error


def print_key_manuf(wireless_network):#Metodo para realizar tablas y graficas de Fabricante
    try:
        manufCol = []# Creamos una lista para almacear los datos de Fabricante
        for i in wireless_network:#Recorremos la lista
            manufCol.append(i["manuf"])#Agregamos un campo para el Fabricante
        manufVal = contarElementosLista(manufCol)#Llamamos al metodo contarElementosLista(utils) para que nos recorra
        df_manuf = pd.DataFrame([[key, manufVal[key]]
                                 for key in manufVal.keys()], columns=['Manuf', 'Cantidad'])# Cremamos el DataFrame de Fabricante para columnas y filas
        df_manuf#Visalizamos las columnas y filas
    except Exception:#Manejo de error
        raise key_error("Fallo llave: manuf")#Mensaje de error


    #ESTAS SON LAS LLAMADAS DE GRAFICAS PERO NO LA UTILIZAMOS EN LA PARTE GRAFICA
    #
    # graphBarh(manufVal, 10, 7, "Manufactura")
    # graphBar(manufVal, 20, 7, "Manufactura")


# Metodo: Ubicar cuantas BSSID hay con la misma MAC
# def conteo_BSSID(bssid):
#     print(len(panda_network[panda_network["BSSID"].str.contains(bssid)]))
# conteo_BSSID(bssid = input("Digite la MAC: "))

# Metodo: Ubicar cuantas Manuf hay con el mismo nombre
# def conteo_Manuf(manuf):
#         print(len(panda_network[panda_network["manuf"].str.contains(manuf)]))
# conteo_Manuf(manuf = input("Digite el nombre del fabricante: "))
