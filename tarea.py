from numpy import NaN
import pandas as pd

data = pd.read_csv("./empleados.csv")

'''
Filtrar empleados que solo sean analistas 1
Filtrar empleados que solo sean analistas 2
Filtrar empleados en general que tengan menos de 30 años
Filtrar empleados en general que tengan mas de 50 años
¿Cuál es el promedio de salario de un analista 1?
¿Cuál es el promedio de salario de un analista 2?
Filtrar empleados cuto porcentaje de deducción sea mayor al 10%
Cambiar todos los datos nan por el valor 0
Cambiar los nan de nombres por la palabra default, los nan de cargo por el mensaje sin cargo y edad por 0
Versionar el desarrollo del taller

'''
#1
print("\n")
print("Filtrar empleados que solo sean analistas 1")
analistas1 = data[data["cargo"]== "analista1"]
print(analistas1)

#2
print("\n")
print("Filtrar empleados que solo sean analistas 2")
analistas2 = data[data["cargo"]== "analista2"]
print(analistas2)

#3
print("\n")
print("Filtrar empleados en general que tengan menos de 30 años")
menores30 = data[data["edad"]<30]
print(menores30)

#4
print("\n")
print("Filtrar empleados en general que tengan mas de 50 años")
masDe50 = data[data["edad"]>50]
print(masDe50)

#5
print("\n")
print("¿Cuál es el promedio de salario de un analista 1?")
analistas1Promedio = analistas1[["salario"]].mean()
print(round(analistas1Promedio,2))

#6
print("\n")
print("¿Cuál es el promedio de salario de un analista 2?")
analistas2Promedio = analistas2[["salario"]].mean()
print(round(analistas2Promedio,2))

#7
print("\n")
print("Filtrar empleados cuyo porcentaje de deducción sea mayor al 10%")
deduccionMayor_10 = data[data["porcentajeDeduccion"]>10]
print(deduccionMayor_10)

#8
print("\n")
print("Cambiar todos los datos nan por el valor 0")
replaceNaN = data.fillna({"cargo": 0})
print(replaceNaN)

#9
print("\n")
print("Cambiar los nan de nombres por la palabra default, los nan de cargo por el mensaje sin cargo y edad por 0")
cambiarDatos = data.fillna({"nombres": "default", "cargo": "sin cargo", "edad": 0})
print(cambiarDatos)


print("\n")
print("")