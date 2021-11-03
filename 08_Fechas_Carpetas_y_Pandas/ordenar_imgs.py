import os
from shutil import rmtree
from datetime import datetime

glob_carpeta_nueva = '../Data/ordenar/imgs_procesadas'

def borrar_vacias(ruta):
    print("Borrando carpetas vacias..")
    for (path, _, archivos) in os.walk(ruta):
        if len(archivos) == 0:
            rmtree(path)

def get_archivos_png(directorio):
    archivos = []
    for root, _, files in os.walk(directorio):
        if files:
            archivos += [os.path.join(root, fname) for fname in files if '.png' in fname]
    return archivos

def procesar_nombre(fname):
    fecha = fname.split('_')[-1].split('.')[0]
    fecha_mod = datetime(year = int(fecha[0:4]), month = int(fecha[4:6]), day = int(fecha[6:8])).timestamp()
    fname = glob_carpeta_nueva + "/" + fname.replace(fname.split('/')[-1], fname.split('/')[-1].split('_')[0] + '.png').split('/')[-1]
    return fecha_mod, fname

def procesar(fname):
    try:
        fecha_mod, name = procesar_nombre(fname)
        os.rename(fname, name)
        os.utime(name, (fecha_mod, fecha_mod))
    except FileNotFoundError:
        print(f'No se encuentra el directorio {fname}')

def crear_carpeta(carpeta):
    try:
        os.mkdir(carpeta)
        print(f"Directorio {carpeta} creado.")
    except FileExistsError:
        print(f"El subdirectorio {carpeta} ya existe. No hace falta crear.")

def ordenar():
    ruta = '../Data/ordenar'
    archivos = get_archivos_png(ruta)
    if archivos:
        crear_carpeta(glob_carpeta_nueva)
        for archivo in archivos:
            procesar(archivo)
    else:
        print(f"No hay archivos .png en el directorio {ruta}")
    borrar_vacias(ruta)

if __name__ == "__main__":
    ordenar()
