# Agrupamiento de Estaciones de Transporte con K-Means

## Descripción

Este proyecto aplica una técnica de aprendizaje no supervisado para identificar grupos de estaciones de transporte con características similares.

Se utiliza el algoritmo K-Means sobre un conjunto de datos académico compuesto por 10 estaciones. Las variables utilizadas son pasajeros por hora, tiempo de espera, porcentaje de ocupación y cantidad de transbordos.

Los datos utilizados son una muestra sintética creada con fines académicos, debido a que no se cuenta con una fuente real que contenga todas las variables requeridas para el ejercicio.

## Objetivo

Aplicar el algoritmo K-Means para agrupar estaciones de transporte según características similares y analizar los resultados obtenidos.

## Archivos del proyecto

- `datos_transporte.csv`: conjunto de datos utilizado para el análisis.
- `agrupamiento_transporte.py`: código Python que realiza el agrupamiento mediante K-Means.
- `Descripcion_datos_transporte.pdf`: descripción de las variables y características del conjunto de datos.
- `Pruebas_agrupamiento_transporte.pdf`: documento con las pruebas realizadas al sistema.

## Variables utilizadas

- **Pasajeros por hora:** cantidad estimada de pasajeros durante una hora.
- **Tiempo de espera:** tiempo promedio de espera en minutos.
- **Ocupación:** porcentaje estimado de ocupación.
- **Transbordos:** cantidad promedio de transbordos.

## Tecnologías utilizadas

- Python 3
- Pandas
- Scikit-learn
- Matplotlib

## Metodología

Primero se cargan los datos mediante Pandas. Luego se seleccionan las variables utilizadas para el agrupamiento y se estandarizan mediante `StandardScaler`.

Posteriormente se aplica el algoritmo K-Means con tres grupos. Finalmente, se muestran las estaciones pertenecientes a cada grupo y se genera una gráfica para visualizar los resultados.

## Resultados

El algoritmo K-Means agrupó las 10 estaciones en tres grupos:

- **Grupo 0:** Portal Norte, Portal El Dorado y Portal Americas.
- **Grupo 1:** Toberin, Calle 100, Calle 72, Calle 63 y Calle 26.
- **Grupo 2:** Calle 53 y Calle 45.

El Grupo 0 presentó los valores promedio más altos de pasajeros, ocupación y transbordos. El Grupo 1 presentó características intermedias y el Grupo 2 presentó los valores promedio más bajos.

Los números de los grupos son identificadores asignados por el algoritmo. La interpretación de cada grupo se realizó posteriormente a partir de sus características promedio.

## Pruebas

Se realizaron pruebas para verificar:

1. La carga correcta del conjunto de datos.
2. La generación de los tres grupos.
3. La repetibilidad de los resultados.
4. La asignación de todas las estaciones a un grupo.

Las pruebas fueron exitosas.

## Ejecución

Para instalar las librerías necesarias:

```bash
pip install pandas scikit-learn matplotlib

Para ejecutar el programa:

python agrupamiento_transporte.py

Al ejecutar el programa se muestran los grupos de estaciones obtenidos mediante K-Means y una gráfica con los resultados.
Datos
El conjunto de datos utilizado es una muestra sintética elaborada con fines académicos y no representa datos oficiales del sistema de transporte.
Autor
Nicolás Junco