#  Proyecto tabla premier league

## De que trata el proyecto ?

Este proyecto crea la tabla de resultados de la premier league temporada 2026/27, 50 partidos disputados hasta el 20 de septiembre de 2026, fuente football-data.co.uk. Les dimos estructura, orden y creamos la tabla con las posiciones de los equipos siguiendo los lineamientos oficiales de desempate. 

## Datos

### Datos de entrada

HomeTeam, AwayTeam, FTHG, FTAG, FTR

### Datos de salida

Posición, nombre del equipo, partidos perdidos, ganados y empatados, goles a favor y en contra, y la diferencia de goles, al igual que el puntaje del equipo

```python
Pos         Equipo     PJ         G          E         P         GF        GC        DG        Pts       
1          Man City    5          5          0          0         13          5         +8         15
2          Arsenal     5          4          0          1          8          4         +4         12
3          Brighton    5          3          1          1         16          5        +11         10
4          Brentford   5          2          3          0         10          4         +6          9
5          Leeds       5          2          3          0          7          3         +4          9
```

## Como ejecutarlo

```bash
python3 tabla.py
```

El comando se ejecuta desde la carpeta del repositorio, porque la ruta al CSV es relativa.

tabla.py es la versión desarrollada durante la semana y tabla_desde_cero.py la reescritura de memoria. Para ejecutarlo requiere Python 3.12 o superior, es necesario tener el archivo csv. No hay que instalar dependencias, ni librerías externas.

## Validación

Todos los datos estan validados con pruebas tipo print. Como suma de puntajes con partidos ganados, empatados, perdidos. Validación de suma de goles y una de tipo assert para ver si faltan partidos por contar. Y todo esta contrastado posición por posición con la clasificación oficial al 20-09-2026

```python
print(all(e['G'] + e['E'] + e['P'] == e['PJ'] for e in Teams.values()))
print(all(e['Pts'] == 3*e['G'] + e['E'] for e in Teams.values()))
assert sum(e['PJ'] for e in Teams.values()) == 100, "Faltan partidos por contar"
```

## Aprendizaje 

Con este proyecto aprendí mucho. Desde como acceder a un archivo csv, hasta como darle orden. Fue crucial el aprendizaje de como funcionan los diccionarios, como iterarlos, y como usar funciones como sorted y enumerate para ver una estructura correcta y ordenada.

