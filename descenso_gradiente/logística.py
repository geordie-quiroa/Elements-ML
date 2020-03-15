import numpy as np

def h_teta(vector_x, vector_t): # esta funcion es h_zeta
    #zeta_teta = np.matmul(vector_t.T, vector_x)
    zeta_teta = np.matmul(vector_t.T, vector_x.T)
    #print('Zeta teta: ', zeta_teta) # si zeta >= 0; entonces clase positiva.
    #[5,4,-1] = 5 + 4x1-x2 = 0
    # x2 =  5 + 4x1

    return ((1 + np.power(np.e, -1*zeta_teta))**-1).T # (n,1)

def jota_teta(x, y, hipotesis, m, tetas):
    #h = hipotesis(tetas, x)
    #print('hipotesis: {}\n'.format(-np.log(h)))
    #print('y shape: {}\n'.format(y.shape))
    #print('h shape: {}\n'.format(h.shape))
    return (-1/float(m)) * (np.matmul(y.T, np.log(hipotesis) + np.matmul((1-y.T), np.log(1 - hipotesis))))

def gradiente(
        x,
        y,
        h,
        m,
        tetas,
    ):
    return (((np.matmul((h - y).T, x).T) / float(m)))

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
    
    unos = np.ones(x_set.shape[1]) # [1] ya que X viene en formato de filas, por lo que cada columna es una observacion.
    
    X = transformar_arreglo(x_set, grado)
    
    m, n = X.shape
    #y_set = y_set.reshape(m,1) # convertir a vector columna.
    #print(y_set[-10:])
    tetas = np.random.rand(n,1)

    for i in range(max_iters):
        h = hipotesis(X, tetas) # vector solucion (100,1)
        #print((h - ys).shape) # (100,1) - (100,1)
        tetas -= alpha * gradiente(X, y_set, h, m, tetas) 
    
    #costo = jota_teta(y_set, h, m)
    #y_pred = np.matmul(X,tetas)

    #return y_pred, tetas, costo.sum()
    return tetas # retorno X, ya que incluye la col de uno's, la cual será útil en cross validation.

def cross_validate(x_train, y_train, x_test, y_test, tetas):
    """ Calculo la validación cruzada para los tetas resultantes del train set sobre el test set."""
    
    m = x_train.shape[0]
    h_train = h_teta(x_train, tetas)
    h_test = h_teta(x_test, tetas)
    costo_train = jota_teta(x_train, y_train, h_train, m, tetas)
    costo_test = jota_teta(x_train, y_test, h_test, m, tetas)
    
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

#(x==3)*1

# -log(h(x)), y = 1 cuando se que y es igual a 1. Cuando h es mas cercano a cero, mas alto es el costo. inf - 0
# -log(1-h(x)), y = 0 cuando se que y es igual a 0. Cuando h es mas cercano a cero, el costo se acerca a 0. 0 - inf
# j_teta = y*(-log(h(x))) + (1-y)*(-log(1-h(x)))
# j_teta = 1/m * sum([ y*(-log(h(x))) + (1-y)*(-log(1-h(x))) ])
# X = auto_df.drop('price', axis = 1)
# X_train = X.copy() # en Appendix: handling many levels of categorical variables.

# np.zeros(10, dtype=np.int8)

# x1, x2 = np.meshgrid(
#     np.arange(0,4,0.05),
#     np.arange(0,4,1)
# )

# # x.shape = n featsures, m obs # 
# result = op.minimize(
#     fun=logreg_cost,
#     x0=tetas.flatten(),
#     args=dataset, # dataset es tupla (X, y)
#     method='Newton-CG',
#     jac=logreg_cost_derivative
# )

#
# 
# sigmoid = lambda z: 1.0 / 1-e-z
# Lo que nos sirve es X, success (converge o no), jac (normas de los vectores), nit.

if __name__=='__main__':    
    t = np.array([[-3],[1],[1]]) # tres vars, 2 obs
    #x = np.array([[1,2],[0,1],[3,4]])
    x = np.array([[1,0,3], [2,1,4]])
    y = np.array([[1], [0]])
    print(jota_teta(x, y, h_teta, x.shape[1], t))
    print('y - h: ', y-h_teta(t,x))
    print(gradiente(x, y, h_teta(t,x), x.shape[1], t))
