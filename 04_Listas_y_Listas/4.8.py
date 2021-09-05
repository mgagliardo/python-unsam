import csv

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

def leer_precios(nombre_archivo):
    precios = {}
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if row:
                precios[row[0]] = float(row[1])
    return precios

camion = leer_camion('../Data/camion.csv')

costo = sum([s['cajones'] * s['precio'] for s in camion])
print(costo)

precios = leer_precios('../Data/precios.csv')
valor = sum([s['cajones'] * precios[s['nombre']] for s in camion])
print(valor)

print(sum([s['cajones'] * s['precio'] for s in camion]))
