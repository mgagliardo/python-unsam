import csv
import sys

def leer_archivo(archivo):
    f = open(archivo, 'rt')
    rows = csv.reader(f)
    next(f)
    return rows


def leer_camion(nombre_archivo):
    costo_total = 0.0
    rows = leer_archivo(nombre_archivo)
    for line in rows:
        _, cajones, precio = line
        costo_total = costo_total + int(cajones) * float(precio.rstrip())
    return costo_total

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = leer_camion(nombre_archivo)
print("Costo total: {}".format(costo))

# Costo total: 47671.15
