import csv


def leer_archivo(archivo):
    f = open(archivo, 'rt')
    rows = csv.reader(f)
    next(f)
    return rows


def costo_camion(nombre_archivo):
    costo_total = 0.0
    rows = leer_archivo(nombre_archivo)
    for n_fila, fila in enumerate(rows, start=1):
        try:
            _, cajones, precio = fila
            costo_total = costo_total + int(cajones) * float(precio.rstrip())
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')
            continue
    return costo_total

costo = costo_camion('../Data/missing.csv')

print("Costo total: {}".format(costo))
# Costo total: 47671.15
