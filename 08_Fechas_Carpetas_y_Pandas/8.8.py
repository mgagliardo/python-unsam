import os
import pandas as pd
import matplotlib.pyplot as plt


def leer_archivo(directorio, archivo):
    fname = os.path.join(directorio, archivo)
    df = pd.read_csv(fname)
    return df

def graficar_diametro_altura_pecho(directorio, archivo, columnas, especies):
    df = leer_archivo(directorio, archivo)
    df_lineal = df[columnas]
    df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies)]
    df_lineal_seleccion.boxplot('altura_arbol', by = 'nombre_cientifico')
    plt.show()

if __name__ == '__main__':
    directorio = '../Data'
    archivo = 'arbolado-publico-lineal-2017-2018.csv'
    cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
    especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
    graficar_diametro_altura_pecho(directorio, archivo, cols_sel, especies_seleccionadas)
