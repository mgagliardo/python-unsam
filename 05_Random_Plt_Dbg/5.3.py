import random


def get_cumples_random(cant_personas, cant_dias):
    # Devuelvo 365 dias random de 1 a `cant_dias`
    # Loop la cantidad de personas que hayad
    cumples = random.choices(range(1,cant_dias), k=cant_personas)
    return cumples

def hay_duplicados(lista):
    # Guarda la lista en un set
    # Si hay duplicados, el len(set) va a ser menor al len(lisa)
    set_de_lista = set(lista)
    return len(lista) != len(set_de_lista)

def cumplen_mismo_dia(cant_personas, cant_dias):
    dias_de_cumpleanios = get_cumples_random(cant_personas, cant_dias)
    return hay_duplicados(dias_de_cumpleanios)

cant_personas = 30
cant_dias = 365
N = 100000
G = sum([cumplen_mismo_dia(cant_personas, cant_dias) for _ in range(N)])

print(f'Experimentando {N} veces, la cantidad de veces que salieron al menos 2 personas que cumplen el mismo dia fue de {G}')
print(f'Podemos estimar la probabilidad de que dos personas cumplan el mismo dia es de {G/N:.4f}.')
