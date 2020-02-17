from typing import List, Callable, Any # para docstrings y typing
from random import random, uniform, seed

import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

# ------------------ Refactorización del descenso al gradiente a funciones ---------------------------------------------------------------
""" 
El código inicial de descenso al gradiente refactorizado a funciones.
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

# ----------------------------------------- Inicia código sin refactorizar -----------------------------------------------------

def sin_refactorizar():
        
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

    alpha = 0.0001

    for i in range(100000):
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