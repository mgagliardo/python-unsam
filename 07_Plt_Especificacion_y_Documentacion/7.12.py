import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint(-1, 2, largo)    
    return pasos.cumsum()

def obtener_caminatas(largo_trayectorias, cant_trayectorias):
    return [randomwalk(largo_trayectorias) for _ in range(cant_trayectorias)]

def lista_de_maximos(lista):
    lista_maximos = [ abs(max(walk.min(), walk.max(), key=abs)) for walk in lista ]
    return lista_maximos

def cuan_alejada(lista, callback):
    lista_maximos = lista_de_maximos(lista)
    ind = lista_maximos.index(callback(lista_maximos))
    return lista[ind]

def graficar(largo_trayectorias, cant_trayectorias):
    '''Grafica una cantidad de "caminatas" dada de trayectorias cant_trayectorias
       Con un largo determinado por largo_trayectorias

    Pre: Dos numeros naturales largo_trayectorias y can_trayectorias
    Pos: Tres graficas, con todas las caminatas, la que mas se alejo y la que menos se alejo
    '''
    limite_axis = 500.0
    colores = ["yellow", "yellowgreen", "dodgerblue", "lightseagreen", "royalblue", "mediumpurple", "orchyd", "palevioletred", "crimson", "lightcoral", "indianred", "chocolate"]

    plt.figure()
    plt.xlabel("Tiempo")
    plt.ylabel("Distancia al origen")

    plt.subplot(2, 1, 1)
    plt.ylim(-limite_axis, limite_axis)
    plt.title("12 Caminatas al azar")

    caminatas = obtener_caminatas(largo_trayectorias, cant_trayectorias)
    for ind, caminata in enumerate(caminatas): # Recorro la lista de caminatas obtenidas y las grafico 1x1
        plt.plot(caminata)
        plt.plot(color=colores[ind], linewidth=1.0, linestyle="-")
        plt.xticks([])

    plt.subplot(2, 2, 3)
    plt.ylim(-limite_axis, limite_axis)
    plt.title("La caminata que mas se aleja")
    plt.xticks([])
    plt.plot(color="dimgrey", linewidth=1.0, linestyle="-")
    plt.plot(cuan_alejada(caminatas, max))


    plt.title("La caminata que menos se aleja")
    plt.subplot(2, 2, 4)
    plt.ylim(-limite_axis, limite_axis)
    plt.xticks([])
    plt.plot(color="navy", linewidth=1.0, linestyle="-")
    plt.plot(cuan_alejada(caminatas, min))

    plt.show()

if __name__ == '__main__':
    cant_trayectorias = 12
    largo_trayectorias = 100000
    graficar(largo_trayectorias, cant_trayectorias)
