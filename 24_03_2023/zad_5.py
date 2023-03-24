import numpy as np
import math

array = np.array([[0, .3, 0.5], [round(round(math.pi, 2) * 1/3, 2), round(math.pi, 2), round(round(math.pi, 2) * 1/6, 2)]])

a = np.sin(array)

print(a)
