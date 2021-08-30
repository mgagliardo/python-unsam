def propagar(vector):
    vector_nuevo = vector[:]
    length = len(vector_nuevo)
    for ind, elem in enumerate(vector_nuevo):
        if elem == 1:
            if (ind != 0) and (vector[ind - 1] == 0):
                vector_nuevo[ind-1] = 1
            if (ind + 1 < length) and (vector[ind + 1] == 0):
                vector_nuevo[ind + 1] = 1
    return vector_nuevo


lista_1 = [0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]
# propagar(lista_1)
# [0, 0, 0, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1]

lista_2 = [ 0, 0, 0, 1, 0, 0]
[ 1, 1, 1, 1, 1, 1]
print(propagar([ 0, 0, 0, 1, 0, 0]))
