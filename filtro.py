import matplotlib.pyplot as plt
import pandas as pd

# 1. CARGA DE DATOS HISTÓRICOS (Temporadas 18/19 a 22/23)
archivos = ['1819', '1920', '2021', '2122', '2223']
cols = ['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']
keys = ['18/19', '19/20', '20/21', '21/22', '22/23']

grupo = []
for i in archivos:
  df = pd.read_csv(f'data/E0_{i}.csv', usecols=cols)
  grupo.append(df)

df_unido = pd.concat(grupo, keys=keys, names=['Temporada'])
df_final = df_unido.reset_index(level=0).reset_index(drop=True)
df_final['Diferencia_goles'] = df_final['FTHG'] - df_final['FTAG']

# 2. CARGA DE LA TEMPORADA 23/24
df_sujeto = pd.read_csv('data/E0_2324.csv', usecols=cols)


# 3. AGRUPAR EL HISTÓRICO (Calculamos las 3 métricas)
stats_historico = (
    df_final.groupby('HomeTeam')
    .agg(
        Prom_DifGoles_Hist=('Diferencia_goles', 'mean'),
        Prom_FTAG_Hist=('FTAG', 'mean'),  # Goles en contra del local
        Prom_FTHG_Hist=('FTHG', 'mean'),  # Goles a favor del local
    )
    .reset_index()
)

# 4. AGRUPAR LA TEMPORADA 23/24
stats_sujeto = (
    df_sujeto.groupby('HomeTeam')
    .agg(Prom_FTHG_2324=('FTHG', 'mean'))
    .reset_index()
)

# 5. UNIR AMBOS DATASETS POR EQUIPO
df_comparacion = pd.merge(
    stats_historico, stats_sujeto, on='HomeTeam', how='inner'
)

print(f'Equipos analizados en común: {len(df_comparacion)}')
print('-' * 60)


# ==========================================
# GRÁFICA 1: Dif. Goles Histórica vs Goles 23/24
# ==========================================
corr1 = df_comparacion['Prom_DifGoles_Hist'].corr(
    df_comparacion['Prom_FTHG_2324']
)
print(f'1. Correlación Dif. Goles (Hist) vs Goles (23/24): {corr1:.4f}')

plt.figure(figsize=(9, 6))
plt.scatter(
    df_comparacion['Prom_DifGoles_Hist'],
    df_comparacion['Prom_FTHG_2324'],
    color='royalblue',
    s=90,
    alpha=0.8,
    edgecolors='black',
    label=f'Correlación: {corr1:.4f}',
)

for i, row in df_comparacion.iterrows():
  plt.annotate(
      row['HomeTeam'],
      (row['Prom_DifGoles_Hist'], row['Prom_FTHG_2324']),
      xytext=(5, 5),
      textcoords='offset points',
      fontsize=9,
  )

plt.title('1. Dif. de Goles Histórica (Local) vs Goles a Favor (23/24)')
plt.xlabel('Promedio Diferencia de Goles (18/19 - 22/23)')
plt.ylabel('Promedio Goles a Favor Local (23/24)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()




# ==========================================
# GRÁFICA 2: Goles en Contra Históricos vs Goles 23/24
# ==========================================
corr2 = df_comparacion['Prom_FTAG_Hist'].corr(
    df_comparacion['Prom_FTHG_2324']
)
print(f'2. Correlación Goles en Contra (Hist) vs Goles (23/24): {corr2:.4f}')

plt.figure(figsize=(9, 6))
plt.scatter(
    df_comparacion['Prom_FTAG_Hist'],
    df_comparacion['Prom_FTHG_2324'],
    color='crimson',
    s=90,
    alpha=0.8,
    edgecolors='black',
    label=f'Correlación: {corr2:.4f}',
)

for i, row in df_comparacion.iterrows():
  plt.annotate(
      row['HomeTeam'],
      (row['Prom_FTAG_Hist'], row['Prom_FTHG_2324']),
      xytext=(5, 5),
      textcoords='offset points',
      fontsize=9,
  )

plt.title('2. Goles en Contra Históricos (Local) vs Goles a Favor (23/24)')
plt.xlabel('Promedio Goles en Contra Local (18/19 - 22/23)')
plt.ylabel('Promedio Goles a Favor Local (23/24)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()





# ==========================================
# GRÁFICA 3: Goles a Favor Históricos vs Goles 23/24
# ==========================================
corr3 = df_comparacion['Prom_FTHG_Hist'].corr(
    df_comparacion['Prom_FTHG_2324']
)
print(f'3. Correlación Goles a Favor (Hist) vs Goles (23/24): {corr3:.4f}')

plt.figure(figsize=(9, 6))
plt.scatter(
    df_comparacion['Prom_FTHG_Hist'],
    df_comparacion['Prom_FTHG_2324'],
    color='forestgreen',
    s=90,
    alpha=0.8,
    edgecolors='black',
    label=f'Correlación: {corr3:.4f}',
)

for i, row in df_comparacion.iterrows():
  plt.annotate(
      row['HomeTeam'],
      (row['Prom_FTHG_Hist'], row['Prom_FTHG_2324']),
      xytext=(5, 5),
      textcoords='offset points',
      fontsize=9,
  )

plt.title('3. Goles a Favor Históricos (Local) vs Goles a Favor (23/24)')
plt.xlabel('Promedio Goles a Favor Local (18/19 - 22/23)')
plt.ylabel('Promedio Goles a Favor Local (23/24)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()


plt.show()