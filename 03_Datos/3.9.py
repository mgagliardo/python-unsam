import csv


def costo_camion(nombre_archivo):
    costo_total = 0.0
    with open(nombre_archivo, "rt") as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(encabezados, fila))
            print(record)
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                costo_total += ncajones * precio
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
                continue
    return costo_total


costo = costo_camion('../Data/fecha_camion.csv')
# print(f"Costo total: {costo}")
# Costo total: 47671.15
