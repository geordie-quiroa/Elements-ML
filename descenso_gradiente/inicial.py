from typing import List, Callable, Any # para docstrings y typing
from random import random, uniform, seed

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

# ------------------ Refactorización del descenso al gradiente a funciones ---------------------------------------------------------------
""" 
El código anterior será refactorizado a funciones.
"""

def h_teta(
        x: List[List[float]],
        coefs: List[List[float]]
    ) -> List[float]:
    """Calcula matricialmente las hipótesis para las tetas ingresadas.
    
    Retorna una lista con la hipótesis calculada para cada valor en x.
    """

    return (np.matmul(x, coefs)) # (174, 2) * (2, 1) = (174, 1)

def jota_teta(
        y: List[float],
        hipotesis: List[float],
        m: int
    ) -> int:
    """Calcula el costo de error para la hipotesis respecto a los valores teóricos (y).
    
    m: cantidad de observaciones.

    Retorna un entero.
    """

    return (1/(2 * m) * (y - hipotesis)**2).sum()

def gradiente(
        x: List[List[float]],
        y: List[float],
        h: List[float],
        m: float
    ) -> List[List[float]]:
    """Calcula el gradiente para el conjunto de valores X, Y, respecto a la hipótesis dada.
    
    Retorna una matriz (m,1) con los coeficientes.
    """
    
    return ((np.matmul((h - y).T, x).T) / float(m)) # (1,100) * (100, 2) . T = (2, 1) //reshape(2,1)

def descenso_gradiente(
        x_set: List[List[float]],
        y_set: List[float],
        #tetas_iniciales: List[float],
        hipotesis: Callable[[Any], Any],#[[List[float], List[float]], List[float]], # Callable[[parametros], resultado]
        gradiente: Callable[[Any], Any],#[[List[float], List[float], List[float], float], List[float]], # Callable[[parametros], resultado]
        max_iters: int = 10000,
        alpha: float = 0.0001,
        grado: int = 1
    ) -> List[float]:
    
    """Esta función ejecuta el descenso en gradiente para encontrar las tetas que minimizan el costo."""
    
    unos = np.ones(x_set.shape[1]) # [1] ya que X viene en formato de filas, por lo que cada columna es una observacion.
    
    if grado == 1:
        X = np.vstack(
            (
            unos,
            x_set,
            #-x_set**2
            )
        ).T # Se transpuso la matriz para tener la columna de unos y asi calcular teta_0
    elif grado == 2:
        X = np.vstack(
            (
            unos,
            x_set,
            x_set**2
            )
        ).T
    elif grado == -2:
        X = np.vstack(
            (
            unos,
            x_set,
            -x_set**2
            )
        ).T
    
    m, n = X.shape
    #y_set = y_set.reshape(m,1) # convertir a vector columna.
    #print(y_set[-10:])
    tetas = np.random.rand(n,1)

    for i in range(max_iters):
        h = hipotesis(X, tetas) # vector solucion (100,1)
        #print((h - ys).shape) # (100,1) - (100,1)
        tetas -= alpha * gradiente(X, y_set, h, m) 
    
    #costo = jota_teta(y_set, h, m)
    #y_pred = np.matmul(X,tetas)

    #return y_pred, tetas, costo.sum()
    return tetas, X # retorno X, ya que incluye la col de uno's, la cual será útil en cross validation.

def cross_validate(x_train, y_train, x_test, y_test, tetas):
    """ Calculo la validación cruzada para los tetas resultantes del train set sobre el test set."""
    
    m = x_train.shape[0]
    h_train = h_teta(x_train, tetas)
    h_test = h_teta(x_test, tetas)
    costo_train = jota_teta(y_train, h_train, m)
    costo_test = jota_teta(y_test, h_test, m)
    
    return [(costo_train, costo_test), (h_train, h_test)]

# ----------------------------------------- Finaliza código refactorizado. ----------------------------------------------

def no_refactorizado_descenso_gradiente():
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