import os
import numpy as np
import matplotlib.pyplot as plt

def plotear_temperaturas():
    temperaturas = np.load('../Data/temperaturas.npy')
    print(temperaturas)
    plt.hist(temperaturas, bins=25)
    plt.show()

plotear_temperaturas()
