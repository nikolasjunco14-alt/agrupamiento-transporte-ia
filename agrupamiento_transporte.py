import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1. Cargar el dataset
datos = pd.read_csv("datos_transporte.csv")

print("Datos cargados correctamente:")
print(datos)
print()

# 2. Seleccionar las variables para el agrupamiento
variables = [
    "pasajeros_hora",
    "tiempo_espera",
    "ocupacion",
    "transbordos"
]

X = datos[variables]

# 3. Estandarizar los datos
escalador = StandardScaler()
X_escalado = escalador.fit_transform(X)

# 4. Crear el modelo K-Means
modelo = KMeans(n_clusters=3, random_state=42, n_init=10)

# 5. Entrenar el modelo
datos["grupo"] = modelo.fit_predict(X_escalado)

# 6. Mostrar los resultados
print("Agrupamiento de las estaciones:")
print(datos[["estacion", "grupo"]])
print()

# 7. Mostrar las estaciones de cada grupo
for grupo in sorted(datos["grupo"].unique()):
    print(f"Grupo {grupo}:")
    estaciones = datos[datos["grupo"] == grupo]["estacion"]
    for estacion in estaciones:
        print("-", estacion)
    print()

# 8. Mostrar los centros de los grupos
centros = escalador.inverse_transform(modelo.cluster_centers_)
centros_df = pd.DataFrame(centros, columns=variables)

print("Características promedio de cada grupo:")
print(centros_df)

# 9. Crear una gráfica
plt.figure(figsize=(10, 6))

plt.scatter(
    datos["pasajeros_hora"],
    datos["ocupacion"],
    c=datos["grupo"],
    s=100
)

for _, fila in datos.iterrows():
    plt.annotate(
        fila["estacion"],
        (fila["pasajeros_hora"], fila["ocupacion"]),
        xytext=(5, 5),
        textcoords="offset points"
    )

plt.xlabel("Pasajeros por hora")
plt.ylabel("Ocupación (%)")
plt.title("Agrupamiento de estaciones de transporte con K-Means")
plt.grid(True)
plt.show()