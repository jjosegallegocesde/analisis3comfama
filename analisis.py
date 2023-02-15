import pandas as pd

data = pd.read_csv("./empleados.csv")
filtro1 = data.head(10)
filtro2 = filtro1["nombres"]
filtro3 = data.tail(5)[["nombres","salario"]]
filtro4 = data.head(20).describe()

#filtro por condiciones logicas
filtroEdad = data[data["edad"] < 30].head(20)
print(filtroEdad, "\n")

#limpiando datos
dataLimpia = filtroEdad.dropna()
print(dataLimpia, "\n")


