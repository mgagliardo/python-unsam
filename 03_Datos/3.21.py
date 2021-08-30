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

# 3.21
def contar_ejemplares(lista_arboles, especie):
    contador_arboles = Counter()
    for arbol in lista_arboles:
        if especie in arbol['nombre_com']:
            contador_arboles[arbol['nombre_com']] += 1
    return contador_arboles

def obtener_alturas(lista_arboles, especie):
    contador_alturas = Counter()
    altura_max = 0
    for arbol in lista_arboles:
        nombre_arbol = arbol['nombre_com']
        if especie in nombre_arbol:
            altura_arbol = float(arbol['altura_tot'])
            contador_alturas[nombre_arbol] += altura_arbol
            if altura_arbol > altura_max:
                altura_max = altura_arbol
    total_ejemplares = contar_ejemplares(lista_arboles, especie)
    promedio_alturas = float(contador_alturas.get(especie) / total_ejemplares.get(especie))
    return altura_max, promedio_alturas

# nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'

# lista_arboles = leer_parque(nombre_archivo, "GENERAL PAZ")
# pprint(obtener_alturas(lista_arboles, 'Casuarina'))
