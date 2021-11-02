import os
import sys
from datetime import datetime

def archivos_png(directorio):
    archivos = []
    for root, _, files in os.walk(directorio):
        if files:
            archivos += [os.path.join(root, fname) for fname in files if '.png' in fname] # Split para obtener solo el nombre del file, sin full path.
    return archivos

def procesar_nombre(fname):
    fecha = fname.split('_')[-1].split('.')[0]
    fecha_mod = datetime(year = int(fecha[0:4]), month = int(fecha[4:6]), day = int(fecha[6:8]))
    return fname.replace(fecha, fecha_mod)

def procesar(fname):
    for archivo in fname:
        print(archivo)
        fecha = archivo[-12:-4]
        fecha_mod = datetime(year = int(fecha[0:4]), month = int(fecha[4:6]), day = int(fecha[6:8]))
        ts_mod = fecha_mod.timestamp()
        direccion = os.path.join(root, name)
        print(direccion)
        os.utime(direccion, (ts_mod, ts_mod))
        os.rename(direccion, direccion[:-13] + '.png')
    return os.listdir(ruta)

def crear_carpeta(ruta, carpeta):
    try:
        os.mkdir(os.path.join(ruta, carpeta))
        print(f"Mostrando directorio {ruta}")
    except FileExistsError:
        print(f"El subdirectorio {carpeta} ya existe!")

def ordenar(ruta):
    carpeta_nueva = 'imgs_procesadas'
    crear_carpeta(ruta, carpeta_nueva)
    archivos = archivos_png(ruta)
    print(archivos)
    # procesar(archivos)

if __name__ == "__main__":
    try:
        if len(sys.argv) == 2:
            ruta = sys.argv[1]
        else:
            ruta = '../Data/ordenar'
        ordenar(ruta)
    except FileNotFoundError:
        print(f'No se encuentra el directorio {sys.argv}')
