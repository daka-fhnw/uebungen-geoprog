import matplotlib.pyplot as plt
import numpy as np

def random_plus_minus_100():
    return np.random.randint(-100, 100)

for idx in range(1000):
    x = random_plus_minus_100()
    y = random_plus_minus_100()
    plt.plot(x, y, 'o')

plt.xlabel("x-Achse")
plt.ylabel("y-Achse")
plt.axis([-100, 100, -100, 100])
plt.show()
