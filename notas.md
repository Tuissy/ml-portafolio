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

## Semana 2 — Dónde mi instinto pidió un bucle

1. **Al sumar los goles de un equipo seleccionado.** Pregunté literalmente:
   "¿puedo usar un for para sumar los goles una vez ya tengo el índice?"
   → Respuesta: no. Si el bucle recorre *datos*, está mal; si recorre
   *entidades* (los 20 equipos), está bien. Lo resolví con .sum() sobre
   las filas seleccionadas.

2. **Al buscar el partido con más goles.** Mi primer reflejo fue quedarme
   con un solo máximo (argmax); pensar en "todos los que empatan en el
   máximo" exigía comparar el array entero contra un valor y usar
   np.flatnonzero, no recorrerlo.

3. **Al agrupar por equipo.** No supe cómo seleccionar los partidos de un
   equipo sin recorrer los 380 partidos comprobando el nombre uno a uno.
   La herramienta que sustituye a ese if dentro del bucle es la máscara
   booleana.

### Lo que me costó más
- El parámetro `axis` (qué significa 0 y 1).
- Que un array tiene un único `dtype` y que si lees texto del CSV sin
  convertirlo, NumPy se niega a sumar.
- La diferencia entre m[0,0] (un número) y m[:,0] (una columna entera).

### Regla que me llevo
Si el bucle recorre datos → vectorizar. Si recorre entidades → está bien.

## Semana 2 Dia jueves

### Ejercicio 1: multiplicacion de matriz
Para el ejercicio 1, inicie haciendolo a mano, lo primero que hice fue desglosar las reglas para hacer una multiplicacion de matrices:

1. El numero de columnas de la matriz A tiene que ser igual al numero de filas de la matriz B
2. El resultado C sera una matriz de forma (n filas A, n columnas B)

Despues al hacer la multiplicacion a mano, e iba poniendo las variables en el papel en forma de indices, por ejemplo A[0][0] * B[0][0] + A[0][1] * [1][0]

Despues estuve un buen rato pensando como usar los for para que se lograra respetar la forma de multiplicar cada fila por cada columna y que obtuviera el orden de indices para lograrlo. Y despues de un rato, lo que me ayudo mucho fue definir los nombres de las variables de python, poner el numero de columnas y filas de A y B. ya que asi tenia una mejor imagen mental de que es lo que tiene que iterarse.

Estuve un buen tiempo haciendolo, pero logre que la correcion np.allclose(mi_resultado, A @ B) diera True

Mi hipotesis del uso de np.allclose y no == es que ese margen de error que sea lo mas cercano posible, para evitar las pequeños numeros de diferencia entra una operacion de python y numpy

### Ejercicio 2: normalizacion

Mi hipotesis del uso de np.allclose tenia la direccion correcta, pero la explicacion es que muchas veces no hay una representacion exacta en binario para los decimales, por lo que el valor que queda es lo mas parecido posible a 0, por ejemplo 1e-16. Entonces si usaramos == para comparar, siempre dara False porque no es exactamente igual, lo mejor es np.allclose ya que verifica que se acerque lo mas posible al 0