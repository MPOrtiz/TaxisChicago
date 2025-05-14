# Zuber Analysis 
Overview:

As an analyst for Zuber, a new ride-sharing company launching in Chicago, my task is to identify patterns in the available data. The goal is to gain insights into passenger preferences and understand how external factors influence ride frequency.

Through database analysis, I will examine competitor data and test a hypothesis on the impact of weather conditions on ride demand. This project aims to uncover key factors that drive user behavior, providing actionable insights to optimize Zuber's operations and customer experience.

Introducción: 

Como analista para Zuber, una nueva empresa de viajes compartidos que se lanza en Chicago, mi tarea es identificar patrones en los datos disponibles. El objetivo es obtener información sobre las preferencias de los pasajeros y entender cómo los factores externos influyen en la frecuencia de los viajes.

A través del análisis de bases de datos, examinaré los datos de los competidores y pondré a prueba una hipótesis sobre el impacto de las condiciones climáticas en la demanda de viajes. Este proyecto tiene como fin descubrir los factores clave que impulsan el comportamiento de los usuarios, proporcionando información útil para optimizar las operaciones y la experiencia del cliente en Zuber.
PLAN DE TRABAJO:

1. Limpieza de datos

2. Analisis de datos

3. Pruebas de Hipótesis

4. Conclusiones
## TOC:
* [Previsualización de la información](#Inicializacion)
* [Preparación de los datos](#Preprocesamiento)
* [Análisis de la información](#Analysis)
* [Pruebas de Hipotesis](#Hypothesis)
* [Conclusiones del análisis](#Conclusion)

Martha, excelente trabajo agregando una introducción al proyecto donde se especifiquen claramente los objetivos y se explique el propósito del mismo. Es esencial hacer esto para establecer las bases del proyecto y aclarar lo que buscamos alcanzar. Con la introducción, queda de manera clarar el análisis que desarrollaremos en el proyecto y cómo lo pretendemos abordar. Además, esto lo complementaste con una tabla de contenidos para guiarnos sobre los diferentes apartados</div>
# Inicicializacion
import pandas as pd
import numpy as np
import math
import seaborn as sns
from matplotlib import pyplot as plt
from scipy import stats as st

1. Imported Data
1.1 Data Companies
df_zuber=pd.read_csv('/datasets/project_sql_result_01.csv')
print()
print('Data Info')
print(df_zuber.info())
print()
print('Info Head')
print(df_zuber.head())
Se visualiza la información y el encabezado de data frame que contiene la información de las empresas que realizan los viajes
1.2 Data Trips
df_trips=pd.read_csv('/datasets/project_sql_result_04.csv')
print()
print('Data Info')
print(df_trips.info())
print()
print('Data Head')
print(df_trips.head())

Recuerda que como buena prática es recomendable cargar todas las bases de datos en una misma celda. Es por ello que te recomiendo cargar la base faltante en esta misma celda..</div>

Se visualiza la información y el encabezado de data frame que contiene la información de los viajes que realizan los viajes
# Preprocesamiento
2.1 NULL Values
print('NULL Values Companies')
print(df_zuber.isna().sum())
print()

print('NULL Values Trips')
print(df_zuber.isna().sum())

No se encuentran valores Nulos en ambos data frames
2.2 Duplicated Values
print('Duplicated values in Company')
print(df_zuber.duplicated().sum())
print()

print('Duplicated values in Trips')
print(df_trips.duplicated().sum())
No se encuentran valores duplicados en ambos data frames

Se continua a la fase del análisis
<div class="alert alert-block alert-success">

<b>Comentario del revisor</b> <a class="tocSkip"></a>

Martha, muy buen trabajo con el análisis de registros duplicados! Como aprendiste en cursos anteriores esto es un paso fundamental dado que puede sesgar nuestros resultados.</div>
# Analysis
1.1 Top 5 companies
df_topcompanies=df_zuber.groupby(['company_name'])['trips_amount'].sum().sort_values(ascending=False).reset_index()
df_topcompanies=df_topcompanies.head(10)
print(df_topcompanies)
print()

df_topcompanies_stats=df_topcompanies.describe()
print(df_topcompanies_stats)

print('Top Companies')
plt.figure(figsize=(15,8))
plt.bar(df_topcompanies['company_name'],df_topcompanies['trips_amount'],label='Top Companies',align='center',alpha=0.7)
plt.title('Top Companies')
plt.xlabel('Companies')
plt.ylabel('Trips')
plt.show()
<div class="alert alert-block alert-success">

<b>Comentario del revisor</b> <a class="tocSkip"></a>

Excelente trabajo con el desarrollo de este análisis, muestras de manera clara cuales son los 10 principales barrios en términos de finalización del recorrido
    </div>
Conclusiones: Se registran los top 10 de empresas de Taxis que realizaron viajes en el periodo de tiempo acordado, el promedio de viajes en el top 10 es de 9,927
1.2 Top destinations
df_toptrips=df_trips.groupby(['dropoff_location_name'])['average_trips'].sum().sort_values(ascending=False).reset_index()
df_toptrips=df_toptrips.head(10)
print(df_toptrips)
print()

df_toptrips_stats=df_toptrips.describe()
print(df_toptrips_stats)

print('Top Destination')
plt.figure(figsize=(12,10))
plt.xlabel('Companies')
plt.ylabel('Destinations')
plt.title('Top Destination')
plt.bar(df_toptrips['dropoff_location_name'],df_toptrips['average_trips'],align='center',alpha=0.7)
plt.show()

Conclusiones: Top 10 de destinos de viaje, el tiempo aproximado por destino es de 4324. Hay una significativa diferencia entre el top 4 y los otros 6 destinos principales 
# Hypothesis
Prueba de Hipotesis La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare cambia los sábados lluviosos.
Hipotesis Nula: La duración de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare no cambia los sabados lluviosos

Hipotesis Alternativa: La duración de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare cambia los sabados lluviosos

P value: 0.05
1.1 Imported Data
df_ht=pd.read_csv('/datasets/project_sql_result_07.csv')
print(df_ht)
2.1 Null and Duplicated Values
print('NULL Values',df_ht.isna().sum())
print()

No se encuentran valores Nulos
print('Duplicated Values',df_ht.duplicated().sum())
Se encuentran valores duplicados, en la siguiente fase se eliminarán
Clean Values
df_ht=df_ht.drop_duplicates()
print(df_ht)
#Date Format
df_ht['start_ts']=pd.to_datetime(df_ht['start_ts'])
df_ht_saturday=df_ht[df_ht['start_ts'].dt.weekday==5]
print(df_ht_saturday)
2.2 Box Plot GOOD Weather VS BAD Weather
print('Trips Duration in Good and Bad Weather')
plt.figure(figsize=(6, 6))
plt.title('Trips Duration in Good and Bad Weather')
sns.boxplot(data=df_ht_saturday, x='duration_seconds', y='weather_conditions', orient='h')
plt.show()
Se visualizan diferentes Outliers, se eliminaran en el siguiente paso
df_ht_saturday_stats=df_ht_saturday.describe()
print(df_ht_saturday_stats)
#Quartile
Q1=1440
Q3=2584

IQR=Q3-Q1
print('IQR: ',IQR)
print()
upper_limit=Q3+(1.5*IQR)
lower_limit=Q1-(1.5*IQR)
print('Upper Limit',upper_limit)
print('Lower Limit',lower_limit)
data_no_outliers=df_ht_saturday.query('duration_seconds <= @upper_limit')
data_no_outliers=data_no_outliers.query('duration_seconds >= @lower_limit')
#Data without outliers
print('Trips Duration in Good and Bad Weather')
plt.figure(figsize=(6, 6))
plt.title('Trips Duration in Good and Bad Weather')
sns.boxplot(data=data_no_outliers,x='duration_seconds', y='weather_conditions', orient='h')
plt.show()

Se visualiza que en condiciones malas del clima la duración de los viajes en el primer cuartil se encuentran desplazados hacia el lado derecha de la gráfica, por lo cual nos indica que podríamos pensar que duran más tiempo. Sin embargo, es importante observar que los bigotes del límite superior del grafico se encuentran en una distancia similar en ambas condiciones, una variación similar. La caja de Buena condición del clima se observa con mayor variación.

2.3 Variance Test
# Prueba de levene
# Hipótesis nula: Las varianzas de los grupos son iguales.
# Hipótesis alternativa: Al menos uno de los grupos tiene una variable diferente.

data_no_outliers_good=data_no_outliers[data_no_outliers['weather_conditions']=='Good']
data_no_outliers_bad=data_no_outliers[data_no_outliers['weather_conditions']=='Bad']

print('Stats good Weather')
print()
print(data_no_outliers_good.describe())
print('Stats Bad Weather')
print()
print(data_no_outliers_bad.describe())

# Prueba de Levene para igualdad de varianzas
pvalue_levene = st.levene(data_no_outliers_good['duration_seconds'],data_no_outliers_bad['duration_seconds'])

# Imprimir resultados de la prueba de Levene
print()
print('Statistic',pvalue_levene.statistic)
print('P value', pvalue_levene.pvalue)
print()

if pvalue_levene.pvalue < 0.05:
    print('Se rechaza la hipótesis nula: Al menos uno de los grupos tiene una variable diferente')
else:
    print('No podemos rechazar la hipótesis nula : Las varianzas de los grupos son iguales')

2.4 Hypothesis Test
alpha=0.05
ttest_weathercondition = st.ttest_ind(data_no_outliers_good['duration_seconds'],data_no_outliers_bad['duration_seconds'], equal_var=True)

print("P value", ttest_weathercondition.pvalue)

if ttest_weathercondition.pvalue < alpha:
    print("Rechazamos la hipotesis nula")
else:
    print("No podemos rechazar la hipotesis nula")
    
print()

La duración promedio de los viajes no son iguales desde el Loop hasta el Aeropuerto Internacional O'Hare cambia los sábados lluviosos.

# Conclusion

Data Frame Companies: Es importante identificar a nuestros aliados estrategicos en la ejecucción de nuestros viajes para ofrecerles un plan estratégico en el cual alcancemos mayores viajes a un menor costo. Identificando horas picos y salidas de viaje.


Data Frame Trips: Tenemos identificado a nuestro Top 10 de destinos, sin embargo creo importante que se grafique topograficamente para identificar cual es el mejor punto estrategico para que la distancia de solicitud y arribo del automovil sea el menor, por lo cual beneficia a reducir costos operativos. 

Data Frame días lluviosos: En días lluviosos los viajes duran mayor tiempo que en días soleados. Seria importante verificar si de igual forma hay mayor demanda para generar un plan para usuarios finales y empresas que favorezca la demanda de los clientes. 
