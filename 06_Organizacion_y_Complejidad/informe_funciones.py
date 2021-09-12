import csv


def leer_camion(nombre_archivo):
    '''
    Lee precios de un archivo de datos CSV con dos columnas.
    La primera columna debe contener un nombre y la segunda un precio.
    '''
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        return [dict(zip(headers, row)) for row in rows]


def costo_camion(cajones_camion):
    costo_total_camion = 0.0
    for cajon in cajones_camion:
        costo_total_camion += cajon['cajones'] * cajon['precio']
    return costo_total_camion


def leer_precios(nombre_archivo):
    '''
    Lee precios de un archivo de datos CSV con dos columnas.
    La primera columna debe contener un nombre y la segunda un precio.
    '''
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

def hacer_informe(encabezados, lista_cajones, dict_precios):
    separadores_str_format = "---------- " * len(encabezados)
    informe = [encabezados, separadores_str_format]
    for cajon in lista_cajones:
        informe.append(
          tuple(cajon.values()) + (float(dict_precios[cajon['nombre']]),)
        )
    return informe

def imprimir_informe(datos):
    encabezados = datos.pop(0)
    encabezados_str_format = "%10s " * len(encabezados)
    print(encabezados_str_format % encabezados)
    
    # Saco el dato de la lista 
    separadores = datos.pop(0)
    print(separadores)
    
    for nombre, cajones, precio, cambio in datos:
        # Convierto a str con un $ adelante antes del print
        precio = "$" + "{:.2f}".format(float(precio))
        print(f'{nombre:>10s} {cajones:>10s} {precio:>10s} {cambio:>10.2f}')

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    cajones_camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    informe = hacer_informe(headers, cajones_camion, precios)
    imprimir_informe(informe)


#%%
files = ['../Data/camion.csv', '../Data/camion2.csv']
for name in files:
    print(f'{name:-^43s}')
    informe_camion(name, '../Data/precios.csv')
    print()

# ------------../Data/camion.csv-------------
#     Nombre    Cajones     Precio     Cambio 
# ---------- ---------- ---------- ---------- 
#       Lima        100     $32.20      40.22
#    Naranja         50     $91.10     106.28
#      Caqui        150    $103.44     105.46
#  Mandarina        200     $51.23      80.89
#    Durazno         95     $40.37      73.48
#  Mandarina         50     $65.10      80.89
#    Naranja        100     $70.44     106.28
# 
# ------------../Data/camion2.csv------------
#     Nombre    Cajones     Precio     Cambio 
# ---------- ---------- ---------- ---------- 
#       Lima         50     $27.10      40.22
#  Frambuesa        250     $43.15      34.35
#  Mandarina         25     $50.15      80.89
#    Durazno        125     $52.10      73.48
