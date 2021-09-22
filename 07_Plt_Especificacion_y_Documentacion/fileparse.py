import csv

def parse_csv(file_obj, select=None, types=None, has_headers=True, silence_errors=False):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    filas = csv.reader(list(file_obj))
    if select and has_headers == False:
        raise RuntimeError("Para seleccionar, necesito encabezados.")
    if has_headers:
        encabezados = next(filas)
    if select and has_headers:
        indices = [encabezados.index(nombre_columna) for nombre_columna in select]
        encabezados = select
    else:
        indices = []
    registros = []
    for n_fila, fila in enumerate(filas):
        try:
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
        except ValueError as e:
            if not silence_errors:
                print(f"Fila {n_fila + 1}: No pude convertir {fila}")
                print(f"Fila {n_fila + 1}: Motivo: {e}")
            continue
        registros.append(registro)
    return registros
