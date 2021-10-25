def pascal(n, k):
    """Devuelve el elemento n, k del triangulo de pascal"""
    def triangulo_pascal(n):
        """Devuelve en una matriz de `n` elementos el triangulo de pascal armado"""
        if n == 0:
            return []
        elif n == 1:
            return [[1]]
        else:
            nueva_fila = [1]
            res = triangulo_pascal(n - 1)
            ultima_fila = res[-1]
            for i in range(len(ultima_fila) - 1):
                nueva_fila.append(ultima_fila[i] + ultima_fila[i+1])
            nueva_fila += [1]
            res.append(nueva_fila)
        return res
    return triangulo_pascal(n+1)[n][k]
