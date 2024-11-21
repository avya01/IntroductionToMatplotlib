import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 5, 9, 0])
y = np.array([4, 6, 0, 8])

plt.plot(x, y, marker = "o", ms = 10, mec = "green", linestyle = "dashed", mfc = "green", color = "yellow", linewidth = "5")
plt.show()