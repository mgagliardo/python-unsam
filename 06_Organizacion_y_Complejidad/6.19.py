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
