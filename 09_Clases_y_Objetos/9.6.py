#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# informe_final.py

#%% ejercicio 9.4
import fileparse
import formato_tabla
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
    return dict(precios)

def hacer_informe(camion, precios):
    lista = []
    for lote in camion:
        cambio = precios[lote.nombre] - lote.precio
        t = (lote.nombre, lote.cajones, lote.precio, cambio)
        lista.append(t)
    return lista

def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in   data_informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)

# TXT
# def informe_camion(archivo_camion, archivo_precios):
#     '''
#     Crea un informe por camion a partir de archivos camion y precio.
#     '''
#     # Leer archivos con datos
#     camion = leer_camion(archivo_camion)
#     precios = dict(leer_precios(archivo_precios))
# 
#     # Obtener los datos para un informe
#     data_informe = hacer_informe(camion, precios)
# 
#     # Imprimir
#     formateador = formato_tabla.FormatoTablaTXT()
#     imprimir_informe(data_informe, formateador)

# CSV
# def informe_camion(archivo_camion, archivo_precios):
#     '''
#     Crea un informe por camion a partir de archivos camion y precio.
#     '''
#     # Leer archivos con datos
#     camion = leer_camion(archivo_camion)
#     precios = dict(leer_precios(archivo_precios))
# 
#     # Obtener los datos para un informe
#     data_informe = hacer_informe(camion, precios)
# 
#     # Imprimir
#     formateador = formato_tabla.FormatoTablaCSV()
#     imprimir_informe(data_informe, formateador)

# HTML
def informe_camion(archivo_camion, archivo_precios):
    '''
    Crea un informe por camion a partir de archivos camion y precio.
    '''
    # Leer archivos con datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    # Obtener los datos para un informe
    data_informe = hacer_informe(camion, precios)

    # Imprimir
    formateador = formato_tabla.FormatoTablaHTML()
    imprimir_informe(data_informe, formateador)


#%%
def f_principal(argumentos):
    informe_camion(argumentos[1], argumentos[2])

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
