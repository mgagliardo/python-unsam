import random
import matplotlib.pyplot as plt
import numpy as np


def generar_elemento(m):
    return random.randint(0, m-1)

def generar_lista(n, m):
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    comparaciones = 0
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            comparaciones += 1
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            comparaciones += 1
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            comparaciones += 1
            izq = medio + 1 # descarto mitad izquierda
    return pos, comparaciones

def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0
    pos = -1
    for i,z in enumerate(lista):
        comps += 1
        if z == x:
            pos = i
            break
    return pos, comps

def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for _ in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,x)[1]
    comps_prom = comps_tot / k
    return comps_prom

def experimento_binario_promedio(lista, m, k):
    comps_tot = 0
    for _ in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria(lista,x)[1]
    comps_prom = comps_tot / k
    return comps_prom

def graficar_bbin_vs_bseq(m, k):
    limit = 256
    largos = np.arange(limit) + 1
    comps_promedio_sec = np.zeros(limit)
    comps_promedio_bin = np.zeros(limit)
    for i, n in enumerate(largos):
        lista = generar_lista(n, m)
        comps_promedio_sec[i] = experimento_secuencial_promedio(lista, m, k)
        comps_promedio_bin[i] = experimento_binario_promedio(lista, m, k)

    plt.plot(largos, comps_promedio_sec, color='blue', label = 'Búsqueda Secuencial')
    plt.plot(largos, comps_promedio_bin, color='orange', label = 'Búsqueda Binaria')
    plt.xlim([0, limit + 10])
    plt.ylim([0, 50])
    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Complejidad de la Búsqueda")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    k = 1000
    m = 10000
    graficar_bbin_vs_bseq(m, k)
