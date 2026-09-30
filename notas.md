Bueno, arranco sin saber nada sobre los archivos csv, ni como manejarlso con python. Iniciare entrando a la documentacion docs.python.org/3/library/csv.html y vere csv.DictReader.

Uso with y open para abrir el archiov. Uso un for row en el archiov para leer cada fila

1. Abrir el archivo e imprimir las 3 primeras filas

Codigo: import csv

with open('/Users/hectorfigueredo/Desktop/Curso-Machine Learning/repos/ml-portafolio/ml-portafolio/data/E0.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Date'], row['Time'], row['HomeTeam'])

2. Imprimir, para cada partido, solo cuatro datos: local, visitante, goles del local, goles del visitante.

import csv

with open('/Users/hectorfigueredo/Desktop/Curso-Machine Learning/repos/ml-portafolio/ml-portafolio/data/E0.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['HomeTeam'], row['AwayTeam'], row['FTHG'], row['FTAG'])

3. Elegir dónde vas a ir guardando lo que acumulas de cada equipo (esta es la decisión de diseño importante del ejercicio; piénsala antes de escribir).

Los datos yo diria que los guardare en listas o en variables

4. Para la creacion del programa estoy viendo como hacer lo de los diccionarios si los equiops no estan. Ahorita no tengo mucha idea de como hacerlo

    for row in reader:
        Equipos=[]
        Equipos.append(row['HomeTeam'])
        Equipos.append(row['AwayTeam'])
        for x in Equipos:
            if x in Teams:
                continue
            else:
                Teams[x] = {'PJ':0, 'G':0, 'E':0, 'P':0, 'GF':0, 'GC':0, 'puntos':0,'DG':0}

    Esa fue mi solucion y me di cuenta depsues que puedo hacer con dict.setdefault

5. Criterio de desempate puntos, diferencia de goles, goles a favor