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

def ord_burbujeo_recursivo(lista):
    """Recibe una lista y la ordena utilizando ordenamiento burbuja recursivamente"""

    def burbujeo_recursivo(lista, n):
        for i in range(len(lista) - 2):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]     
        if n > 1:
            burbujeo_recursivo(lista, n-1)
    
    return burbujeo_recursivo(lista, len(lista))


# if __name__ == '__main__':
#     lista = [10, 8, 6, 2, -2, -5]
#     ord_burbujeo(lista)
#     print(lista)    
# 
#     lista = [10, 8, 6, 2, -2, -5]    
#     ord_burbujeo_recursivo(lista)
#     print(lista)    
