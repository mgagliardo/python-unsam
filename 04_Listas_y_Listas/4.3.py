def buscar_n_elemento(lista, elemento):
    apariciones = 0
    for elem in lista:
        if elem == elemento:
            apariciones += 1
    return apariciones

def buscar_u_elemento(lista, elemento):
    ultima_pos = -1
    for ind, elem in enumerate(lista):
        if elem == elemento:
            ultima_pos = ind
    return ultima_pos

#### buscar_u_elemento

# print(buscar_u_elemento([1,2,3,2,3,4],1))
# 0

# buscar_u_elemento([1,2,3,2,3,4],2)
# 3

# buscar_u_elemento([1,2,3,2,3,4],3)
# 4

# buscar_u_elemento([1,2,3,2,3,4],5)
# -1


#### buscar_n_elemento

# print(buscar_n_elemento([1,2,3,2,3,4],1))
# 1

# buscar_n_elemento([1,2,3,2,3,4],2)
# 2

# buscar_n_elemento([1,2,3,2,3,4],3)
# 2

# buscar_n_elemento([1,2,3,2,3,4],5)
# 0
