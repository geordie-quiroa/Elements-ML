from random import random
from random import seed
import matplotlib.pyplot as plt

seed(1)

#teta_1 = ((random() - 0.5) * 2 * desv * random() + x  )

desv = 0.5

mu = 2

teta_1 = ((random() - 0.5) * 2 * desv * random() + mu)

teta_0 = 5

fx = lambda x: teta_0 + teta_1*x + ((random() - 0.5) * 2 * desv * random() + mu)*1.5 if x % 2 == 0 \
    else teta_0 + teta_1*x - ((random() - 0.5) * 2 * desv * random() + mu)*1.5

xs = [i for i in range(100)]
ys = [fx(x) for x in xs]

#h_teta = teta_0 + teta_1*x
m = len(xs) 
#j = (y - h_teta)**2

#plt.scatter(xs, ys)
#plt.show()

h_teta = lambda teta_0, teta_1, x: teta_0 + teta_1 * x

#error_cuadrado = [(h_teta(teta_0, teta_1, i) - fx(i))**2 for i in xs]

j = lambda teta_0, teta_1: 1 * (2*m)**-1 * sum([(h_teta(teta_0, teta_1, i) - fx(i))**2 for i in xs])

# def jota(teta_0, teta_1):
#    return 1 / 2*m * sum(error_cuadrado)

print(teta_0, teta_1)
print(j(teta_0, teta_1))
print(0, 1)
print(j(0, 1))
teta_0 = 0
teta_1 = 1

teta_0 -= 1 * (m)**-1 * sum([(h_teta(teta_0, teta_1, xi) - fx(xi)) for xi in xs])
teta_1 -= 1 * (m)**-1 * sum([(h_teta(teta_0, teta_1, xi) - fx(xi))*xi for xi in xs])

print(teta_0, teta_1)
print(j(teta_0, teta_1))

teta_0 -= 1 * (m)**-1 * sum([(h_teta(teta_0, teta_1, xi) - fx(xi)) for xi in xs])
teta_1 -= 1 * (m)**-1 * sum([(h_teta(teta_0, teta_1, xi) - fx(xi))*xi for xi in xs])

print(teta_0, teta_1)
print(j(teta_0, teta_1))

teta_0 -= 1 * (m)**-1 * sum([(h_teta(teta_0, teta_1, xi) - fx(xi)) for xi in xs])
teta_1 -= 1 * (m)**-1 * sum([(h_teta(teta_0, teta_1, xi) - fx(xi))*xi for xi in xs])

print(teta_0, teta_1)
print(j(teta_0, teta_1))

teta_0 -= 1 * (m)**-1 * sum([(h_teta(teta_0, teta_1, xi) - fx(xi)) for xi in xs])
teta_1 -= 1 * (m)**-1 * sum([(h_teta(teta_0, teta_1, xi) - fx(xi))*xi for xi in xs])

print(teta_0, teta_1)
print(j(teta_0, teta_1))


#print(h_teta(teta_0, teta_1, 1))
#print(error_cuadrado[:5])

def descenso_gradiente(j, alpha):
    teta_0 = 0
    teta_1 = 1
    convergido = False
    while not convergido:
        teta_0 = teta_0 - alpha * gradiente_teta_0()
        teta_1 = teta_1 -  alpha * gradiente_teta_1()
        convergido = True
    return (teta_0, teta_1)

print(ys[0:5])
#descenso_gradiente(j,1.5)