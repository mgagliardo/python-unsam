import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

N = 100000
trayectorias = 12
colores = ["green", "navy", "red", "black", "brown", "gold", "orange", "blueviolet", "crimson", "slategrey", "dodgerblue", "pink"]


plt.xlabel("tiempo")
plt.ylabel("distancia al origen")

for i in range(trayectorias):
    plt.plot(randomwalk(N))
    plt.plot(color=colores[i], linewidth=1.0, linestyle="-")

plt.show()
