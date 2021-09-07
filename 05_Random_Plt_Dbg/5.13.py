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
    # Devuelvo * 5 dado que es la cantidad de figuritas
    return contador


# 5.13
total_figus_album = 30
paquetes_para_llenar_album = cuantas_figus(total_figus_album)
print(f"Para completar un album de {total_figus_album} figuritas hizo falta comprar {paquetes_para_llenar_album} paquetes de figuritas")
# Ejemplo del output: Para completar un album de 30 figuritas hizo falta comprar 153 paquetes de figuritas
