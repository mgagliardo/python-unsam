import csv


def leer_archivo(archivo):
    f = open(archivo, 'rt')
    rows = csv.reader(f)
    next(f)
    return rows


def costo_camion(nombre_archivo):
    costo_total = 0.0
    rows = leer_archivo(nombre_archivo)
    for line in rows:
        _, cajones, precio = line
        costo_total = costo_total + int(cajones) * float(precio.rstrip())
    return costo_total

costo = costo_camion('../Data/camion.csv')

print("Costo total: {}".format(costo))
# Costo total: 47671.15
