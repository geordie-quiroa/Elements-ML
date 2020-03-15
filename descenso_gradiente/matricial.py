import numpy as np

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
        m: int,
        tetas: List[List[float]],
        _lambda: float,
    ) -> int:
    """Calcula el costo de error para la hipotesis respecto a los valores teóricos (y).
    
    m: cantidad de observaciones.

    Retorna un entero.
    """
    e = (y - hipotesis) # (n,1)
    e2 = np.matmul(e.T, e) # (1,1) suma de los errores cuadrados.
    #tts = np.matmul(tetas.T, tetas)
    
    #print('Errores ', 1/(2 * m) * e2)
    #print('Regularizacion ', (_lambda / (2 * m)) * tts)
    #res = 1/(2 * m) * (e2) + _lambda / (2 * m) * tts
    #print('Error ',e2)
    #print('RES ',e2)
    return (1/(2 * m) * (e2) + _lambda / (2 * m) * np.matmul(tetas.T, tetas)) # np.sum(np.power(tetas, 2))

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
        m: int,
        tetas: List[List[float]],
        _lambda: float,
    ) -> int:
    """Calcula el costo de error para la hipotesis respecto a los valores teóricos (y).
    
    m: cantidad de observaciones.

    Retorna un entero.
    """
    e = (y - hipotesis) # (n,1)
    e2 = np.matmul(e.T, e) # (1,1) suma de los errores cuadrados.
    #tts = np.matmul(tetas.T, tetas)
    
    #print('Errores ', 1/(2 * m) * e2)
    #print('Regularizacion ', (_lambda / (2 * m)) * tts)
    #res = 1/(2 * m) * (e2) + _lambda / (2 * m) * tts
    #print('Error ',e2)
    #print('RES ',e2)
    return (1/(2 * m) * (e2) + (_lambda / (2 * m)) * np.matmul(tetas.T, tetas)) # np.sum(np.power(tetas, 2))

def gradiente(
        x: List[List[float]],
        y: List[float],
        h: List[float],
        m: float,
        tetas: List[List[float]],
        _lambda: float,
    ) -> List[List[float]]:
    """Calcula el gradiente para el conjunto de valores X, Y, respecto a la hipotesis dada.
    
    Retorna una matriz (m,1) con los coeficientes.
    """
    
    return (((np.matmul((h - y).T, x).T) / float(m)) + ((_lambda / m) * np.sum(tetas))) # (1,100) * (100, 2) . T = (2, 1) //reshape(2,1)

def descenso_gradiente(
        x_set: List[List[float]],
        y_set: List[float],
        #tetas_iniciales: List[float],
        hipotesis: Callable[[Any], Any],#[[List[float], List[float]], List[float]], # Callable[[parametros], resultado]
        gradiente: Callable[[Any], Any],#[[List[float], List[float], List[float], float], List[float]], # Callable[[parametros], resultado]
        max_iters: int = 10000,
        alpha: float = 0.0001,
        _lambda: float = 0.0,
        grado: int = 1
    ) -> List[float]:
    
    """Esta función ejecuta el descenso en gradiente para encontrar las tetas que minimizan el costo."""
    
    X = transformar_arreglo(x_set, grado)
    
    m, n = X.shape
    #y_set = y_set.reshape(m,1) # convertir a vector columna.
    #print(y_set[-10:])
    tetas = np.random.rand(n,1)

    for i in range(max_iters):
        h = hipotesis(X, tetas) # vector solucion (100,1)
        #print((h - ys).shape) # (100,1) - (100,1)
        tetas -= alpha * gradiente(X, y_set, h, m, tetas, _lambda) 
    
    #costo = jota_teta(y_set, h, m)
    #y_pred = np.matmul(X,tetas)

    #return y_pred, tetas, costo.sum()
    return tetas#, X # retorno X, ya que incluye la col de uno's, la cual será útil en cross validation.

def cross_validate(x_train, y_train, x_test, y_test, tetas, _lambda = 0.0):
    """ Calculo la validación cruzada para los tetas resultantes del train set sobre el test set."""
    
    m = x_train.shape[0]
    h_train = h_teta(x_train, tetas)
    h_test = h_teta(x_test, tetas)
    costo_train = jota_teta(y_train, h_train, m, tetas, _lambda)
    costo_test = jota_teta(y_test, h_test, m, tetas, _lambda)
    
    return [(costo_train, costo_test), (h_train, h_test)]

def transformar_arreglo(x_set, grado):
    
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
        
    return X