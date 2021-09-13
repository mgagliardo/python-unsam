def busqueda_lineal(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1
    for i, z in enumerate(lista):
        if z == e:
            pos = i
            break
    return pos


def busqueda_lineal_lordenada(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1
    for i, z in enumerate(lista):
        if z == e:
            pos = i
            break
    return pos
