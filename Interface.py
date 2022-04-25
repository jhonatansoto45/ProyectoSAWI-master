import tkinter as tk # Lib parte Grafica
from utils import valid_file # Clase de utilidades
from Kismet_code import init,contarElementosLista #Clase donde se encuentra_todo lo relacionado con el archivo XML
from cuadro_dialogo import show_error, show_warning #Clase de Manejo de errores
from tkinter import filedialog #Clase de cuadro de texto o para abrir Explorador de archivos
from custom_error import custom_error #Mensaje de error
import pandas as pd #Lib para realizar DataFrames
from pandastable import Table #Lib para realizar las tablas de modo grafico


# Creamos variables en string para poder manejar en demas metodos
file_xml = ""
file_gps = ""


def cargar_xml(): #Metodo para cargar Archivo XML
    file_kismet = filedialog.askopenfilename(initialdir="/",
                                             title="Select file kismet",
                                             filetypes=(
                                                 ("XML files", "*.netxml"), ("All Files", "*.*"))
                                             )
    ext = valid_file(file_kismet)

    if ext:
        global file_xml
        file_xml = file_kismet
    else:
        show_warning("El tipo archivo no es valido")

def cargar_gps():#Metodo para cargar Archivo GPS (En produccion)
    file_kismet = filedialog.askopenfilename(initialdir="/",
                                             title="Select file kismet",
                                             filetypes=(
                                                 ("GPS files", "*.gpsxml"), ("All Files", "*.*"))
                                             )
    ext = valid_file(file_kismet)

    if ext:
        global file_gps
        file_gps = file_kismet
    else:
        show_warning("El tipo archivo no es valido")

def interface_gps(raiz): #Metodo: Ventana del Grafico GPS
    raiz.withdraw() # Cerramos la ventana principal
    ventana3 = tk.Toplevel(raiz) # Abrimos la nueva ventana
    ventana3.title("Mapa") #Titulo de la ventana
    ventana3.iconbitmap(".icon\\logo.ico") #Icono de la ventana

    frame_ventana_gps = tk.Frame(ventana3, width="699", height="400") #Creacion del Frame de la ventana con sus dimensiones
    frame_ventana_gps.pack() #Agregamos el Frame a la ventana

def interface_ventana2(raiz):
    raiz.withdraw()# Cerramos la ventana principal
    ventana2 = tk.Toplevel(raiz)# Abrimos la nueva ventana
    ventana2.title("Elige")#Titulo de la ventana
    ventana2.iconbitmap(".icon\\logo.ico")#Icono de la ventana

    frame_ventana_btn = tk.Frame(ventana2, width="699", height="400")#Creacion del Frame de la ventana con sus dimensiones
    frame_ventana_btn.pack()#Agregamos el el frame a la ventana
    tk.Label(frame_ventana_btn,
             text="Eliga las tablas que deseas vizualizar:",
             font=('sans serif', 13), bg="#F2F2F2", fg="#313540").place(x=10, y=20) #Creamos una etiqueta para que el usuario pueda eligir que ventanas ver
    try: #Validamos con una sentencia Try por si se produce algun error en el proceso
        archivo_xml = init(file_xml) #Llamamos al metodo init de Kismet_code y le mandamos como parametro la variable de cargar_xml(file_xml)
        wireless_network_ = archivo_xml["detection-run"]["wireless-network"] #Traemos la llave del xml(detection-run) y el contenido de ella(wireless-network)
        btnGrafica1 = tk.Button(ventana2, text="Ver Tabla Principal", font=(
            "sans serif", 9),bg="#4ecda7",fg="#0D0D0D", width=40, command=lambda: tablas(wireless_network_)).place(x=220,y=80)
        #Boton con su metodo para realizar las graficas llevando como parametro la variable a la que le almacenamos la llave y su contenido
        btnGrafica2 = tk.Button(ventana2, text="Ver Tabla Tipos", font=(
            "sans serif", 9),bg="#4ecda7",fg="#0D0D0D", width=40, command=lambda: print_key_type_i(wireless_network_)).place(x=220,y=120)
        # Boton con su metodo para realizar las graficas llevando como parametro la variable a la que le almacenamos la llave y su contenido
        btnGrafica3 = tk.Button(ventana2, text="Ver Tabla BSSID", font=(
            "sans serif", 9),bg="#4ecda7",fg="#0D0D0D", width=40, command=lambda: print_key_bssid_i(wireless_network_)).place(x=220,y=160)
        # Boton con su metodo para realizar las graficas llevando como parametro la variable a la que le almacenamos la llave y su contenido
        btnGrafica4 = tk.Button(ventana2, text="Ver Tabla Canales", font=(
            "sans serif", 9),bg="#4ecda7",fg="#0D0D0D", width=40, command=lambda: print_key_channel_i(wireless_network_)).place(x=220,y=200)
        # Boton con su metodo para realizar las graficas llevando como parametro la variable a la que le almacenamos la llave y su contenido
        btnGrafica5 = tk.Button(ventana2, text="Ver Tabla Fabricantes", font=(
            "sans serif", 9),bg="#4ecda7",fg="#0D0D0D", width=40, command=lambda: print_key_manuf_i(wireless_network_)).place(x=220,y=240)
        # Boton con su metodo para realizar las graficas llevando como parametro la variable a la que le almacenamos la llave y su contenido
        btnGrafica6 = tk.Button(ventana2, text="Ver Tabla Dia/Hora", font=(
            "sans serif", 9),bg="#4ecda7",fg="#0D0D0D", width=40, command=lambda: print_key_bsstimestamp_i(wireless_network_)).place(x=220,y=280)
        # Boton con su metodo para realizar las graficas llevando como parametro la variable a la que le almacenamos la llave y su contenido
    except custom_error as e: #Validacion si se produce error
        show_error(e) #Mensaje de error

def tablas(wireless_network_): #Metodo ver tabla principal
    ventana_tabla_p = tk.Toplevel() # Abrimos la nueva ventana
    ventana_tabla_p.title("Principal")#Titulo de la ventana
    ventana_tabla_p.iconbitmap(".icon\\logo.ico")#Icono de la ventana

    frame_tabla_p = tk.Frame(ventana_tabla_p, width="699", height="400")#Creacion del Frame de la ventana con sus dimensiones
    frame_tabla_p.pack(fill="both",expand="True")#Agregamos el el frame a la ventana y le ponemos que se expanda en la ventana
    panda_network = pd.DataFrame(wireless_network_) #Creacion de columnas y filas
    panda_Dataframe = Table(frame_tabla_p, dataframe=panda_network,showtoolbar=True) #Creacion de la tabla principal con sus respectivas graficas
    panda_Dataframe.show()#Visualizamos la tabla
    # try:
    #     print_key_type_i(wireless_network_)
    #     print_key_bssid_i(wireless_network_)
    #     print_key_bsstimestamp_i(wireless_network_)
    #     print_key_channel_i(wireless_network_)
    #     print_key_manuf_i(wireless_network_)
    # except key_error as e:
    #     return e

def print_key_type_i(wireless_network_): #Metodo para ver los tipos de la tabla principal y un conteo de cuantos hay del mismo nombre
    ventana_tabla_p = tk.Toplevel()# Abrimos la nueva ventana
    ventana_tabla_p.title("TIPOS")#Titulo de la ventana
    ventana_tabla_p.iconbitmap(".icon\\logo.ico")#Icono de la ventana

    mainFrame1 = tk.Frame(ventana_tabla_p,width="100", height="100")#Creacion del Frame de la ventana con sus dimensiones
    mainFrame1.pack(expand="True",fill="both")#Agregamos el el frame a la ventana y le ponemos que se expanda en la ventana
    try: #Validamos por si se llega a producir algun error
        typeCol = []  # Creamos una lista para almacear los datos de Type
        for i in wireless_network_: #Recorremos la lista
            typeCol.append(i["@type"]) #Agregamos un campo para el tipo
        typeVal = contarElementosLista(typeCol) #Llamamos al metodo contarElementosLista(utils) para que nos recorra
        df_type = pd.DataFrame([[key, typeVal[key]] for key in typeVal.keys()], columns=[
                                'Tipo', 'Cantidad'])  # Cremamos el DataFrame de Type para columnas y filas
        panda_type = Table(mainFrame1,dataframe=df_type, showtoolbar=True, showstatusbar=True) #Creamos la tabla
        panda_type.show() #Visualizamos la tabla
    except Exception: #Validacion de Error
         show_error("Fallo llave: @type") #Mensaje de error

def print_key_bssid_i(wireless_network_):#Metodo para ver los BSSID de la tabla principal y un conteo de cuantos hay del mismo nombre
    ventana_tabla_p = tk.Toplevel() #Abrimos la nueva ventana
    ventana_tabla_p.title("BSSID")#Titulo de la ventana
    ventana_tabla_p.iconbitmap(".icon\\logo.ico")#Icono de la ventana

    mainFrame2 = tk.Frame(ventana_tabla_p,width="100", height="100")#Creacion del Frame de la ventana con sus dimensiones
    mainFrame2.pack(fill="both", expand="True")#Agregamos el el frame a la ventana y le ponemos que se expanda en la ventana
    try:#Validamos por si se llega a producir algun error
        bssidCol = []# Creamos una lista para almacear los datos de BSSID
        for i in wireless_network_:#Recorremos la lista
            bssidCol.append(i["BSSID"])#Agregamos un campo para el BSSID
        bssid_table = contarElementosLista(bssidCol)#Llamamos al metodo contarElementosLista(utils) para que nos recorra
        df_bssid = pd.DataFrame([[key, bssid_table[key]] for key in bssid_table.keys()],
                                columns=['BSSID', 'Cantidad'])# Cremamos el DataFrame de BSSID para columnas y filas
        panda_bssid = Table(mainFrame2,dataframe=df_bssid,showtoolbar=True, showstatusbar=True)#Creamos la tabla
        panda_bssid.show()#Visualizamos la tabla
    except Exception:#Validacion de Error
        show_error("Fallo llave: BSSID")#Mensaje de error
#
def print_key_channel_i(wireless_network_):#Metodo para ver los Canal de la tabla principal y un conteo de cuantos hay del mismo nombre
    ventana_tabla_p = tk.Toplevel()#Abrimos la nueva ventana
    ventana_tabla_p.title("CANALES")#Titulo de la ventana
    ventana_tabla_p.iconbitmap(".icon\\logo.ico")#Icono de la ventana

    mainFrame3 = tk.Frame(ventana_tabla_p,width="100", height="100")#Creacion del Frame de la ventana con sus dimensiones
    mainFrame3.pack(fill="both",expand="True")#Agregamos el el frame a la ventana y le ponemos que se expanda en la ventana
    try:#Validamos por si se llega a producir algun error
        channelCol = []# Creamos una lista para almacear los datos de Canal
        for i in wireless_network_:#Recorremos la lista
            channelCol.append(i["channel"])#Agregamos un campo para el BSSID
        channelVal = contarElementosLista(channelCol)#Llamamos al metodo contarElementosLista(utils) para que nos recorra
        df_channel = pd.DataFrame(
            [[key, channelVal[key]] for key in channelVal.keys()], columns=['Canal', 'Cantidad'])# Cremamos el DataFrame de BSSID para columnas y filas
        panda_channel=Table(mainFrame3,dataframe=df_channel,showtoolbar=True, showstatusbar=True)#Creamos la tabla
        panda_channel.show()#Visualizamos la tabla
    except Exception:#Validacion de Error
        show_error("Fallo llave: channel")#Mensaje de error

def print_key_manuf_i(wireless_network_):#Metodo para ver los Fabricante de la tabla principal y un conteo de cuantos hay del mismo nombre
    ventana_tabla_p = tk.Toplevel()#Abrimos la nueva ventana
    ventana_tabla_p.title("FABRICANTE")#Titulo de la ventana
    ventana_tabla_p.iconbitmap(".icon\\logo.ico")#Icono de la ventana

    mainFrame4 = tk.Frame(ventana_tabla_p,width="100", height="100")#Creacion del Frame de la ventana con sus dimensiones
    mainFrame4.pack(fill="both",expand="True")#Agregamos el el frame a la ventana y le ponemos que se expanda en la ventana
    try:#Validamos por si se llega a producir algun error
        manufCol = []# Creamos una lista para almacear los datos de Fabricante
        for i in wireless_network_:#Recorremos la lista
            manufCol.append(i["manuf"])#Agregamos un campo para el Fabricante
        manufVal = contarElementosLista(manufCol)#Llamamos al metodo contarElementosLista(utils) para que nos recorra
        df_manuf = pd.DataFrame([[key, manufVal[key]]
                                 for key in manufVal.keys()], columns=['Manuf', 'Cantidad'])# Cremamos el DataFrame de Fabricante para columnas y filas
        panda_manuf = Table(mainFrame4,dataframe=df_manuf,showtoolbar=True, showstatusbar=True)#Creamos la tabla
        panda_manuf.show()#Visualizamos la tabla
    except Exception:#Validacion de Error
        show_error("Fallo llave: manuf")#Mensaje de error

def print_key_bsstimestamp_i(wireless_network_):#Metodo para ver los Dia/Hora de la tabla principal y un conteo de cuantos hay del mismo nombre
    ventana_tabla_p = tk.Toplevel()#Abrimos la nueva ventana
    ventana_tabla_p.title("DIA/HORA")#Titulo de la ventana
    ventana_tabla_p.iconbitmap(".icon\\logo.ico")#Icono de la ventana

    mainFrame5 = tk.Frame(ventana_tabla_p,width="200", height="200")#Creacion del Frame de la ventana con sus dimensiones
    mainFrame5.pack(fill="both",expand="True")#Agregamos el el frame a la ventana y le ponemos que se expanda en la ventana
    try:#Validamos por si se llega a producir algun error
        bsstimestampCol = []# Creamos una lista para almacear los datos de Dia/Hora
        for i in wireless_network_:#Recorremos la lista
            bsstimestampCol.append(i["bsstimestamp"])#Agregamos un campo para el Dia/Hora
        bsstimestampCol_table = contarElementosLista(bsstimestampCol)#Llamamos al metodo contarElementosLista(utils) para que nos recorra
        df_bsstimestampCol = pd.DataFrame([[key, bsstimestampCol_table[key]] for key in bsstimestampCol_table.keys()],
                                          columns=['Dia/hora', 'Cantidad'])# Cremamos el DataFrame de Dia/Hora para columnas y filas
        panda_bsstimestampCol = Table(mainFrame5,dataframe=df_bsstimestampCol,showtoolbar=True, showstatusbar=True)#Creamos la tabla
        panda_bsstimestampCol.show()#Visualizamos la tabla
    except Exception:#Validacion de Error
        show_error("Fallo llave: bsstimestamp")#Mensaje de error

def GUI(): #Metodo Principal: Vista Grafica

    # Ventana
    raiz = tk.Tk() #Creamos la ventana como principal
    raiz.title("Inicio")#Titulo de la ventana
    raiz.iconbitmap(".icon\\logo.ico")#Icono de la ventana(se le pone .icon\\ para que se deje grabar como ejecutable(.exe))

    # FRAME
    mainFrame = tk.Frame(raiz, width="699", height="560")#Creacion del Frame de la ventana con sus dimensiones
    # Empaquetamos el Frame
    mainFrame.pack(fill="both", expand="True")
    # Color del Frame
    mainFrame.config(bg="#F0F0F0")
    # Label
    miImagen = tk.PhotoImage(file=".img\\sawi.png") #Imagen de SAWI(se le pone .img\\ para que se deje grabar como ejecutable(.exe)
    tk.Label(mainFrame, image=miImagen).place(x=20, y=10) #Dimensiones de la imagen
    tk.Label(mainFrame, text="Software de Análisis de", bg="#F0F0F0",
             font=('sans serif',17),fg="#0D0D0D").place(x=310, y=50) #Nombre del Software
    tk.Label(mainFrame, text="Datos Wifi", bg="#F0F0F0",
             font=('sans serif', 17), fg="#0D0D0D").place(x=310, y=80)#Nombre del Software
    tk.Label(mainFrame, text="Bienvenido Usuario", bg="#F0F0F0",
             font=('sans serif', 15), fg="#0D0D0D").place(x=310, y=120) #Texto de Bienvenida
    tk.Label(mainFrame,text="Instrucciones:",font=('sans serif',15),bg="#F2F2F2",fg="#0D0D0D").place(x=119,y=220) #Texto de pasos
    tk.Label(mainFrame, text="1. Cargar archivo con extension .netxml .",font=('sans serif',12),bg="#F2F2F2",fg="#0D0D0D").place(x=119, y=260)#Texto de pasos
    tk.Label(mainFrame, text="2. Despues de cargado, oprimir el boton 'Continuar'",font=('sans serif',12),bg="#F2F2F2",fg="#0D0D0D").place(x=119, y=300)#Texto de pasos
    tk.Label(mainFrame, text="¡Empecemos!",font=('sans serif',14),bg="#F2F2F2",fg="#0D0D0D").place(x=300, y=350)#Texto de pasos
    btnAnexar = tk.Button(mainFrame, text="Cargar XML", font=(
        "sans serif", 10),bg="#4ecda7",fg="#0D0D0D", width=16, command=cargar_xml).place(x=290, y=430)#Boton para cargar o anexar el archivo XML
    # btnAnexarGPS = tk.Button(mainFrame, text="Cargar GPS", font=(
    #     "sans serif", 9),bg="#F21D56",fg="#F2F2F2", width=11, command= cargar_gps).place(x=400, y=430) #Boton para cargar o anexar el archivo GPSXML(Produccion)
    btnventana_xml = tk.Button(mainFrame, text="Continuar", font=(
        "sans serif", 10),bg="#4ecda7",fg="#0D0D0D",width=16, command=lambda: interface_ventana2(raiz)).place(x=290, y=490)#Boton para enviar el archivo al metodo(interface_ventana2)
                                                                                                                            #con un parametro de la ventana principal
    # btnventana_gps = tk.Button(mainFrame, text="Convertir GPS", font=(
    #     "sans serif", 9),bg="#F21D56",fg="#F2F2F2", width=11, command=lambda: interface_gps(raiz)).place(x=400, y=490)#Boton para enviar el archivo al metodo(interface_gps)
    #                                                                                                                             #con un parametro de la ventana principal(Produccion)
    raiz.mainloop() #Metodo para cargar la ventana principal
