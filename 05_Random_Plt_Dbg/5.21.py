import matplotlib.pyplot as plt
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

# 5.17
def comprar_paquete(figus_total, figus_paquete):
    return [comprar_figu(figus_total) for _ in range(figus_paquete)]

# 5.18
def cuantos_paquetes(figus_total, figus_paquete):
    contador = 0
    nuevo_album = crear_album(figus_total)
    array_figus_total = np.array([])
    while album_incompleto(nuevo_album):
        figus = comprar_paquete(figus_total, figus_paquete)
        array_figus_total = np.append(array_figus_total, figus)
        contador += 1
        for figu in figus:
            nuevo_album[figu] = 1
    np.save('../Data/figus.npy', array_figus_total)
    return contador

# 5.15
def experimento_figus(n_repeticiones, figus_total, figus_paquete):
    resultados = [cuantos_paquetes(figus_total, figus_paquete) for _ in range(n_repeticiones)]
    return np.mean(resultados)

def plotear_figuritas():
    figuritas = np.load('../Data/figus.npy')
    plt.hist(figuritas, bins=50)
    plt.show()


n_repeticiones = 100
figus_total = 670
figus_paquete = 5
probabilidad = experimento_figus(n_repeticiones, figus_total, figus_paquete)

print(f'Podemos estimar que para llenar un album de {figus_total} figuritas hay que comprar en promedio {probabilidad:.2f} paquetes.')
plotear_figuritas()
