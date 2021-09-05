import csv
from pprint import pprint

def leer_arboles(nombre_archivo):
    arboleda = []
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        for fila in filas:
            arbol = dict(zip(encabezados, fila))
            arboleda.append(arbol)
    return arboleda

def lista_alturas(arboleda, nombre_arbol):
    # NDA: El ejercicio (cito) dice:
    # "Tenga pares (tuplas de longitud 2) conteniendo no solo el alto sino también el diámetro de cada Jacarandá en la lista."
    # Por tanto entiendo que el par de la tupla es (altura, diametro) y por tanto ese es el orden en que se devuelve
    return [ 
        # Tupla (altura, diametro)
        (float(arbol['altura_tot']), float(arbol['diametro']))
        for arbol in arboleda
        if arbol['nombre_com'] == nombre_arbol 
    ]

def medidas_de_especies(especies, arboleda):
    listas_altura = [lista_alturas(arboleda, nombre_arbol) for nombre_arbol in especies]
    return dict(zip(especies, listas_altura))

nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
arboleda = leer_arboles(nombre_archivo)

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

# print(medidas_de_especies(especies, arboleda))
# No pongo el output ya que es demasiado largo
