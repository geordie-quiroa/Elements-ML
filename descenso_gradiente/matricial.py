from random import random, uniform, seed
import matplotlib.pyplot as plt
import numpy as np


""" Generacion de los datos
- xs = lista de valores en x.
- ys = lista de valores para fx.
"""
seed(1)

bias = 25
varianza = 50

fx = lambda x: (x + bias) + uniform(0,1) * varianza

n_obs = 100

# arreglos para datos en eje x, y.
xs = [i for i in range(n_obs)]
ys = [fx(x) for x in xs]
unos = np.ones(n_obs)

X = np.vstack(
    (unos,
    xs)
).T # Se transpuso la matriz para tener la columna de unos y asi calcular teta_0

print(X[:10,:])
