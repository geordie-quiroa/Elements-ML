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

# preparacion de las matrices x, y

n_obs = 100

# arreglos para datos en eje x, y.
xs = np.arange(n_obs)
unos = np.ones(n_obs)

X = np.vstack(
    (unos,
    xs)
).T # Se transpuso la matriz para tener la columna de unos y asi calcular teta_0

#fx = lambda x: (x + bias) + uniform(0,1) * varianza

ys = xs + bias + np.random.rand(n_obs) * varianza

# np applu

#print(X[:10,:])
#print(X.shape)

m, n = X.shape

ys = ys.reshape(m,1) # convertir a vector columna

tetas = np.random.rand(2,1)

alpha = 0.00001

for i in range(10000):
    h = np.matmul(X, tetas) # vector solucion (100,1)
    #print((h - ys).shape) # (100,1) - (100,1)
    tetas -= alpha * ((np.matmul((h - ys).T, X).T) / float(m)) # (1,100) * (100, 2) . T = (2, 1) //reshape(2,1)
    #print(tetas)
print(xs.shape)

y_pred = np.matmul(X,tetas)
print(tetas)

# data = {
#     'y': ys.tolist(),
#     'x': X.tolist()
# }

# import json
# with open('dataset.json', 'w') as f:  # writing JSON object
#     json.dump(data, f)

# with open('dataset.json', 'r') as f:
#     dataset = json.load(f)

# print(np.array(dataset['x']).shape)
plt.plot(xs, y_pred, color = 'r')
plt.scatter(xs,ys)
plt.show()