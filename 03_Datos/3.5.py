# Cuando se le asignan los valores a "registro" donde esta posicionado,
# hace que una nueva iteracion sobreescriba los valores pasados,
# por eso siempre imprime la ultima linea
# La solucion fue cambiar la linea donde se define "registro" y dejarla adentro del for

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
