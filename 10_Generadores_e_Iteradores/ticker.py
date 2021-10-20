import csv
from vigilante import vigilar


def hace_dicts(rows, headers):
    return (dict(zip(headers, row)) for row in rows)

def elegir_columnas(rows, indices):
    return ((row[index].strip() for index in indices) for row in rows)

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
    rows = (row for row in rows if row['nombre'] in camion)
    formateador = crear_formateador(fmt)
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
    for row in rows:
        formateador.fila(row.values())

# if __name__ == '__main__':
#     camion_file = '../Data/camion.csv'
#     log_file = '../Data/mercadolog.csv'
#     fmt = 'txt'
#     ticker(camion_file, log_file, fmt)
