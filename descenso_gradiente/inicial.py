from random import random, uniform
from random import seed
import matplotlib.pyplot as plt

seed(1)
bias = 25
varianza = 50

fx = lambda x: (x + bias) + uniform(0,1) * varianza

xs = [i for i in range(100)]
ys = [fx(x) for x in xs]

m = len(xs) 

plt.scatter(xs, ys)
plt.show()

n_steps = 100
alpha = 0.10
criteria = 0.008
teta_0 = 1
teta_1 = 1

convergido = False
n = 0

while not convergido:
    n+=1
    teta_0_gradient = 0
    teta_1_gradient = 0
    m = float(len(xs))

    for i in range(0, len(xs)):
        teta_0_gradient += (ys[i] - (teta_0 + teta_1 * xs[i]))
        teta_1_gradient += (ys[i] - (teta_0 + teta_1 * xs[i])) * xs[i]
        
    teta_0 -= (alpha * (teta_0_gradient / m))
    teta_1 -= (alpha * (teta_1_gradient / m))

    if max(abs(alpha * teta_0_gradient), abs(alpha * teta_1_gradient)) < criteria:
        convergido = True
    elif n >= n_steps:
        print("No converge, pero se llego a las maximas iteraciones")
        convergido = True
    
print("Los valores que se obtienen son: {}, {} en {} pasos.".format(teta_0, teta_1, n))