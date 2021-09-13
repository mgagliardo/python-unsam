import fileparse


def leer_camion(nombre_archivo):
    return fileparse.parse_csv(
        nombre_archivo,
        select = ['nombre', 'cajones', 'precio'],
        types = [str, int, float]
    )

def leer_precios(nombre_archivo):
    return dict(fileparse.parse_csv(
            nombre_archivo,
            types = [str, float],
            has_headers = False
    ))

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
    
    separadores = datos.pop(0)
    print(separadores)
    
    for nombre, cajones, precio, cambio in datos:
        precio = "$" + "{:.2f}".format(float(precio))
        cambio = "$" + "{:.2f}".format(float(cambio))
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10s}')

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    cajones_camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    informe = hacer_informe(headers, cajones_camion, precios)
    imprimir_informe(informe)


#%%
# files = ['../Data/camion.csv', '../Data/camion2.csv']
# for name in files:
#     print(f'{name:-^43s}')
#     informe_camion(name, '../Data/precios.csv')
#     print()
#%%

# Output:
# ------------../Data/camion.csv-------------
#     Nombre    Cajones     Precio     Cambio 
# ---------- ---------- ---------- ---------- 
#       Lima        100     $32.20     $40.22
#    Naranja         50     $91.10    $106.28
#      Caqui        150    $103.44    $105.46
#  Mandarina        200     $51.23     $80.89
#    Durazno         95     $40.37     $73.48
#  Mandarina         50     $65.10     $80.89
#    Naranja        100     $70.44    $106.28
# 
# ------------../Data/camion2.csv------------
#     Nombre    Cajones     Precio     Cambio 
# ---------- ---------- ---------- ---------- 
#       Lima         50     $27.10     $40.22
#  Frambuesa        250     $43.15     $34.35
#  Mandarina         25     $50.15     $80.89
#    Durazno        125     $52.10     $73.48
