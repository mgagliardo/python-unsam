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

# 3.22
def obtener_inclinaciones(lista_arboles, especie):
    inclinacion_max = 0
    for arbol in lista_arboles:
        if especie in arbol['nombre_com']:
            inclinacion_arbol = float(arbol['inclinacio'])
            if inclinacion_arbol > inclinacion_max:
                inclinacion_max = inclinacion_arbol
    return inclinacion_max

# nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'

# lista_arboles = leer_parque(nombre_archivo, "GENERAL PAZ")
# pprint(obtener_inclinaciones(lista_arboles, 'Casuarina'))
