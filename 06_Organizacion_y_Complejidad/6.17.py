def incrementar(s):
    carry = 1
    l = len(s)
    
    # Es una funcion lineal
    # Recorre la lista de 1 en 1 de manera reversa
    for i in range(l-1,-1,-1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    return s
