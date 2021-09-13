import informe_funciones


def costo_camion(nombre_archivo):
    costo_total = 0.0
    filas = informe_funciones.leer_camion(nombre_archivo)
    for n_fila, record in enumerate(filas, start=1):
        try:
            ncajones = record['cajones']
            precio = record['precio']
            costo_total += ncajones * precio
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {record}')
            continue
    return costo_total


costo = costo_camion('../Data/fecha_camion.csv')
# print(f"Costo total $: {costo}")
# Costo total: 47671.15
