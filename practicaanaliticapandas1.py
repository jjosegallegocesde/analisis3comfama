import pandas as pd

dataframe = pd.read_csv("./empleados.csv")
print(dataframe)
analistas1 = dataframe[dataframe["cargo"] == "analista1"]
print(f"{analistas1}\n")
analistas2 = dataframe[dataframe["cargo"] == "analista2"]
print(f"{analistas2}\n")
menor30 = dataframe[dataframe["edad"] < 30]
print(f"{menor30}\n")
mayor50 = dataframe[dataframe["edad"] > 50]
print(f"{mayor50}\n")
salariomedio1 = analistas1["salario"].mean()
print(f"El salario promedio de los analistas1 es: {round(salariomedio1, 2)}\n")
salariomedio2 = analistas2["salario"].mean()
print(f"El salario promedio de los analistas2 es: {round(salariomedio2, 2)}\n")
porcentaje10 = dataframe[dataframe["porcentajeDeduccion"] > 10]
print(f"{porcentaje10}\n")
notnan = dataframe.fillna(0)
print(f"{notnan}\n")
notnan2 = dataframe.fillna({"nombres": "default", "cargo": "sin cargo", "edad": 0})
print(f"{notnan2}\n")