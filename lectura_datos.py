from tkinter.messagebox import NO
import pandas as pd 
#el comando header ahce referencia a que desde esa columna se entregara la info, esto sirve
#para cuando existen filas sin info al inicio del archivo excel.
carga = pd.read_excel("carga-bip.xlsx", header=9)

#Para poder ver un resumen con una x cantidad de filas se utiliza el siguiente comando
print(carga.head(8))

print("carga en terminal",carga)
comuna = carga[ carga["MAIPU"]=="RENCA" ]
print(comuna.items())
renca = {"RENCA":59}
print(renca)

#para visualizar datos solamente de algunas columnas, se debe realizar otro procedimiento
cod_nom = comuna.loc[ : , ["CODIGO", "NOMBRE FANTASIA"]]
print("cod_nom", cod_nom)

#crear columna con dato predefinido
cod_nom["ESTACIONAMIENTO"] = NO
cod_nom["ES PAR"] = comuna.loc[ : , ["CODIGO"]]
print("cod_nom con dos columnas mas", cod_nom)
