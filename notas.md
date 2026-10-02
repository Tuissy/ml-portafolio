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


Explicacion de Feynam:

¿Por qué un diccionario de diccionarios y no una lista?

Usamos un diccionario de diccionarios porque si usaramos listas tendrias que recorrerla completa para acceder a un dato, esto con una gran cantidad de datos haria mucho mas lento el programa. Por lo que con los diccionarios tenemos una velocidad de O(1) y no de O(n), gracias a que podemos ir directo al dato deseado con el uso de las keys.

¿Qué hace setdefault y qué problema te evita?

El setdefault nos ayuda a crear los valores por defecto del diccionario, de esta forma crea solo si no existe; si ya hay valores, no los toca, y evitar que haya problemas a la hora de insertar datos.


¿Por qué la clave de ordenación devuelve una tupla de tres valores?

Esto lo hace porque fue lo que pedimos, ya que no estamos ordenando la tabla por un solo criterio, sino que hay un desempate de 3 condiciones. Por lo que es necesario para nostros que se nos retorne la tupla de 3 valores.

