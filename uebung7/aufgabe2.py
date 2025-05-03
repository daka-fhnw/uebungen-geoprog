import matplotlib.pyplot as plt
import numpy as np
import math

def function(x, y):
    return np.multiply(np.exp(np.negative(np.power(x, 2))), np.sin(y))

x = np.linspace(-np.pi, np.pi, 1000)
y = np.linspace(-np.pi, np.pi, 1000)
X, Y = np.meshgrid(x, y)
Z = function(X, Y)

plt.pcolormesh(X, Y, Z)
plt.show()
