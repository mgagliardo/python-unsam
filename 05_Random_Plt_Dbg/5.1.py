import random

def tirar():
    dados = []
    for _ in range(5):
        dados.append(random.randint(1,6))
    return dados

def es_generala(tirada):
    # Convierto la lista a un set
    # Si hay repetidos el len() de la lista va a ser > 1
    # Si son todos iguales el len() va a ser exactamente == 1
    return len(tirada) == 5 and len(set(tirada)) == 1

N = 100000
G = sum([es_generala(tirar()) for _ in range(N)])   
prob = G/N
# print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
# print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
