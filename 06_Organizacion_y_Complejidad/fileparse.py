import csv

def parse_csv(nombre_archivo, select=None, types=None, has_headers=True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        if has_headers:
            encabezados = next(filas)
        if select and has_headers:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []
        registros = []
        for fila in filas:
            if not fila:
                continue
            if indices:
                fila = [fila[index] for index in indices]
            if types:
                fila = [func(val) for func, val in zip(types, fila) ]
            if has_headers:
                registro = dict(zip(encabezados, fila))
            else:
                registro = tuple(fila)
            registros.append(registro)

    return registros
