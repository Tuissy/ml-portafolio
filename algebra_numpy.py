import numpy as np
import time

# Ejercicio 1
def producto_matricial(A,B):
    filasA = len(A)
    columnasA = len(A[0])
    filasB = len(B)
    columnasB = len(B[0])

    if columnasA != filasB:
        raise ValueError('El numero de columnas de la matriz A debe coincidir con el numero de filas de la matriz B')

    C = np.zeros((filasA,columnasB))

    for i in range(filasA):
        for j in range(columnasB):
            for k in range(columnasA):
                C[i , j] += A[i][k] * B[k][j]

    return C
    

A = np.array([[1,2,3],[1,2,3],[1,2,3]])
B = np.array([[2,2],[3,3],[1,1]])

mi_resultado = producto_matricial(A,B)

# Verificacion
print(np.allclose(mi_resultado, A @ B))

# Comparacion de velocidad

ranA = np.random.randint(10, size=(200, 200))
ranB = np.random.randint(10, size=(200, 200))

inicio_for = time.perf_counter()
productor_for = producto_matricial(ranA,ranB)
fin_for = time.perf_counter()
tiempo_for = fin_for - inicio_for

inicio_np = time.perf_counter()
productor_np = ranA @ ranB
fin_np = time.perf_counter()
tiempo_np = fin_np - inicio_np

print(f"Tiempo con bucles for:    {tiempo_for:.6f} segundos\n")
print(f"Tiempo con np:    {tiempo_np:.6f} segundos\n")

diferencia = tiempo_for / tiempo_np
print(f"NumPy es aprox. {diferencia:.1f} veces más rápido.")

# Ejercicio 2

def normalizar_columnas(arr):
    arr_mean = arr.mean(0)
    arr_std = arr.std(0)

    arr_std[arr_std == 0] = 1.0

    resultado = (arr - arr_mean) / arr_std
    return resultado

arr1 = np.random.random((3,3))
arr2 = np.ones((3,3))

resultado1 = normalizar_columnas(arr1)
resultado2 = normalizar_columnas(arr2)
print('Caso numeros random')
print(resultado1.mean(axis=0))
print(resultado1.std(axis=0))
print('Caso columnas con valores iguales')
print(resultado2.mean(axis=0))
print(resultado2.std(axis=0))