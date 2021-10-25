import io
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model


def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b

if __name__ == '__main__':
    enlace = 'https://raw.githubusercontent.com/python-unsam/Programacion_en_Python_UNSAM/master/Notas/11_Recursion/longitudes_y_pesos.csv'
    r = requests.get(enlace).content
    data_lyp = pd.read_csv(io.StringIO(r.decode('utf-8')))
    
    x = data_lyp['longitud']
    y = data_lyp['peso']

    datosxy = pd.DataFrame({'x': x, 'y': y}) # Paso los datos a un dataframe
    ajus = linear_model.LinearRegression() # Llamo al modelo de regresión lineal
    ajus.fit(datosxy[['x']], datosxy['y']) # Ajusto el modelo
    grilla_x = np.linspace(start = 0, stop = 70, num = 1000)
    grilla_y = ajus.predict(grilla_x.reshape(-1,1))
    datosxy.plot.scatter('x', 'y')
    plt.title('Ajuste lineal usando sklearn')
    plt.plot(grilla_x, grilla_y, c = 'green')
    plt.show()

    N = 50
    minx = 0
    maxx = 500
    a, b = ajuste_lineal_simple(x, y)
    grilla_x = np.linspace(start = minx, stop = maxx, num = 1000)
    grilla_y = grilla_x*a + b
    g = plt.scatter(x = x, y = y)
    plt.title('y ajuste lineal')
    plt.plot(grilla_x, grilla_y, c = 'green')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
