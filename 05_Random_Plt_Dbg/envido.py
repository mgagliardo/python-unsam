import random


def generar_mazo():
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ['oro', 'copa', 'espada', 'basto']
    naipes = [(valor,palo) for valor in valores for palo in palos]
    random.shuffle(naipes)
    return naipes

def probabilidad_envido(puntos):
    cartas = random.choices(generar_mazo(), k=3)
    # Siempre empieza con base 20.
    puntaje_envido = 20
    # Sumo solo si no son rey, caballo o sota.
    cartas_10_11_12 = [10, 11, 12]
    puntaje_envido += sum([elem[0] for elem in cartas if elem[0] not in cartas_10_11_12])
    return puntaje_envido == puntos


N = 100000
for puntos in [31, 32, 33]:
    G = sum([probabilidad_envido(puntos) for _ in range(N)])
    print(f'Experimentando {N} veces, la cantidad de veces que dio {puntos} puntos de envido fue de {G}.')
    print(f'Podemos estimar la probabilidad de obtener {puntos} de envido es de {G/N:.4f}.\n')
