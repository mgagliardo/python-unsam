import csv


def leer_archivo(archivo):
    f = open(archivo, 'rt')
    rows = csv.reader(f)
    next(f)
    return rows


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

total = 0.0
for s in camion:
    total += s['cajones']*s['precio']

print(total)
