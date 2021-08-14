import csv


def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            lote = { 'nombre': row[0], 'cajones': int(row[1]), 'precio': float(row[2]) }
            camion.append(lote)
    return camion


def costo_camion(cajones_camion):
    costo_total_camion = 0.0
    for cajon in cajones_camion:
        costo_total_camion += cajon['cajones'] * cajon['precio']
    return costo_total_camion


def leer_precios(nombre_archivo):
    precios = {}
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if row:
                precios[row[0]] = row[1]
    return precios


def calcular_recaudacion(nombre_archivo, cajones_camion):
    recaudacion = 0.0    
    precios_fruta = leer_precios(nombre_archivo)
    for cajon in cajones_camion:
        nombre_fruta = cajon['nombre']
        if cajon['nombre'] in precios_fruta.keys():
            recaudacion += int(cajon['cajones']) * float(precios_fruta[nombre_fruta])
    return recaudacion


def evaluar_diferencia(recaudacion, costo):
    diferencia = recaudacion - costo
    if diferencia > 0:
        print("Hubo ganancia!: ${}".format(round(diferencia, 2)))
    elif diferencia == 0:
        print("La recaudacion fue neutra: ${}".format(round(diferencia, 2)))
    else:
        print("Uyy, hubo perdida!: ${}".format(round(diferencia, 2)))


cajones_camion = leer_camion('../Data/camion.csv')
costo_total_camion = costo_camion(cajones_camion)
print("Costo del camion: ${}".format(round(costo_total_camion, 2)))

recaudacion = calcular_recaudacion("../Data/precios.csv", cajones_camion)
print("Recaudacion de la venta: ${}".format(round(recaudacion, 2)))

evaluar_diferencia(recaudacion, costo_total_camion)

# Output:
# Costo del camion: $47671.15
# Recaudacion de la venta: $62986.1
# Hubo ganancia!: $15314.95
