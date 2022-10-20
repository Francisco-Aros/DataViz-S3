import json
import pandas as pd
import matplotlib.pyplot as plt
#para leer excel debemos importarlo con la siguiente linea de código. "Header significa que se comienza a leer desde la filaX", Index siginifca que la columa 0 es mi indice
datos = pd.read_excel("carga-bip.xlsx", header=9, index_col=0)
print("datos: ", datos)

#corregir nombre de la columna comunas en el excel aparece como "maipu" cuando debe ser "comuna"
datos.rename(columns={"MAIPU": "COMUNA"}, inplace=True)
print("datos: ",datos)

#############################
##Generar total de datos de puntos de carga por comuna##
renca= datos[ datos["COMUNA"]=="RENCA" ]

#Obtener Filas y Columnas de los datos.
#Se genera un Numpy y luego se añade la función "shape".
renca_filas, renca_columnas = renca.to_numpy().shape

#se pasa por el contador de filas a nuestro Diccionario
puntos_de_carga = {
    "RENCA": renca_filas
}

#Luego guardamos usando la librería json
#indicamos su codifciación utf-8
#Y que mantenga una identificación de 2 caracteres
with open("puntos-carga.json", "w", encoding="utf-8") as j:
    j.write( json.dumps(puntos_de_carga, indent=2) )

###############################
###Generar csv con puntos de carga para 3 comunas###
#Se debe filtrar datos de 3 comunas

datos_tres_comunas = [
    datos[ datos["COMUNA"]=="RENCA" ] ,
    datos[ datos["COMUNA"]=="LA FLORIDA" ]
]
datos_tres_comunas.append(datos[ datos["COMUNA"] == "ÑUÑOA"])
#Metodo append lo que realiza es agregar un elemento al final de la lista(se pueden usar los dos metodos)
#Los elementos obtenidos anteriormente, se generan de forma separada, por lo cual se deben unir en un solo elemento
#Para lo cual primeramente debemos corregir el nombre de la columna correspondiente a la dirección 
#posteriormente se crea un archivo CSV
pd.concat(datos_tres_comunas).rename( columns={"CERRO BLANCO 625": "DIRECCION"} ).to_csv("datos-tres-comunas.csv", encoding="UTF-8")

########################################################
###Generar valores ficticios para horario referencial###
horario = datos.index
horarios = []
for h in horario:
    # se evalua una condición, en este caso que el CODIGO sea par
    if (h%2==0):
        horarios.append("09:00 - 13:00, 14:00 - 19:00")
    else:
        horarios.append("08:30 - 12:30, 13:30 - 18:30")
        
#Otra forma de escribirlo es:
# horarios=["09:00 - 13:00, 14:00 - 19:00" if(h % 2 == 0) else "08:30 - 12:30, 13:30 -18:00" for h in horario]

#con la lsita de horarios completa, se asigna a la columna de datos
datos["HORARIO REFERENCIAL"] = horarios
print(datos)

################################################################
###CREAR GRAFICO CON LOS PUNTOS DE CARGA POR CADA HORARIO#######
#agrupar por cada columna los horarios requeridos
horario_ref = datos.groupby(["HORARIO REFERENCIAL"])
#Se crea la referencia al conteo por la columna de horario
horario_agrupado = horario_ref["HORARIO REFERENCIAL"].count()
#Se deben cerrar todos los ploteo anteriores
plt.close("all")
#Generar el espacio de graficación
plt.figure()
#Se debe genera un ploteo de los datos agrupados y contados
horario_agrupado.plot()
#Ahora se debe mostrar el gráfico desarrollado
plt.show()
#ahora se deben mostrar los datos que se graficaron
print(horario_agrupado)
