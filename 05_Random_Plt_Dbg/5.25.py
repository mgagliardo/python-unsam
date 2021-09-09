import csv
import os
import matplotlib.pyplot as plt

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


nombre_archivo = os.getcwd() + '/../Data/arbolado-en-espacios-verdes.csv'
arboleda = leer_arboles(nombre_archivo)
nombre_arbol = 'Jacarandá'
# Tomo solo el primer dato de la tupla, altura.
altos = [tupla[0] for tupla in lista_alturas(arboleda, nombre_arbol)]

# Grafico
plt.hist(altos,bins=50)
plt.show()
