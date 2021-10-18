#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# costo_camion.py

#%% ejercicio 9.4
import informe_final

def costo_camion(filename):
    '''
    Computa el precio total (cantidad * precio) de un archivo camion
    '''
    camion = informe_final.leer_camion(filename)
    return camion.precio_total()

def f_principal(argumentos):
    costo = costo_camion(argumentos[1]) 
    print(f'Costo total: {costo}')
#%%    
if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
    






















