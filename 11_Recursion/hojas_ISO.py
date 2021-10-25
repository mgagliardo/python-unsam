def medidas_hoja_A(N):
    """Devuelve el ancho y largo de la hoja A(N) calculada"""
    if N == 0:
        return (841, 1189)
    elif N < 0:
        return "Error, ingrese un tipo de hoja valido."

    if N % 2 == 0:
        res = tuple(int(n / N) for n in medidas_hoja_A(N % 2))
    else:
        ancho, largo = medidas_hoja_A(N - 1)
        res = (int(largo / 2), ancho)

    return res
