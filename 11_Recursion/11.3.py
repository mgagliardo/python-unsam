def cant_digitos(n):
    if n < 10:
        return 1

    nuevo = n / 10
    return 1 + cant_digitos(nuevo)
