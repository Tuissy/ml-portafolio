import csv
import pandas as pd
import matplotlib.pyplot as plt
import random as rd
import numpy as np

# Para no tener que crear uno por uno los dataframes con diferentes nombres
# Dentro de un for, usamos una lista con los distintos nombres y lo pasamos con un f string a la creacion
# Despues pasamos cada df a una lista, y lo concatenamos en un df_unido

files = ['1819','1920','2021','2122','2223','2324']
columnas = ['Date','HomeTeam','AwayTeam','FTHG','FTAG','FTR']
dataframes = []
for file in files:
    df = pd.read_csv(f'data/E0_{file}.csv', usecols=columnas)
    dataframes.append(df)

temporadas = ['18/19','19/20','20/21','21/22','22/23','23/24']
df_unidos = pd.concat(dataframes, keys= temporadas, names=['Temporada'])
#Agregamos el parametro keys, ya que con esto cada temporada estara nombrada con base al año de la temporada
#Al hacer esto, se pasara como un indice nuevo. Para darle nombre a estos indices usamos el parametro names
# Y le pones dentro de una lista como queremos que se llame, ya que hay que recordar que tenemos dos indices
# El de las temporadas, y el de cada fila individualmente

#Despues, para convertir este nuevo indice, en una columna, creamos un nuevo dataset
# y le aplicamos resest_index() a nuestro dataset que teniamos antes
# importante especificar level=0 como parametro, ya que solo queremos que las temporadas sean una nueva columna
# Y despues volvemos a aplicar .reset_index() pero con el parametro drop=True, para que los indices
# sean aplicados al numero de filas, y no se reinicien por cada temporada, esto para un mejor acceso individual
df_final = df_unidos.reset_index(level=0).reset_index(drop=True)

df_final['Date'] = pd.to_datetime(df_final['Date'], format='%d/%m/%Y')
# Convertimos la columa Date de texto a la forma de fecha de pandas, con to_datetime, y pasamos como argumento
#la columna y especificamos el formato, ya que por default lleva primero mes y luego dia, entonces 
# lo cambiamos a dia , mes , año

# Creamos una condicion que indica el rango de fechas donde no hubo publico en los partidos
condicion_publico = ((df_final['Date'] >= '2020-03-13') & (
    df_final['Date'] <= '2021-05-31'
))

# Creamos un nuevo dataframe con solo los partidos con publico
df_publico = df_final.loc[~condicion_publico]

medias_muestra = []
medias_muestra2 = []
medias_muestra3 = []

df_publico['Ventaja local'] = df_publico['FTHG'] - df_publico['FTAG']

for x in range(1000):
    #Extraemos al azar una muestra de 50,200,800 partidos y calculamos su ventaja media
    df_muestra = df_publico.sample(n=50)
    df_muestra2 = df_publico.sample(n=200)
    df_muestra3 = df_publico.sample(n=800)
    media = df_muestra['Ventaja local'].mean()
    media2 = df_muestra2['Ventaja local'].mean()
    media3 = df_muestra3['Ventaja local'].mean()
    medias_muestra.append(media)
    medias_muestra2.append(media2)
    medias_muestra3.append(media3)

#  Lo repetimos 1000 veces y guardamos las 1000 medias

# Unimos todas las medias para encontrar el rango global mínimo y máximo
todas_medias = medias_muestra + medias_muestra2 + medias_muestra3
min_val = min(todas_medias)
max_val = max(todas_medias)

# Creamos bins unificados y compartidos (por ejemplo, 35 o 40 bins)
bins_comunes = np.linspace(min_val, max_val, 35)

# Histograma
fig, ax = plt.subplots(figsize=(9, 5))

plt.hist(medias_muestra, bins=bins_comunes, label='Muestra de 50 partidos', 
         edgecolor='black', color='skyblue', density=True, alpha=0.4)
plt.hist(medias_muestra2, bins=bins_comunes, label='Muestra de 200 partidos', 
         edgecolor='black', color='limegreen', density=True, alpha=0.5)
plt.hist(medias_muestra3, bins=bins_comunes, label='Muestra de 800 partidos', 
         edgecolor='black', color='orange', density=True, alpha=0.6)


# Calculamos la media y la desviación estándar de las 1,000 medias de las muestra de 800
mu = np.mean(medias_muestra3)
std = np.std(medias_muestra3)

# Generamos los puntos en el eje X
xmin, xmax = plt.xlim()
# Cuando no tiene ningun argumetno dentro de xlim() devuelve una tupla con los limites actuales

# Con numpy creamos 100 puntos que van del minimo de x al maximo
x = np.linspace(xmin, xmax, 100)

# Aplicamos la fórmula de la campana de Gauss directamente con NumPy
p = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / std) ** 2)

#Trazamos la línea de la curva teórica encima
plt.plot(x, p, 'r-', linewidth=2.5, label='Curva Normal Teórica')

ax.set_title('Distribucion de ventaja de goles (Local - visitante)')
ax.set_xlabel('Media de la ventaja de goles')
ax.set_ylabel('Frecuencia')
plt.grid(True, linestyle='--', alpha=0.6)
ax.legend(frameon=True)
plt.tight_layout()
fig.savefig('figura_repaso/Distribucion_de_las_medias_(ventaja goles local).png')
plt.show()

# Tamaño total de la población (partidos con público disponibles)
N = len(df_publico)

# Desviación estándar de todos los datos originales
std_poblacional = df_publico['Ventaja local'].std()

# Tamaño de tu muestra (por ejemplo, n = 800)
n = 800

# Error Estándar Teórico CON el factor de corrección para población finita
se_teorico_corregido = (std_poblacional / np.sqrt(n)) * np.sqrt((N - n) / (N - 1))

print(f"SE Empírico en las 1000 sim. (n=800): {np.std(medias_muestra3):.4f}")
print(f"SE Teórico con fórmula (n=800): {se_teorico_corregido:.4f}")


