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


def hacer_informe(lista_cajones, dict_precios):
    informe = []
    for cajon in lista_cajones:
        informe.append(
          tuple(cajon.values()) + (float(dict_precios[cajon['nombre']]),)
        )
    return informe


cajones_camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
informe = hacer_informe(cajones_camion, precios)
for r in informe:
    print(r)

# ('Lima', 100, 32.2, 40.22)
# ('Naranja', 50, 91.1, 106.28)
# ('Caqui', 150, 103.44, 105.46)
# ('Mandarina', 200, 51.23, 80.89)
# ('Durazno', 95, 40.37, 73.48)
# ('Mandarina', 50, 65.1, 80.89)
# ('Naranja', 100, 70.44, 106.28)
