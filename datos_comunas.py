import json
import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_excel("carga-bip.xlsx", header=9, index_col=0)
print("datos: ", datos)

#corregir nombre de la columna comunas en el excel aparece como "maipu" cuando debe ser "comuna"
datos.rename(columns={"MAIPU": "COMUNA"}, inplace=True)
print("datos: ",datos)

#############################
#Generar total de datos de puntos de carga por comuna
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
