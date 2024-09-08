import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rnd

x = 3 - 6*rnd.rand(100000)
y = 3 - 6*rnd.rand(100000)
z = -3*x + 3j*y
phi = np.angle(z)
P1 = ((phi >= np.pi/3) & (np.abs(z) <= 6))
P2 = ((-phi >= np.pi/3) & (np.abs(z) <= 6))

plt.plot(x[P1], y[P1], color='b')
plt.plot(x[P2], y[P2], color='b')

plt.axis([-2, 2, -2, 2])
plt.axhline(y=0, color='black')
plt.axvline(x=0, color='black')

plt.grid()
plt.xlabel('Действительная часть')
plt.ylabel('Мнимая часть')
plt.show()
