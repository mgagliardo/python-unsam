import numpy as np
import random


def medir_temp(n):
    temperaturas = []
    for _ in range(n):
        temperaturas.append(round(random.normalvariate(37.5, 0.2), 3))
    return temperaturas

def resumen_temp(n):
    temperaturas = medir_temp(n)
    temperatura_max = max(temperaturas)
    temperatura_min = min(temperaturas)
    temperatura_prom = round(sum(temperaturas) / n, 3)
    temperatura_mediana = np.median(temperaturas)
    return (temperatura_max, temperatura_min, temperatura_prom, temperatura_mediana)


print(resumen_temp(10000))
