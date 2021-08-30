import csv
from collections import Counter
from pprint import pprint

def leer_parque(nombre_archivo, parque):
    arboles_parque = []
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        for n_fila, fila in enumerate(filas, start=1):
            arbol = dict(zip(encabezados, fila))
            try:
                # Dado que todos los nombres son en uppercase
                # Se asegura que la comparacion sea parcial y en uppercase para ambos
                # Ejemplo, parque avellaneda es "AVELLANEDA, NICOLÁS, Pres." 
                if parque.upper() in arbol['espacio_ve'].upper():
                    arboles_parque.append(arbol)
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
                continue
    return arboles_parque

# 3.20
def contar_ejemplares(lista_arboles):
    contador_arboles = Counter()
    for arbol in lista_arboles:
        contador_arboles[arbol['nombre_com']] += 1
    return contador_arboles


# nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'

# lista_arboles = leer_parque(nombre_archivo, "GENERAL PAZ")
# pprint(contar_ejemplares(lista_arboles).most_common(5))

# lista_arboles = leer_parque(nombre_archivo, "ANDES, LOS")
# pprint(contar_ejemplares(lista_arboles).most_common(5))

# lista_arboles = leer_parque(nombre_archivo, "CENTENARIO")
# pprint(contar_ejemplares(lista_arboles).most_common(5))
