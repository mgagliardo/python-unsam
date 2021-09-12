import csv

def parse_csv(nombre_archivo, select=None, types=None, has_headers=True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        fila = []
        registros = []
        rows = csv.reader(f)
        if has_headers:
            headers = select or next(rows)
        for row in rows:
            if not row:
                continue
            if types:
                fila = [func(val) for func, val in zip(types, row)]
            else:
                fila = row
            if has_headers:
                registro = dict(zip(headers, fila))
            else:
                registro = tuple(fila)
            registros.append(registro)
    return registros
