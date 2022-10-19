import pandas as pd 
#el comando header hace referencia a que desde esa columna se entregara la info, esto sirve
#para cuando existen filas sin info al inicio del archivo excel.
carga = pd.read_excel("carga-bip.xlsx", header=9)

#Para poder ver un resumen con una x cantidad de filas se utiliza el siguiente comando
#print(carga.head(12))

print("carga en terminal",carga)
carga["COMUNA"] = carga.loc[ : ,["MAIPU"]]
comuna = carga[ carga["MAIPU"]=="RENCA" ]

print(comuna)
renca = {"RENCA":59}
print(renca)
comuna.to_json("renca.json")

comuna = carga[ carga["MAIPU"]=="RENCA", "ESTACION CENTRAL", "VITACURA" ]

#para visualizar datos solamente de algunas columnas, se debe realizar otro procedimiento
cod_nom = comuna.loc[ : , ["CODIGO", "NOMBRE FANTASIA"]]
print("cod_nom", cod_nom)

print("cod_com con COMUNA: ",cod_nom)

#crear columna con dato predefinido
cod_nom["ESTACIONAMIENTO"] = "NO"
cod_nom["ES PAR"] = comuna.loc[ : , ["CODIGO"]]
print("cod_nom con dos columnas mas", cod_nom)

cod_nom["ES PAR"] = cod_nom["ES PAR"].apply(lambda x: "SI" if (int(x) % 2 == 0) else "NO")
print("cod_nom con ES PAR modificado", cod_nom)
