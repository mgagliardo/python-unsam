def triangular(n):
    """Devuelve el n-esimo numero triangular."""
    if n == 1:
        return n

    t = triangular(n - 1)
    return n + t
