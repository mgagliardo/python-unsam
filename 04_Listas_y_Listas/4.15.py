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

nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
arboleda = leer_arboles(nombre_archivo)

# pprint(arboleda)
# No pongo el output ya que es demasiado largo
