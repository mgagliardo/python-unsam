def es_potencia(n, b):
    if n == 1: # Donde por ej 2 ^ 0 == 1
        return True
    if n < b:
        return n == 1
    return es_potencia(n / b, b)
