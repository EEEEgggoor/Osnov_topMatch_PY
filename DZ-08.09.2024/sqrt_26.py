import matplotlib.pyplot as plt
import numpy as np

z = 1 + 1j

r = np.abs(z)
phi = np.angle(z)

n = 26
k = np.arange(1, 27)

zroot = r ** (1 / n) * (np.cos((phi + 2.0 * np.pi * k) / n) +
                        1j * np.sin((phi + 2.0 * np.pi * k) / n))
print(zroot)
plt.title(f'$\sqrt[{n}]{{1+j}}$')
plt.plot(np.real(zroot), np.imag(zroot), '*r')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.axis('equal')
t = np.linspace(0, 2 * np.pi, 100)
plt.plot(r ** (1 / n) * np.cos(t), r ** (1 / n) * np.sin(t), ':')

plt.grid()

plt.show()
