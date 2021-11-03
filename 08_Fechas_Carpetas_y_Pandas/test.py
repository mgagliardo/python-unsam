import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""
Al comienzo de la materia estuvimos trabajando con el dataset de árboles en parques. 
Ahora estuvimos analizando otro dataset: el de árboles en veredas. Ahora queremos estudiar si hay diferencias entre los ejemplares
de una misma especie según si crecen en un sitio o en otro. Queremos hacer un boxplot del diámetro a la altura del pecho para las Tipa
(su nombre científico es tipuana tipu), que crecen en ambos tipos de ambiente. Para eso tendremos que juntar datos de dos bases de datos diferentes.

Nos vamos en meter en un lío. El GCBA usa en un dataset 'altura_tot', 'diametro' y 'nombre_cie' para las alturas,
diámetros y nombres científicos de los ejemplares, y en el otro dataset usa 'altura_arbol', 'diametro_altura_pecho' y 'nombre_cientifico' para los mismos datos.

Es más, los nombres científicos varían de un dataset al otro. 'Tipuana Tipu'
se transforma en 'Tipuana tipu' y 'Jacarandá mimosifolia' en 'Jacaranda mimosifolia'.
Obviamente son cambios menores pero suficientes para desalentar al usuarie desprevenide.

En este ejercicio te proponemos los siguientes pasos para comparar los diámetros a la altura del pecho
de las tipas en ambos tipos de entornos. Guardá este trabajo en un archivo arbolado_parques_veredas.py.
"""


def leer_archivo(directorio, archivo):
    fname = os.path.join(directorio, archivo)
    df = pd.read_csv(fname)
    return df

def leer(directorio, archivo, columnas, especie):
    df = leer_archivo(directorio, archivo)
    print(df)
    df_lineal = df[columnas]
    df_lineal_seleccion = df_lineal[df_lineal[columnas[-1]].isin([especie])]
    print(df_lineal_seleccion)

if __name__ == "__main__":
    directorio = "../Data"
    archivo_parques = "arbolado-en-espacios-verdes.csv"
    archivo_veredas = "arbolado-publico-lineal-2017-2018.csv"
    especie = 'tipuana tipu'
    columnas_parques = ['altura_tot', 'diametro', 'nombre_cie']
    columnas_veredas = ['altura_arbol', 'diametro_altura_pecho', 'nombre_cientifico']
    leer(directorio, archivo_parques, columnas_parques, especie)
    leer(directorio, archivo_veredas, columnas_veredas, especie)

"""
Para cada dataset armate otro seleccionando solamente las filas correspondientes a las
tipas (llamalos df_tipas_parques y df_tipas_veredas, respectivamente) y las columnas correspondientes al
diametro a la altura del pecho y alturas. Hacelo como copias (usando .copy() como hicimos más arriba) para
poder trabajar en estos nuevos dataframes sin modificar los dataframes grandes originales.
Renombrá las columnas que muestran la altura y el diámetro a la altura del pecho para que se llamen igual
en ambos dataframes, para ello explorá el comando rename.
"""
