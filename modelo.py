
import numpy as np
import pandas as pd

# ==================================================
# 1. CARGA DE DATOS (Entrenamiento y Prueba)
# ==================================================
archivos = ['1819', '1920', '2021', '2122', '2223']
cols = ['HomeTeam', 'FTHG']

unido = []
for archivo in archivos:
    df = pd.read_csv(f'data/E0_{archivo}.csv', usecols=cols)
    unido.append(df)

df_train = pd.concat(unido, ignore_index=True)
df_test = pd.read_csv('data/E0_2324.csv', usecols=cols)

# ==================================================
# 2. ESTADÍSTICOS BASE DE ENTRENAMIENTO
# ==================================================
# Conteo de partidos (N), suma de goles y media por equipo
stats_equipo = df_train.groupby('HomeTeam')['FTHG'].agg(['count', 'sum'])
promedio_global = df_train['FTHG'].mean()

y_real = df_test['FTHG']
ss_tot = ((y_real - y_real.mean()) ** 2).sum()

print('=== COMPARACIÓN DE DIFERENTES NIVELES DE SUAVIZADO (m) ===\n')

# ==================================================
# 3. EXPERIMENTO CON DISTINTOS VALORES DE m (PESO VIRTUAL)
# ==================================================
# m = 0  -> Modelo original (sin suavizado / media simple)
# m > 0  -> Grado de contracción hacia la media de la liga
valores_m = [0, 5, 10, 19, 38, 100]

for m in valores_m:
    # Fórmula de Suavizado: (Suma goles + m * media_liga) / (N partidos + m)
    feature_shrunk = (stats_equipo['sum'] + m * promedio_global) / (
        stats_equipo['count'] + m
    )
    mapa_shrunk = feature_shrunk.to_dict()

    # Aplicar en la temporada 23/24
    prediccion = (
        df_test['HomeTeam'].map(mapa_shrunk).fillna(promedio_global)
    )

    # Métricas
    mae = (y_real - prediccion).abs().mean()
    ss_res = ((y_real - prediccion) ** 2).sum()
    r2 = 1 - (ss_res / ss_tot)

    print(
        f'm = {m:3d}  |  MAE: {mae:.4f} goles  |  R²: {r2:.4f}  |  Ej. Arsenal'
        f' Pred: {mapa_shrunk.get("Arsenal", promedio_global):.3f}'
    )
