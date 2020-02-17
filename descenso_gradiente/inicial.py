from random import random, uniform, seed

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

""" Generacion de los datos
- xs = lista de valores en x.
- ys = lista de valores para fx.
"""
seed(1)

bias = 25
varianza = 50

# funcion de ys con media 25 y varianza 50
fx = lambda x: (x + bias) + uniform(0,1) * varianza

# arreglos para datos en eje x, y.
xs = [i for i in range(100)]
ys = [fx(x) for x in xs]

# visualizacion de los datos.
plt.scatter(xs, ys)
plt.show()


""" Descenso en gradiente

alpha: learning rate.
criteria: treshold del valor de error.

Retorna los valores finales para los tetas."""

# total de iteraciones maximo.
n_steps = 100

# learning rate.
alpha = 0.10

# criterio para detener el while.
criteria = 0.008

# tetas iniciales para el descenso en gradiente.
teta_0 = 1
teta_1 = 1

# Bandera de convergencia para ciclo while.
convergido = False

# Numero de iteraciones inicial
n = 0

# Total de series en los datos
m = float(len(xs))

# Funcion de error.
def j(t_0, t_1, xs, ys):
    error = 0.0
    for i in range(len(xs)):
        error+= (ys[i] - (t_0 + t_1*xs[i]))

    return (error / (2*m))

while not convergido:

    teta_0_gradient = 0
    teta_1_gradient = 0

    for i in range(0, len(xs)): # sumatoria de la derivada parcial para cada teta.
        h_teta = teta_0 + teta_1 * xs[i]
        teta_0_gradient += (ys[i] - h_teta)
        teta_1_gradient += (ys[i] - h_teta) * xs[i]

    # reajuste de los valores de teta, variando a la tasa del learning rate y resultado de la derivada parcial.
    teta_0 -= (alpha * (teta_0_gradient / m))
    teta_1 -= (alpha * (teta_1_gradient / m))

    if max(abs(alpha * teta_0_gradient), abs(alpha * teta_1_gradient)) < criteria: # si la magnitud es menor al criterio, converge.
        convergido = True
    elif n >= n_steps:
        print("No converge, pero se llego a las maximas iteraciones")
        convergido = True

    n+=1

print("Los valores que se obtienen son: {}, {} en {} pasos.".format(teta_0, teta_1, n))