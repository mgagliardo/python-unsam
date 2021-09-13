def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            return medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return izq

def donde_insertar(lista, x):
    return busqueda_binaria(lista, x)

def insertar(lista, x):
    posicion_en_lista = donde_insertar(lista, x)
    if posicion_en_lista == len(lista): # Catch si el índice está fuera de la lista
        lista.append(x)
    else:
        if lista[posicion_en_lista] != x:
            lista.insert(posicion_en_lista, x)
    return posicion_en_lista
