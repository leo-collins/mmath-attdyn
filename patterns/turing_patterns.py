import time

import matplotlib.pyplot as plt
import numpy as np

start = time.time()

a = 0.00028
b = 0.005
tau = 0.1
k = -0.005

grid_size = 100
h = 2.0 / grid_size

t = 10.0
dt = 0.0001
n = int(t / dt)

U = np.random.rand(grid_size, grid_size)
V = np.random.rand(grid_size, grid_size)


def laplacian(X):
    Xtop = X[0:-2, 1:-1]
    Xleft = X[1:-1, 0:-2]
    Xright = X[1:-1, 2:]
    Xbottom = X[2:, 1:-1]
    Xcentre = X[1:-1, 1:-1]
    return (Xtop + Xleft + Xbottom + Xright - 4 * Xcentre) / (h**2)


def show_mat(X, ax):
    ax.imshow(X, cmap=plt.cm.copper, interpolation="bilinear", extent=[-1, 1, -1, 1])
    ax.set_axis_off()


fig, ax = plt.subplots()

for i in range(n):
    lap_U = laplacian(U)
    lap_V = laplacian(V)

    Ucentre = U[1:-1, 1:-1]
    Vcentre = V[1:-1, 1:-1]

    U[1:-1, 1:-1] = Ucentre + dt * (a * lap_U + Ucentre - Ucentre**3 - Vcentre + k)
    V[1:-1, 1:-1] = Vcentre + dt * (b * lap_V + Ucentre - Vcentre) / tau

    for Z in (U, V):
        Z[0, :] = Z[1, :]
        Z[-1, :] = Z[-2, :]
        Z[:, 0] = Z[:, 1]
        Z[:, -1] = Z[:, -2]

show_mat(U, ax)

end = time.time()
print(end - start)
