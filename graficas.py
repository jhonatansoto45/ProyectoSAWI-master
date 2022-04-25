import matplotlib.pyplot as plt #Lib para realizar graficas
#NO SE UTILIZA EN EL MODO GRAFICO
def graphBarh(setsVal, sizew, sizeh, title):#Metodo para la graficas con parametros de valores. ancho,alto,titulo MODO HORIZONTAL
    fig = plt.figure(figsize=(sizew, sizeh)) #define el ancho y alto
    plt.barh(range(len(setsVal)), list(setsVal.values()), align='center', edgecolor='black') #Valores de kismet_code
    plt.yticks(range(len(setsVal)), list(setsVal.keys())) #Trae las llave de los valores
    plt.title(title)#Titulo de la grafica


def graphBar(setsVal, sizew, sizeh, title):#Metodo para la graficas con parametros de valores. ancho,alto,titulo MODO VERTICAL
    fig = plt.figure(figsize=(sizew, sizeh))#define el ancho y alto
    plt.bar(range(len(setsVal)), list(setsVal.values()), align='center', edgecolor='black')#Valores de kismet_code
    plt.xticks(range(len(setsVal)), list(setsVal.keys()))#Trae las llave de los valores
    plt.title(title)  #Titulo de la grafica