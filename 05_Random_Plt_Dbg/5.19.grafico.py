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
    while album_incompleto(nuevo_album):
        figus = comprar_paquete(figus_total, figus_paquete)
        contador += 1
        for figu in figus:
            nuevo_album[figu] = 1
    return contador

# 5.15
def experimento_figus(n_repeticiones, figus_total, figus_paquete):
    resultados = [cuantos_paquetes(figus_total, figus_paquete) for _ in range(n_repeticiones)]
    return np.mean(resultados)

# 5.20
def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

figus_total = 670
figus_paquete = 5

print(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()
