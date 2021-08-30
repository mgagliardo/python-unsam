def minimo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = lista[0] # Lo inicializo en el elemento con index 0 de la lista
    for e in lista: # Recorro la lista y voy guardando el mayor
        if m > e:
            m = e
    return m

def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = 0 # Lo inicializo en 0
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e > m:
            m = e
    return m

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

lista_muestra = [1,2,3,2,3,4]

#### buscar_u_elemento

# buscar_u_elemento(lista_muestra, 1)
# 0

# buscar_u_elemento(lista_muestra, 2)
# 3

# buscar_u_elemento(lista_muestra, 3)
# 4

# buscar_u_elemento(lista_muestra, 5)
# -1


#### buscar_n_elemento

# buscar_n_elemento(lista_muestra, 1)
# 1

# buscar_n_elemento(lista_muestra, 2)
# 2

# buscar_n_elemento(lista_muestra, 3)
# 2

# buscar_n_elemento(lista_muestra, 5)
# 0


#### maximo

# maximo([1,2,7,2,3,4])
# 7

# maximo([1,2,3,4])
# 4

# maximo([-5,4])
# 4

# maximo([-5,-4])
# 0


#### minimo

# minimo([1,2,7,2,3,4])
# 1

# minimo([1,2,3,4])
# 1

# minimo([-5,4])
# -5
