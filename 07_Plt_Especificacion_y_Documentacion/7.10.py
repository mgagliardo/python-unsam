def valor_absoluto(numero):
    '''Devuelve el valor absoluto de un numero
    
    Pre: Un numero entero
    Pos: Se devuelve el valor absoluto de dicho numero
    '''
    if numero >= 0:
        return numero
    else:
        return -numero

def suma_pares(lista_numeros):
    '''Devuelve la suma de los numeros pares de una lista dada

    Pre: Una lista de numeros enteros
    Pos: Se devuelve el resultado de la sumatoria de los pares de la lista dada
    '''
    res = 0
    for e in lista_numeros:
        if e % 2 == 0:
            res += e
        else:
            res += 0
    return res

def veces(a, b):
    '''Devuelve el resultado de multiplicar el primer numero a
       por el segundo numero b
    
    Pre: Un primer numero entero y un segundo numero natural
    Pos: Se devuelve el resultado de multiplicar ambos numeros.
    '''
    if not b < 0:
        res = 0
        nb = b
        while nb != 0:
            res += a
            nb -= 1
        return res
    return None

'''
Comentario del alumno:

Para hacerlo correctamente deberia ser:

def multiplicar(primer_numero, segundo_numero):
    # Devuelve el resultado de multiplicar el primer_numero
    # por el segundo_numero
    
    # Pre: Dos numeros enteros
    # Pos: Se devuelve el resultado de multiplicar ambos numeros.
    res = 0
    nb = segundo_numero
    while nb != 0:
        if nb > 0:
            res += primer_numero
            nb -= 1
        else:
            res -= primer_numero
            nb += 1
    return res
'''


def collatz(n):
    '''Devuelve la cantidad de pasos (o sucesiones) para lograr la conjetura de Collatz
       https://es.wikipedia.org/wiki/Conjetura_de_Collatz
    
    Pre: Un numero entero positivo
    Pos: Un numero entero positivo representativo de la Conjetura de Collatz
    '''
    res = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        res += 1
    return res
