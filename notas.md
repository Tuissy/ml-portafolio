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

