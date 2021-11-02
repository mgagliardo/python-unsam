import matplotlib.pyplot as plt
import os
import pandas as pd
import sys


def shift_serie(df_mareas):
    dh = df_mareas['12-25-2014':].copy()
    delta_t = 0 # tiempo que tarda la marea entre ambos puertos
    delta_h = 0 # diferencia de los ceros de escala entre ambos puertos
    pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()

def graficar(archivo):
    directorio = 'Data'
    fname = os.path.join(directorio,archivo)
    df = pd.read_csv(
        fname,
        index_col=['Time'],
        parse_dates=True
    )
    shift_serie(df)
    plt.show()

if __name__ == '__main__':
    try:
        if len(sys.argv) == 2:
            archivo = sys.argv[1]
        else:
            archivo = 'OBS_SHN_SF-BA.csv'
    except FileNotFoundError:
        print(f'No se encuentra el archivo {sys.argv[1]}')
    graficar(archivo)
