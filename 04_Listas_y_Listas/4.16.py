import csv
from pprint import pprint

def leer_arboles(nombre_archivo):
    arboleda = []
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        for fila in filas:
            arbol = dict(zip(encabezados, fila))
            arboleda.append(arbol)
    return arboleda

def lista_alturas(arboleda, nombre_arbol):
    return [ float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == nombre_arbol ]


nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
arboleda = leer_arboles(nombre_archivo)

nombre_arbol = 'Jacarandá'
lista_comprension_jacaranda = lista_alturas(arboleda, nombre_arbol)

# pprint(lista_comprension_jacaranda)
# No pongo el output ya que es demasiado largo
