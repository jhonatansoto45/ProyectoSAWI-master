from tkinter import messagebox #Lib tkinter importamos la propiedad de mensaje por ventana o caja de texto

def show_error(message):#Metodo para definir mensaje
    messagebox.showerror(message=message, title="Error") #Definimos el tipo de mensaje que deseamos mostrar

def show_warning(message):#Metodo para definir mensaje
    messagebox.showwarning(message=message, title="Warning")#Definimos el tipo de mensaje que deseamos mostrar
