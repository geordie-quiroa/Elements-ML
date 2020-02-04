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
xs = np.array([i for i in range(n_obs)])
unos = np.ones(n_obs)

X = np.vstack(
    (unos,
    xs)
).T # Se transpuso la matriz para tener la columna de unos y asi calcular teta_0

print(X[:10,:])
print(X.shape)

m, n = X.shape

ys = np.array([fx(x) for x in xs])
ys = ys.reshape(m,1) # convertir a vector columna

tetas = np.random.rand(2,1)

h = np.matmul(X, tetas) # vector solucion (100,1)
print((h - ys).shape) # (100,1) - (100,1)
alpha = 0.01

tetas = tetas - alpha * (np.matmul((h - ys).T, X).T / m) # (1,100) * (100, 2) . T = (2, 1) 
print(tetas)
