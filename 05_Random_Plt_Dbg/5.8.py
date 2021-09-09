import numpy as np
import random


def medir_temp(n):
    temperaturas = np.empty((n,))
    for i in range(n):
        temperaturas[i] = round(random.normalvariate(37.5, 0.2), 3)
    print(temperaturas)
    np.save('../Data/temperaturas.npy', temperaturas)
    return temperaturas

def resumen_temp(n):
    temperaturas = medir_temp(n)
    temperatura_max = max(temperaturas)
    temperatura_min = min(temperaturas)
    temperatura_prom = round(sum(temperaturas) / n, 3)
    temperatura_mediana = np.median(temperaturas)
    return (temperatura_max, temperatura_min, temperatura_prom, temperatura_mediana)

n = 999
tupla_temp = resumen_temp(999)
print(tupla_temp)
