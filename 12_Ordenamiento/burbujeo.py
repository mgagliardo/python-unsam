def ord_burbujeo(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1 - i):
            if lista[j] > lista[j+1]:
                tmp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = tmp
    return lista

def ord_burbujeo_recursivo(lista):
    