def propagar(vector):
    hubo_cambios = 0
    # Creo una copia exacta de la lista
    # Pero que no tiene el mismo puntero
    # Que la lista original
    vector_nuevo = vector[:]
    length = len(vector_nuevo)
    for ind, elem in enumerate(vector_nuevo):
        if elem == 1:
            # Si no estamos en el indice = 0
            # Y si el elemento del indice anterior es 0
            # Prende fuego el fosforo
            # Marca la variable `hubo_cambios`
            if (ind != 0) and (vector[ind - 1] == 0):
                vector_nuevo[ind-1] = 1
                hubo_cambios = 1
            # Si el indice posterior no es el último (length)
            # Y si el elemento del indice posterior es 0
            # Prende fuego el fosforo
            # Marca la variable `hubo_cambios`
            if (ind + 1 < length) and (vector[ind + 1] == 0):
                vector_nuevo[ind + 1] = 1
                hubo_cambios = 1
    # Si hubo cambios en la funcion
    # Es necesario corroborar si debe haber mas
    # Llamada recursiva a la funcion (se llama a si misma)
    if hubo_cambios:
        return propagar(vector_nuevo)
    return vector_nuevo


lista_1 = [0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]
# propagar(lista_1)
# [0, 0, 0, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1]

lista_2 = [ 0, 0, 0, 1, 0, 0]
# propagar([ 0, 0, 0, 1, 0, 0])
# [1, 1, 1, 1, 1, 1]
