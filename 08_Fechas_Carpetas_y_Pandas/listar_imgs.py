import os
import sys

def archivos_png(directorio):
    '''Recibe un directorio valido y retorna una lista con el nombre de cada
       archivo dentro del mismo y cada uno de los subdirectorios que pudiese tener.
    
    Pre: Un string con un directorio valido.
    Pos: Una lista con el nombre de cada archivo dentro del directorio y sus subdirectorios.
    '''
    archivos = []
    for root, _, files in os.walk(directorio):
        if files:
            archivos += [os.path.join(root, name).split('/')[-1] for name in files] # Split para obtener solo el nombre del file, sin full path.
    return archivos


def mensaje_ayuda():
    '''Imprime un mensaje de ayuda ante un dato (directorio) mal ingresado
    
    Pos: Mensaje impreso.
    '''
    print("Debe ingresar un directorio valido, por ejemplo: python3 listar_imgs.py ../Directorio")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        directorio = sys.argv[1]
        if os.path.isdir(directorio):
            print(f"Los archivos del directorio {directorio} son {archivos_png(directorio)}")
        else:
            mensaje_ayuda()
    else:
        mensaje_ayuda()
