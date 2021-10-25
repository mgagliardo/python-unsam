def maximo(lista):
    if len(lista) == 1:
        return lista[0]
    if lista[0] > lista[1]:
        lista.pop(lista.index(lista[1]))
    else:
        lista.pop(lista.index(lista[0]))
    return maximo(lista)
