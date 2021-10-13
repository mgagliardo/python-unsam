import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    '''Funcion base para generar un random array de pasos en base al largo de una caminata.

    Pre: Largo de la caminata.
    Pos: Numpy array de una caminata.
    '''
    return np.random.randint(-1, 2, largo).cumsum()

def obtener_caminatas(largo_trayectorias, cant_trayectorias):
    '''Devuelve una lista de cant_trayectorias de caminatas en base al largo_trayectorias de las mismas.
    
    Pre: Largo de las trayectorias y cantidad de las trayectorias.
    Pos: Una lista de caminatas.
    '''
    return [randomwalk(largo_trayectorias) for _ in range(cant_trayectorias)]

def lista_de_maximos(caminatas):
    '''Obtiene la lista de maximos absolutos por caminata en base a todas las caminatas.
    
    Pre: Una lista de caminatas.
    Pos: Una lista con los maximos absolutos de todas las caminatas coincidentes con el indice de cada una.
    '''
    return [ abs(max(caminata.min(), caminata.max(), key=abs)) for caminata in caminatas ]

def cuan_alejada(caminatas, callback):
    '''Obtiene y devuelve la lista seleccionada en base a un callback function (ej. min o max)
       a partir de una lista de maximos absolutos obtenida usando lista_de_maximos
    
    Pre: Una lista de caminatas.
    Pos: La caminata seleccionada en base al callback, por ejemplo la mas larga o la mas corta.
    '''
    lista_maximos = lista_de_maximos(caminatas)
    # Obtengo el indice del callback, que coindicide con el de la lista dado que matchean 1:1
    ind = lista_maximos.index(callback(lista_maximos))
    return caminatas[ind]

def preparar_pubplot(tupla_pos, limite_axis, titulo):
    '''Prepara la figura (pubplot) con titulo, limites, posicion
       borrado de labels del eje x y tamaño/tipo de linea.

    Pre: 
        * Tupla de x, y, z posiciones para el subplot
        * Limite del axis y
        * Titulo grafico
    Pos: None, dado que solo prepara (crea) la figura
    '''
    x, y, z = tupla_pos
    plt.subplot(x, y, z)
    plt.ylim(-limite_axis, limite_axis)
    plt.title(titulo)
    plt.xticks([])
    plt.plot(linewidth=1.0, linestyle="-")


def graficar(largo_trayectorias, cant_trayectorias):
    '''Grafica una cantidad de "caminatas" dada de trayectorias cant_trayectorias.
       Con un largo determinado por largo_trayectorias.

    Pre: Dos numeros naturales largo_trayectorias y can_trayectorias.
    Pos: Tres graficas, con todas las caminatas, la que mas se alejo y la que menos se alejo.
    '''
    limite_axis = 500.0
    colores = [ # 12 colores cherrypickeados :)
        "yellow",
        "yellowgreen",
        "dodgerblue",
        "lightseagreen",
        "royalblue",
        "mediumpurple",
        "orchyd",
        "palevioletred",
        "crimson",
        "lightcoral",
        "indianred",
        "chocolate"
    ]

    plt.figure()
    plt.xlabel("Tiempo")
    plt.ylabel("Distancia al origen")
    preparar_pubplot((2, 1, 1), limite_axis, "12 Caminatas al azar")

    caminatas = obtener_caminatas(largo_trayectorias, cant_trayectorias)
    for ind, caminata in enumerate(caminatas): # Recorro la lista de caminatas obtenidas y las grafico 1x1
        plt.plot(caminata)
        plt.plot(color=colores[ind], linewidth=1.0, linestyle="-")

    preparar_pubplot((2, 2, 3), limite_axis, "La caminata que mas se aleja")
    plt.plot(cuan_alejada(caminatas, max))

    preparar_pubplot((2, 2, 4), limite_axis, "La caminata que menos se aleja")
    plt.plot(cuan_alejada(caminatas, min))

    plt.show()

if __name__ == '__main__':
    cant_trayectorias = 12
    largo_trayectorias = 100000
    graficar(largo_trayectorias, cant_trayectorias)
