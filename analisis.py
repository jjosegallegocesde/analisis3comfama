import pandas as pd

data = pd.read_csv("./empleados.csv")

filtro1 = data.head(10)
#print(filtro1)

print("\n")

filtroNombres = filtro1[["nombres"]]
#print(filtroNombres)

print("\n")

nom_sal = data[["nombres","salario"]].tail(5)
#print(nom_sal)

print("\n")

estad = data.head(20).describe()
#print(round(estad,2))

print("\n")

#filtrando por condiciones lógicas

filtro_edad = data[data["edad"] <30].head(20)
print(filtro_edad)

print("\n")
#limpieza de datos
clear_data = filtro_edad.dropna()
print(clear_data)

print("\n")
filtro_edad ["cargo"] = filtro_edad["cargo"].replace(["analista2"],"practicante comfama")
print(filtro_edad)
