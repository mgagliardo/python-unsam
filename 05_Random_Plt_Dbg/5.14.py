import numpy as np
import random


# 5.10
def crear_album(figus_total):
    return np.zeros(figus_total)

# 5.11
def album_incompleto(A):
    # Si hay al menos un 0, devuelve true
    return 0 in A

# 5.12
def comprar_figu(figus_total):
    # Devuelve una figurita en el rango
    # del total del album
    return random.choice(range(0, figus_total))

# 5.13
def cuantas_figus(figus_total):
    contador = 0
    nuevo_album = crear_album(figus_total)
    while album_incompleto(nuevo_album):
        nuevo_album[comprar_figu(figus_total)] = 1
        contador += 1
    return contador

# 5.14
n_repeticiones = 1000
figus_total = 6
resultados = [cuantas_figus(figus_total) for _ in range(n_repeticiones)]
probabilidad = np.mean(resultados)
print(f'Podemos estimar que para llenar un album de {figus_total} figuritas hay que comprar en promedio {probabilidad:.2f} figuritas.')
# Ejemplo output: Podemos estimar que para llenar un album de 6 figuritas hay que comprar en promedio 15.08 figuritas
