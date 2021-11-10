import matplotlib.pyplot as plt
import numpy as np
import timeit as tt


def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        lista_nueva = merge(izq, der)
    return lista_nueva

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado = resultado + lista1[i:]
    resultado = resultado + lista2[j:]

    return resultado


def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]

        # reducir el segmento en 1
        n = n - 1

    return lista

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max

def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)

    return lista

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v

def ord_burbujeo(lista):
    """
        Recibe una lista y la ordena utilizando ordenamiento burbuja
        Su complejidad es O(N^2), donde N es len(lista)
    """
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1 - i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def generar_lista(N):
    return np.random.choice(range(1, 1001), size=N, replace=True)

def generar_listas(Nmax):
    return [generar_lista(e) for e, _ in enumerate(range((Nmax)), start= 1)]

def experimento_timeit(Nmax):
    time_seleccion = np.zeros(Nmax)
    time_insercion = np.zeros(Nmax)
    time_burbujeo = np.zeros(Nmax)
    time_merge_sort = np.zeros(Nmax)

    num = 1
    listas = generar_listas(Nmax)
    
    global lista
    for i, lista in enumerate(listas):
        time_seleccion[i] = tt.timeit('ord_seleccion(lista.copy())', number=num, globals=globals())
        time_insercion[i] = tt.timeit('ord_insercion(lista.copy())', number=num, globals=globals())
        time_burbujeo[i] = tt.timeit('ord_burbujeo(lista.copy())', number=num, globals=globals())
        time_merge_sort[i] = tt.timeit('merge_sort(lista.copy())', number=num, globals=globals())

    return time_seleccion, time_insercion, time_burbujeo, time_merge_sort


if __name__ == '__main__':
    Nmax = 100
    time_seleccion, time_insercion, time_burbujeo, time_merge_sort = experimento_timeit(Nmax)
    rango = np.arange(Nmax) + 1
    plt.plot(rango, time_seleccion, color='blue', label = 'Ordenamiento Seleccion')
    plt.plot(rango, time_insercion, color='green', label = 'Ordenamiento Insercion')
    plt.plot(rango, time_burbujeo, color='red', label = 'Ordenamiento Burbujeo')
    plt.plot(rango, time_merge_sort, color='magenta', label = 'Ordenamiento Merge Sort')
    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Complejidad del algoritmo")
    plt.legend()
    plt.show()
