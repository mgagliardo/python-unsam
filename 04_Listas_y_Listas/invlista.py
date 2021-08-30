def invertir_lista(lista):
    '''Recibe una lista y la develve invertida.'''
    length = len(lista)
    invertida = [None]*length
    for e in lista:
        length = length - 1
        invertida[length] = e
    return invertida

lista_num = [1, 2, 3, 4, 5]
print(invertir_lista(lista_num))

lista_ciudades = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
print(invertir_lista(lista_ciudades))
