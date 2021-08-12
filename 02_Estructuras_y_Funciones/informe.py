import csv

from pprint import pprint


def leer_precios(nombre_archivo):
    precios = {}
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if row:
                precios[row[0]] = row[1]
    return precios

def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            lote = { 'nombre': row[0], 'cajones': int(row[1]), 'precio': float(row[2]) }
            camion.append(lote)
    return camion


camion = leer_camion('../data/Data/camion.csv')
pprint(camion)
precios = leer_precios("../data/Data/precios.csv")
print(precios)


total = 0.0
for s in camion:
    total += s['cajones']*s['precio']

print(total)

