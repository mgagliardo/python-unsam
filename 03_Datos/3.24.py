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

# 3.23
def especies(lista_arboles):
    conjunto_especies = set()
    for arbol in lista_arboles:
        conjunto_especies.add(arbol['nombre_com'])
    return conjunto_especies

def contar_ejemplares(lista_arboles):
    contador_arboles = Counter()
    for arbol in lista_arboles:
        contador_arboles[arbol['nombre_com']] += 1
    return contador_arboles

def obtener_inclinaciones_promedio(lista_arboles, especie):
    contador_inclinacion = Counter()
    for arbol in lista_arboles:
        nombre_arbol = arbol['nombre_com']
        if especie in nombre_arbol:
            inclinacio_arbol = float(arbol['inclinacio'])
            contador_inclinacion[nombre_arbol] += inclinacio_arbol
    total_ejemplares = contar_ejemplares(lista_arboles)
    promedio_inclinacion = float(contador_inclinacion.get(especie) / total_ejemplares.get(especie))
    return promedio_inclinacion

def especie_promedio_mas_inclinada(lista_arboles):
    inclinacion = 0
    especie_mas_inclinada = {}
    total_especies = especies(lista_arboles)
    for especie in total_especies:
        inclinacion_max = obtener_inclinaciones_promedio(lista_arboles, especie)
        if inclinacion_max > inclinacion:
            inclinacion = inclinacion_max
            especie_mas_inclinada = {especie: inclinacion_max}
    return especie_mas_inclinada

# nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'

# lista_arboles = leer_parque(nombre_archivo, "Los Andes")
# pprint(especie_promedio_mas_inclinada(lista_arboles))

# lista_arboles = leer_parque(nombre_archivo, "AVELLANEDA")
# pprint(especie_promedio_mas_inclinada(lista_arboles))
