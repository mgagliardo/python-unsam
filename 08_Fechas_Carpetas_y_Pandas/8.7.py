import os
import pandas as pd


def leer_archivo(directorio, archivo):
    fname = os.path.join(directorio, archivo)
    df = pd.read_csv(fname)
    return df

def mas_repetidas(directorio, archivo):
    df = leer_archivo(directorio, archivo)
    mas_repetidas = df['nombre_cientifico'].value_counts()
    print(f"Las 10 especies mas repetidas son:\n{mas_repetidas.head(10)}")

if __name__ == '__main__':
    directorio = '../Data'
    archivo = 'arbolado-publico-lineal-2017-2018.csv'
    mas_repetidas(directorio, archivo)
