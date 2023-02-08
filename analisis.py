import pandas as pd

dataf = pd.read_csv("./empleados.csv")
filtro1= dataf.head(10)
filtro2= dataf["nombres"].head(10)
filtro3= dataf [["nombres","salario"]].tail()


#FLTRANDO POR CONDICIONES LOGICAS
filtroEdad= dataf[dataf["edad"]<30].head(20)
print(filtroEdad)


#Limpiando datos
dataLimpia=filtroEdad.dropna()
print(dataLimpia)

#reemplazando datos
tablaFiltrado=dataf.fillna({"cargo":"Desempleado","edad":"0",}).head(40)
print(tablaFiltrado)
