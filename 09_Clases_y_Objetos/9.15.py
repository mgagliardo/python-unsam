import numpy as np
import matplotlib.pyplot as plt

banda = np.zeros([])
for i in range(1, 8):
    banda = np.add(banda, np.load('clip/LC08_L1TP_225084_20180213_20180222_01_T1_sr_band' + str(i) + '_clip.npy'))

plt.imshow(banda, cmap='winter', vmin=0, vmax=20)
# plt.hist(banda.flatten(),bins = 100)
plt.show()
