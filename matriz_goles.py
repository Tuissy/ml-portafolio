import numpy as np
import csv

with open('data/E0_2324.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    goles = []
    datos = []
    equipos = []
    for row in reader:
        partido = []
        partido.append(row['FTHG'])
        partido.append(row['FTAG'])
        goles.append(partido)

        datos_partido = []
        datos_partido.append(row['Date'])
        datos_partido.append(row['HomeTeam'])
        datos_partido.append(row['AwayTeam'])
        datos.append(datos_partido)

        equipo = []
        equipo.append(row['HomeTeam'])
        equipo.append(row['AwayTeam'])
        equipos.append(equipo)

    m = np.array(goles, dtype=np.int64)
    print(m.shape)

# ¿Cuántos goles se marcaron en toda la temporada?

    total_goles = m.sum()
    print(f'Goles totales en toda la temporada: {total_goles}')

# ¿Cuál es el promedio de goles por partido, de local y de visitante?

    goles_promedio = np.average(m, axis=0)
    avg_total = goles_promedio.sum()
    avg_home = goles_promedio[0]
    avg_away = goles_promedio[1]

    print(f'Goles promedio por partido: {avg_total}')
    print(f'Goles promedio de local: {avg_home}')
    print(f'Goles promedio de visitante: {avg_away}')
    

# ¿En cuántos partidos ganó el local, cuántos acabaron en empate y cuántos ganó el visitante? (Sin recorrer la matriz: compara columnas enteras.)
    
    ganador = (m[:, 0] > m[:, 1])
    local_ganador = ganador.sum()
    print(f'Partidos donde ganó el local: {local_ganador}')

    perdedor = (m[:, 0] < m[:, 1])
    visitante_ganador = perdedor.sum()
    print(f'Partidos donde ganó el visitante: {visitante_ganador}')

    empate = (m[:, 0] == m[:, 1])
    empates = empate.sum()
    print(f'Partidos empatados: {empates}')
# ¿Cuál fue el partido con más goles en total?

    goles_partido = m.sum(axis=1)
    indice_mayor = goles_partido.argmax()
    indices_todos = np.where(goles_partido == goles_partido[indice_mayor])
    partidos_mayor = indices_todos[0].tolist()

    print('Partidos con mas goles:')
    for x in partidos_mayor:
        partido_mayor = datos[x]
        goles_max = goles_partido[x]
        print(f'{partido_mayor[1]} y {partido_mayor[2]} jugado el {partido_mayor[0]} con un total de {goles_max} goles')


# El reto: el promedio de goles a favor de cada equipo, sin bucles sobre los partidos.


    info = np.array(equipos)
    unicos_equipo = np.unique(info)

    
    for i in unicos_equipo:
        mascara_local = (info[:,0] == i)
        goles_local = m[:, 0].sum(where=mascara_local) 

        mascara_visitante = (info[:,1] == i)
        goles_visitante = m[:, 1].sum(where=mascara_visitante) 

        promedio_goles = (goles_local + goles_visitante) / (mascara_visitante.sum() + mascara_local.sum())

        print(f'{i}: {promedio_goles:.2f}')
    

    

