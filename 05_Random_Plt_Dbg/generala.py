import random


def tirar(cant_dados):
    return random.choices(range(1,6), k=cant_dados)

def es_generala(tirada):
    # Convierto la lista a un set
    # Si hay repetidos el len() de la lista va a ser > 1
    # Si son todos iguales el len() va a ser exactamente == 1
    return len(tirada) == 5 and len(set(tirada)) == 1

def contar_dados_repetidos(dados):
    # Crea un diccionario con los numeros y su cantidad de repeticiones
    # Ej.: {1: 0, 2: 1, 3: 2, 4: 1, 5: 1}
    dados_contados = {}
    for d in range(1, 6):
        if dados.count(d) > 1:
            dados_contados[d] = dados.count(d)
            return dados_contados

def sacar_dados_repetidos(dados_en_mesa, nro_dado):
    # Devuelve una lista que no contiene al dado `nro_dado`
    dados_sin_repetir = [d for d in dados_en_mesa if d != nro_dado]
    return dados_sin_repetir

def repetir_3_tiradas():
    # dados_repetidos se usara para agregar
    # la cantidad de repeticiones de un dado
    # Ej. [1, 1, 1, 1]
    dados_repetidos = []
    # Tiro 5 siempre la primera vez
    dados_en_mesa = tirar(5)
    for _ in range(3):  
        # Devuelvo en un dict la cantidad de apariciones de c/dado
        dict_dados_repetidos = contar_dados_repetidos(dados_en_mesa)
        for nro_dado, cant_repeticiones in dict_dados_repetidos.items():
            # Tomo el primer dado que haya salido mas de una vez repetido
            if cant_repeticiones > 1:
                # Si la lista esta vacia o el numero de dado ya se encuentra
                # Entre los repetidos (ya lo separe antes)
                if len(dados_repetidos) == 0 or nro_dado in dados_repetidos:
                    # Agrego el la cantidad de veces que haya aparecido
                    for _ in range(cant_repeticiones):
                        dados_repetidos.append(nro_dado)
                    # Separo los otros dados en la mesa
                    dados_en_mesa = sacar_dados_repetidos(dados_en_mesa, nro_dado)
                    break
                # Si el nro_dado no aparece > 1 vez, continuo con el siguiente
                else:
        # Vuelvo a tirar los dados solo la cantidad que "me sobran"
                    continue
        dados_en_mesa = tirar(len(dados_en_mesa))
    return es_generala(dados_repetidos)

def prob_generala(N):
    G = sum([repetir_3_tiradas() for _ in range(N)])   
    prob = G/N
    return prob

# Cantidad de veces
N = 10000
prob = prob_generala(N)


# print(f'Podemos estimar la probabilidad de hacer una generala de a 3 tiradas mediante {prob:.4f}.')
# Podemos estimar la probabilidad de hacer una generala de a 3 tiradas mediante 0.0301.
