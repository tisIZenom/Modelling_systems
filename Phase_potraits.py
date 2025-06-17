#this is some code to visualise the phase potraits.
# this also helps in visualising hamiltonian flows, a simple function was taken. 

import numpy as np
import matplotlib.pyplot as plt

def hamiltonian_flow(x, y):
    dx = y
    dy = -x
    return dx, dy

X, Y = np.meshgrid(np.linspace(-2, 2, 20), np.linspace(-2, 2, 20))
DX, DY = hamiltonian_flow(X, Y)

plt.quiver(X, Y, DX, DY)
plt.xlabel('q')
plt.ylabel('p')
plt.title('Hamiltonian Vector Field: H = 1/2(p² + q²)')
plt.grid(True)
plt.show()
