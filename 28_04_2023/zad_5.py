import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data = pd.read_csv('data/iris.data', delimiter=",", names=["sepallength", "sepalwidth", "PetalL", "PetalW", "Class"])
dataO = {
    "a": data["sepallength"],
    "b": data["sepalwidth"],
    "c": np.random.randint(0, 50, 150),
    "d": abs(data["sepallength"] - data["sepalwidth"])
}
plt.scatter("a", "b", c="c", s="d", data=dataO)
plt.show()