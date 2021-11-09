import matplotlib.pyplot as plt
import numpy as np


def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
        comparaciones = 0
    else:
        medio = len(lista) // 2
        izq, comp_izq = merge_sort(lista[:medio])
        der, comp_der = merge_sort(lista[medio:])
        lista_nueva, comp_nueva = merge(izq, der)
        comparaciones = comp_izq + comp_der + comp_nueva
    return lista_nueva, comparaciones

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    comparaciones = 0
    while(i < len(lista1) and j < len(lista2)):
        comparaciones += 2
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    # Agregar lo que falta de una lista
    resultado = resultado + lista1[i:]
    resultado = resultado + lista2[j:]
    return resultado, comparaciones

def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    comparaciones = 0
    # posición final del segmento a tratar
    n = len(lista) - 1

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p, comp = buscar_max(lista, 0, n)
        comparaciones += comp

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]

        # reducir el segmento en 1
        n = n - 1
    return comparaciones

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max, b - a

def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    comparaciones = 0
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        comparaciones += 1
        if lista[i + 1] < lista[i]:
            comparaciones += reubicar(lista, i + 1)
    return comparaciones

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""
    comparaciones = 0
    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p

    while j > 0 and v < lista[j - 1]:
        comparaciones += 1
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1
    
    # Sumo una comparacion que corresponde a la entrada del while
    # Si es que no ingreso en el while
    if comparaciones == 0:
        comparaciones += 1
    lista[j] = v
    return comparaciones

def ord_burbujeo(lista):
    """
        Recibe una lista y la ordena utilizando ordenamiento burbuja
        Su complejidad es O(N^2), donde N es len(lista)
    """
    comparaciones = 0
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1 - i):
            comparaciones += 1 
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return comparaciones

def generar_lista(N):
    return np.random.choice(range(1, 1001), size=N, replace=True)

def generar_listas(Nmax):
    l = [generar_lista(e) for e, _ in enumerate(range((Nmax)), start= 1)]
    return l

def experimento(N, k):
    ops_seleccion = 0.0
    ops_insercion = 0.0
    ops_burbujeo = 0.0
    ops_merge_sort = 0.0

    for lista in generar_listas(k):
        ops_seleccion += ord_seleccion(lista.copy())
        ops_insercion += ord_insercion(lista.copy())
        ops_burbujeo += ord_burbujeo(lista.copy())
        _, merge_sort_res = merge_sort(lista.copy())
        ops_merge_sort = merge_sort_res + ops_merge_sort

    return (
        ops_seleccion/k,
        ops_insercion/k,
        ops_burbujeo/k,
        ops_merge_sort/k
    )

def experimento_vectores(Nmax):
    comparaciones_seleccion = np.zeros(Nmax)
    comparaciones_insercion = np.zeros(Nmax)
    comparaciones_burbujeo = np.zeros(Nmax)
    comparaciones_merge_sort = np.zeros(Nmax)

    for i in range(Nmax):
        comp_sel, comp_ins, comp_burb, comp_merge_sort = experimento(Nmax, i+1)
        comparaciones_seleccion[i] += comp_sel
        comparaciones_insercion[i] += comp_ins
        comparaciones_burbujeo[i] += comp_burb
        comparaciones_merge_sort[i] += comp_merge_sort
    
    return comparaciones_seleccion, comparaciones_insercion, comparaciones_burbujeo, comparaciones_merge_sort


# if __name__ == '__main__':
#     Nmax = 100
#     comparaciones_seleccion, comparaciones_insercion, comparaciones_burbujeo, comparaciones_merge_sort = experimento_vectores(Nmax)
#     rango = np.arange(Nmax) + 1
#     plt.plot(rango, comparaciones_seleccion, color='blue', label = 'Ordenamiento Seleccion')
#     plt.plot(rango, comparaciones_insercion, color='green', label = 'Ordenamiento Insercion')
#     plt.plot(rango, comparaciones_burbujeo, color='red', label = 'Ordenamiento Burbujeo')
#     plt.plot(rango, comparaciones_merge_sort, color='magenta', label = 'Ordenamiento Merge Sort')
#     plt.xlabel("Largo de la lista")
#     plt.ylabel("Cantidad de comparaciones")
#     plt.title("Complejidad del algoritmo")
#     plt.legend()
#     plt.show()
