def invertir_lista(lista):
    '''Recibe una lista L y la develve invertida.'''
    invertida = []
    i = len(lista)
    while i > 0:    # tomo el último elemento 
        i = i-1
        invertida.append(lista.pop(i))  #
    return invertida

def invertir_lista(lista):
    invertida = []
    for e in lista: # Recorro la lista
        invertida.append()
        invertida.append(e) #agrego el elemento e al principio de la lista invertida
        if len(invertida) > 1:
            invertida.append(ind(e)-1)
    return invertida
