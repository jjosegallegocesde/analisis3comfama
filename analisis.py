import pandas as pd

data=pd.read_csv("./empleados.csv")
filtroHead=data.head(10)
filtro2=data["nombres"].head(10)
filtro3=data [["nombres", "salario"]].tail(5)
filtro4=data.head(20).describe()

#FILTRANDO POR CONDICIONES LOGICAS
filtroEdad=data[data["edad"]<30].head(20)
print(filtroEdad)

#LIMPIANDO DATOS
dataLimpia=filtroEdad.dropna()
print("\n")
print(dataLimpia)
