from vigilante import vigilar
import csv


def filtrar_datos(rows, nombres):
    for row in rows:
        if row['nombre'] in nombres:
            yield row

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index].strip() for index in indices]

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

def ticker(camion_file, log_file, fmt="txt"):
    import informe_final
    from formato_tabla import crear_formateador
    camion = informe_final.leer_camion(camion_file)
    rows = parsear_datos(vigilar(log_file))
    rows = filtrar_datos(rows, camion)
    formateador = crear_formateador(fmt)
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
    for row in rows:
        formateador.fila(row.values())

if __name__ == '__main__':
    camion_file = '../Data/camion.csv'
    log_file = '../Data/mercadolog.csv'
    fmt = 'txt'
    ticker(camion_file, log_file, fmt)
