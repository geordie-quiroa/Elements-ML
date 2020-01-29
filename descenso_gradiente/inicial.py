from random import random, uniform
from random import seed
import matplotlib.pyplot as plt

seed(1)

#teta_1 = ((random() - 0.5) * 2 * desv * random() + x  )

#desv = 0.5

#mu = 2

#teta_original_1 = ((random() - 0.5) * 2 * desv * random() + mu)

#teta_original_0 = 5

# fx = lambda x: teta_original_0 + teta_original_1*x + ((random() - 0.5) * 2 * desv * random() + mu)*1.5 if x % 2 == 0 \
#     else teta_original_0 + teta_original_1*x - ((random() - 0.5) * 2 * desv * random() + mu)*1.5

bias = 25
varianza = 50
fx = lambda x: (x + bias) + uniform(0,1) * varianza

xs = [i for i in range(100)]
ys = [fx(x) for x in xs]

#h_teta = teta_0 + teta_1*x
m = len(xs) 
#j = (y - h_teta)**2

plt.scatter(xs, ys)
plt.show()

h_teta = lambda teta_0, teta_1, x: teta_0 + teta_1 * x

#error_cuadrado = [(h_teta(teta_0, teta_1, i) - fx(i))**2 for i in xs]

#j = lambda teta_0, teta_1: 1 * (2*m)**-1 * sum([(fx(xi) - h_teta(teta_0, teta_1, xi))**2 for xi in xs])
j = lambda teta_0, teta_1: (sum([(fx(xi) - h_teta(teta_0, teta_1, xi))**2 for xi in xs]) / (2*m))

# def jota(teta_0, teta_1):
#    return 1 / 2*m * sum(error_cuadrado)
#print(h_teta(teta_0, teta_1, 1))
#print(error_cuadrado[:5])

def descenso_gradiente(alpha, n_iteraciones, tol):
    n=1
    teta_0 = 1
    teta_1 = 1
    convergido = False
    error_old = j(teta_0, teta_1)    

    while not convergido:
        n+=1
        print(n)
        print(error_old)

        #teta_0 -=  alpha * 1 * (m)**-1 * sum([(fx(xi) - h_teta(teta_0, teta_1, xi)) for xi in xs])
        teta_0 -=  alpha * (sum([(fx(xi) - h_teta(teta_0, teta_1, xi)) for xi in xs]) / m)
        #teta_1 -= alpha * 1 * (m)**-1 * sum([(fx(xi) - h_teta(teta_0, teta_1, xi))*xi for xi in xs])
        teta_1 -= alpha * (sum([(fx(xi) - h_teta(teta_0, teta_1, xi))*xi for xi in xs]) / m)

        error = j(teta_0, teta_1)
        #print(error)
        #if abs(j(teta_0, teta_1) - j(teta_0_old, teta_1_old)) < 0.005:
        if abs(error - error_old) <= tol:
            convergido = True
        
        if n > n_iteraciones:
            print("Maximo de iteraciones alcanzado.")
            convergido = True

        error_old = error
    return (teta_0, teta_1)


print(descenso_gradiente(0.25,100,0.0001))


def coste(x, y, a, b):
    m = len(x)
    error = 0.0
    for i in range(m):
        hipotesis = a+b*x[i]
        error +=  (y[i] - hipotesis) ** 2
    return error / (2*m)

def ddescenso_gradiente(x, y, a, b, alpha, epochs):
    m = len(x)
    hist_coste = []
    for ep in range(epochs):
        b_deriv = 0
        a_deriv = 0
        for i in range(m):
            hipotesis = a+b*x[i]
            a_deriv += hipotesis - y[i]
            b_deriv += (hipotesis - y[i]) * x[i]
            hist_coste.append(coste(x, y, a, b))
        a -= (a_deriv / m) * alpha
        b -= (b_deriv / m) * alpha
        
    return a, b, hist_coste

a=1
b=1
alpha = 0.0001
iters = 100
a,b, hist_coste = ddescenso_gradiente(xs, ys, a, b, alpha, iters)
