import random

def tirar(cant_dados):
    return [random.randint(1,6) for _ in range(cant_dados)]

def es_generala(tirada):
    # Convierto la lista a un set
    # Si hay repetidos el len() de la lista va a ser > 1
    # Si son todos iguales el len() va a ser exactamente == 1
    return len(set(tirada)) == 1

def contar_dados_repetidos(dados):
    dados_contados = {}
    for d in range(1, 6):
        dados_contados[d] = dados.count(d) > 1
    return dados_contados

def repetir_3_tiradas():
    # Inicio con 5 dados
    dado_repetido = 0
    dados_en_mesa = tirar(5)
    # range(2) dado que ya tire la primera vez
    for _ in range(2):
        print(f'dados_en_mesa: {dados_en_mesa}')
        dados_contados = contar_dados_repetidos(dados_en_mesa)
        print(f'dados_contados: {dados_contados}')
        for nro_dado, esta_repetido in dados_contados.items():
            # Busca el dado que haya salido mas de una vez
            if esta_repetido:
                if nro_dado == dado_repetido:
                    # Remueve todos los dados que estan repetidos
                    dados_sin_repetir = [d for d in dados_en_mesa if d != nro_dado]
                    print(f'dados_sin_repetir: {dados_sin_repetir}')
                    dados_en_mesa = tirar(len(dados_sin_repetir))
                    break
                else:
                    continue
    return es_generala(dados_en_mesa)




def prob_generala(N):
    G = 0
    for _ in range(N):

            




        G += sum()...
        
        if i < N - 1:
            (cant, valor) = contar_dados_repetidos(mesa)[0]
            mesa = [valor] * cant
            print(mesa)
            
    # G = sum([es_generala(tirar()) for _ in range(N)])
    # prob = G/N
    # print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
    # print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
    return 

N = 3
print(prob_generala(N)))




# G = sum([es_generala(tirar()) for _ in range(N)])
# print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
