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
