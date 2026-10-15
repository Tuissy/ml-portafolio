import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv

temporadas = ['1819','1920','2021','2122','2223','2324']
keys = ['18/19','19/20','20/21','21/22','22/23','23/24']

cols = ['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HF',
    'AF', 'HY', 'AY', 'HR', 'AR',]

lista_dfs = []
for i in temporadas:
    df = pd.read_csv(f'data/E0_{i}.csv', usecols=cols)
    lista_dfs.append(df)

df_unido = pd.concat(lista_dfs, keys=keys, names=['Temporada'])
df_final = df_unido.reset_index(level=0).reset_index(drop=True)
df_final['Date'] = pd.to_datetime(df_final['Date'], format='%d/%m/%Y')

# 1. Evolución temporal: ventaja local en goles por temporada, con la 20/21 destacada de algún modo.

# Ventaja local en goles por temporada

goles = df_final.groupby('Temporada')[['FTHG','FTAG']].mean().round(3)
goles['ventaja local'] = (goles['FTHG'] - goles['FTAG'])

# Grafica

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot( goles.index, goles['ventaja local'], marker='o', color='tab:blue', linewidth=2, label='Ventaja local')
val_2021 = goles.loc['20/21', 'ventaja local']
ax.plot('20/21', val_2021, marker='o', markersize=10, color='red', label='Temporada sin público (20/21)')

ax.set( title='Evolución de la Ventaja Local por Temporada', xlabel='Temporada', ylabel='Diferencia de Goles Promedio (Local - Visitante)', )
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(frameon=True)
plt.tight_layout()


#2. Resultados (H/D/A) con público frente a sin público

# Resultados

condicion_sin_publico = (df_final['Date'] >= '2020-03-13') & (
    df_final['Date'] <= '2021-05-31'
)

df_final['Condicion_Publico'] = 'Con Público'
df_final.loc[condicion_sin_publico, 'Condicion_Publico'] = 'Sin Público'

resultados = df_final.groupby('Condicion_Publico')['FTR'].value_counts(normalize=True).unstack()[['H', 'D', 'A']] * 100


#Grafica

fig2, ax2 = plt.subplots(figsize=(9,5))
resultados.plot(kind='bar', ax=ax2, width=0.7, color=['#2b5c8f', '#7f7f7f', '#d95f02'])
ax2.set_title( 'Distribución de Resultados: Con Público vs. Sin Público', fontsize=12, fontweight='bold', )
ax2.set_xlabel('Condición de Público', fontsize=10)
ax2.set_ylabel('Porcentaje de Partidos (%)', fontsize=10)
ax2.set_xticklabels(['Con Público', 'Sin Público'], rotation=0)

ax2.legend( title='Resultado', labels=['Victoria Local (H)', 'Empate (D)', 'Victoria Visitante (A)'], )
ax2.grid(axis='y', linestyle=':', alpha=0.6)
plt.tight_layout()
#3. La ventaja con barras de error

df_final['Diferencia'] = df_final['FTHG'] - df_final['FTAG'] 
goles_stats = df_final.groupby('Temporada')['Diferencia'].agg( promedio='mean', error_estandar='sem')

# Grafica

fig3, ax3 = plt.subplots(figsize=(9,5))
ax3.errorbar(goles_stats.index, goles_stats['promedio'],yerr=goles_stats['error_estandar'],
             fmt='-o',color='tab:blue', ecolor='crimson', elinewidth=1.5, capsize=4, label='Ventaja local (media ± sem)')
ax3.axvline( x='20/21', color='gray', linestyle='--', alpha=0.7, label='Temporada sin público (20/21)' )
ax3.set_title( 'Evolución de la Ventaja Local por Temporada (con Barras de Error)', fontsize=12, fontweight='bold' )
ax3.set_xlabel('Temporada', fontsize=10)
ax3.set_ylabel('Ventaja Local Promedio (Goles)', fontsize=10)
ax3.grid(True, linestyle=':', alpha=0.6)
ax3.legend()
plt.tight_layout()
#Comportamiento arbitral (faltas o tarjetas)

arbitros = df_final.groupby('Condicion_Publico')[['HF','AF','HY','AY']].mean().round(3)

# 4. Comportamiento arbitral faltas
faltas = arbitros[['HF','AF']]

fig4, ax4 = plt.subplots(figsize=(9,5))
faltas.plot(kind='bar', ax=ax4, width=0.7, color=['#2b5c8f', '#d95f02'])

for container in ax4.containers: ax4.bar_label(container, fmt='%.2f', padding=3, fontsize=9)

ax4.set_title( 'Promedio de Faltas por Partido: Local (HF) vs. Visitante (AF)', fontsize=12, fontweight='bold', )
ax4.set_xlabel('Condición de Público', fontsize=10)
ax4.set_ylabel('Faltas Promedio', fontsize=10)
ax4.set_xticklabels(['Con Público', 'Sin Público'], rotation=0)
ax4.legend(['Faltas Local (HF)', 'Faltas Visitante (AF)'], frameon=True)
ax4.grid(axis='y', linestyle=':', alpha=0.6)
ax4.set_ylim(0, faltas.values.max() * 1.2)
plt.tight_layout()

# 5. Comportamiento arbitral tarjetas amarillas
amarillas = arbitros[['HY','AY']]

fig5, ax5 = plt.subplots(figsize=(9,5))
amarillas.plot(kind='bar', ax=ax5, width=0.7, color=["#2b508f", '#d95f02'])

for container in ax5.containers: ax5.bar_label(container, fmt='%.2f', padding=3, fontsize=9)

ax5.set_title( 'Promedio de amarillas por Partido: Local (HY) vs. Visitante (AY)', fontsize=12, fontweight='bold', )
ax5.set_xlabel('Condición de Público', fontsize=10)
ax5.set_ylabel('Amarillas Promedio', fontsize=10)
ax5.set_xticklabels(['Con Público', 'Sin Público'], rotation=0)
ax5.legend(['Amarillas Local (HY)', 'Amarillas Visitante (AY)'], frameon=True)
ax5.grid(axis='y', linestyle=':', alpha=0.6)
ax5.set_ylim(0, amarillas.values.max() * 1.2)
plt.tight_layout()

# 6 Histograma diferencia de goles con y sin publico

dif_con = df_final.loc[ df_final['Condicion_Publico'] == 'Con Público', 'Diferencia' ]
dif_sin = df_final.loc[ df_final['Condicion_Publico'] == 'Sin Público', 'Diferencia' ]

bins = [x - 0.5 for x in range(int(df_final['Diferencia'].min()), int(df_final['Diferencia'].max()) + 2)]

fig6, ax6 = plt.subplots(figsize=(9, 5))
ax6.hist( dif_con, bins=bins, alpha=0.5, label='Con Público', color='#1f77b4', density=True, edgecolor='white', )
ax6.hist( dif_sin, bins=bins, alpha=0.6, label='Sin Público', color='#ff7f0e', density=True, edgecolor='white', )

ax6.axvline( dif_con.mean(), color='#1f77b4', linestyle='--', linewidth=2, label=f'Media Con Público ({dif_con.mean():.2f})', )
ax6.axvline( dif_sin.mean(), color='#ff7f0e', linestyle='--', linewidth=2, label=f'Media Sin Público ({dif_sin.mean():.2f})', )

ax6.set_title( 'Distribución de la Diferencia de Goles (Local - Visitante)', fontsize=12, fontweight='bold', )
ax6.set_xlabel('Diferencia de Goles por Partido', fontsize=10)
ax6.set_ylabel('Proporción / Densidad', fontsize=10)
ax6.set_xticks(range(int(df_final['Diferencia'].min()), int(df_final['Diferencia'].max()) + 1))
ax6.legend(frameon=True)
ax6.grid(axis='y', linestyle=':', alpha=0.6)
plt.tight_layout()

# 6. Calcular los dos porcentajes para cada grupo
hallazgo = ( df_final.groupby('Condicion_Publico')['Diferencia'] 
            .agg(
                Goleadas_Locales=lambda x: (x >= 3).mean() * 100,
                Victorias_Ajustadas=lambda x: x.isin([1, 2]).mean() * 100, ) .round(2) )
print(hallazgo)

fig.savefig('figuras/ventaja_por_temporada.png')
fig2.savefig('figuras/resultados_con_sin_publico.png')
fig3.savefig('figuras/ventaja_por_temporada_error_estandar.png')
fig4.savefig('figuras/faltas_con_sin_publico.png')
fig5.savefig('figuras/amarillas_con_sin_publico.png')
fig6.savefig('figuras/histograma_goles_con_sin_publico.png')
plt.show()



