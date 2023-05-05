import matplotlib.pyplot as plt
import numpy as np

# Wygeneruj  wykres  punktowy  dla 5 różnych  losowych  serii  z  użyciem  różnych  znaczników i kolorów:https://matplotlib.org/api/markers_api.html


def randrange(n, vmin, vmax):
    return(vmax - vmin)*np.random.rand(n)+vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
n = 100

for c, m, zlow, zhigh in [('r', 'o', -50, 20), ('g', '>', 40, 0), ('b', '.', -25, 25), ('y', '4', 0, 25), ('k', 'D', 10, 40)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()