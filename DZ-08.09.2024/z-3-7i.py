import numpy as np
import numpy.random as rng
import matplotlib.pyplot as plt


x = 7 - 10 * rng.rand(100000)
y = 10 * rng.rand(100000)
z = x + 1j * y
L = (np.abs(z - (3 + 7j)) <= 1)
plt.plot(x[L], y[L], '.')
plt.axis('equal')
plt.grid(True)
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.title('$| z - (3 + 7i) | \leq 1$')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')

plt.show()
