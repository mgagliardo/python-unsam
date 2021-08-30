def invertir_lista(lista):
    '''Recibe una lista y la develve invertida.'''
    length = len(lista)
    # Lleno la lista con el ancho de elementos None
    # O sea, defino el tamaño de la lista para que sea el mismo
    # Que la original
    invertida = [ None ] * length
    for e in lista:
        # Empiezo por el último elemento
        # Y voy descontando hasta 0
        length = length - 1
        invertida[length] = e
    return invertida

lista_num = [1, 2, 3, 4, 5]
# invertir_lista(lista_num)
# [ 5,4,3,2,1 ]

lista_ciudades = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
# invertir_lista(lista_ciudades)
# ['San Miguel', 'San Fernando', 'Santiago', 'Rosario', 'Bogotá']
