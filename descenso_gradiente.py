
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

archivos = ['1819', '1920', '2021', '2122', '2223']
cols = ['HomeTeam', 'FTHG']

unido = []
for archivo in archivos:
    df = pd.read_csv(f'data/E0_{archivo}.csv', usecols=cols)
    unido.append(df)

df_train = pd.concat(unido, ignore_index=True)
df_test = pd.read_csv('data/E0_2324.csv', usecols=cols)

# Feature X: Promedio histórico del equipo local
promedio_por_equipo = df_train.groupby('HomeTeam')['FTHG'].mean()
promedio_global = df_train['FTHG'].mean()

X_train = (
    df_test['HomeTeam']
    .map(promedio_por_equipo)
    .fillna(promedio_global)
    .values
)

y_train = df_test['FTHG'].values


#Descenso gradiente

def descenso_gradiente(X, y, alpha, epocas=2000):
    N = len(y)
    theta0 = 0.0  # Intercepto inicial
    theta1 = 0.0  # Pendiente inicial
    perdidas = []

    for _ in range(epocas):
        # a) Predicción actual: h_theta(x) = theta0 + theta1 * X
        y_pred = theta0 + theta1 * X

        # b) Error para cada partido
        error = y_pred - y

        # c) Función de Pérdida (MSE / 2)
        loss = np.mean(error**2) / 2.0
        perdidas.append(loss)

        # d) Gradientes (derivadas parciales)
        grad_theta0 = np.mean(error)
        grad_theta1 = np.mean(error * X)

        # e) Actualización simultánea de parámetros
        theta0 -= alpha * grad_theta0
        theta1 -= alpha * grad_theta1

    return theta0, theta1, perdidas


# Verificaion de los test

epocas_test = 2500
alpha_optimo = 0.12

theta0, theta1, perdidas = descenso_gradiente(
    X_train, y_train, alpha=alpha_optimo, epocas=epocas_test
)

print(f'Theta0 = {theta0}')
print(f'Theta1 = {theta1}')

# TEST 1: La pérdida baja en cada iteración

test1_paso = all(
    perdidas[i + 1] <= perdidas[i] + 1e-12
    for i in range(len(perdidas) - 1)
)

# TEST 2: Convergencia (los últimos 10 valores apenas cambian) 

diferencia_final = abs(perdidas[-1] - perdidas[-10])
test2_paso = diferencia_final < 1e-4

# TEST 3: Coincidencia con np.polyfit(x, y, 1)
# np.polyfit devuelve [pendiente (theta1), intercepto (theta0)]

poly_theta1, poly_theta0 = np.polyfit(X_train, y_train, 1)

test3_paso = np.allclose(
    [theta1, theta0],
    [poly_theta1, poly_theta0],
    atol=0.01
)

print('=== RESULTADOS DE VERIFICACIÓN DE TESTS ===')

print(f'Test 1 (Pérdida monótonamente decreciente) : {test1_paso}')

print(
    f'Test 2 (Convergencia en últimas 10 épocas) : {test2_paso}'
    f' (Diferencia: {diferencia_final:.7f})'
)

print(f'Test 3 (Coincidencia con np.polyfit)       : {test3_paso}')

print(f'  -> GD      : theta1 = {theta1:.4f}, theta0 = {theta0:.4f}')
print(f'  -> Polyfit : theta1 = {poly_theta1:.4f}, theta0 = {poly_theta0:.4f}\n')


# Grafica de perdida con 3 valores de alpha

alphas = [0.01, 0.05, 0.12, 1]

fig, ax = plt.subplots(figsize=(9, 5))

for a in alphas:
    _, _, loss_history = descenso_gradiente(
        X_train, y_train, alpha=a, epocas=1200
    )

    ax.plot(loss_history, label=f'α = {a}')

ax.set_title(
    'Evolución de la Función de Pérdida (MSE) para distintos α',
    fontsize=12,
    fontweight='bold',
)

ax.set_xlabel('Iteración / Época', fontsize=10)
ax.set_ylabel('Pérdida (Loss / 2)', fontsize=10)
ax.legend(frameon=True)
ax.set_yscale('log')
ax.set_xlim(0, 150)
ax.set_ylim(0.8, 1000)
ax.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
fig.savefig('figuras/curvas_de_perdida_con_alpha_distinto.png')
plt.show()

