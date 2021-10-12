#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# informe_final.py

#%% ejercicio 9.4
import fileparse
import lote

def leer_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    with open(nombre_archivo) as f:
        camion_dicts = fileparse.parse_csv(f, select = ['nombre', 'cajones', 'precio'], types = [str, int, float], has_headers = True)
    camion = [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
    return camion

def leer_precios(nombre_archivo):
    with open(nombre_archivo) as f:
        precios = fileparse.parse_csv(f, types = [str, float], has_headers = False)
    return precios

def hacer_informe(camion, precios):
    lista = []
    for lote in camion:
        cambio = precios[lote.nombre] - lote.precio
        t = (lote.nombre, lote.cajones, lote.precio, cambio)
        lista.append(t)
    return lista

def imprimir_informe(informe):
    print('    Nombre    Cajones     Precio     Cambio')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        precio = f'${precio}'
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    lista_precios = leer_precios(nombre_archivo_precios)
    precios = dict(lista_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)
#%%
def f_principal(argumentos):
    informe_camion(argumentos[1], argumentos[2])

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
    






