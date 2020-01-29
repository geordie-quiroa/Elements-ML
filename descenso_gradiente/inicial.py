from random import random
from random import seed
import matplotlib.pyplot as plt

seed(1)

#beta_1 = ((random() - 0.5) * 2 * desv * random() + x  )

desv = 0.5

mu = 2

beta_1 = ((random() - 0.5) * 2 * desv * random() + mu)

beta_0 = 5

fx = lambda x: beta_0 + beta_1*x + ((random() - 0.5) * 2 * desv * random() + mu  ) if x % 2 == 0 \
    else beta_0 + beta_1*x - ((random() - 0.5) * 2 * desv * random() + mu  )

xs = [i for i in range(100)]
ys = [fx(x) for x in xs]

#h_teta = beta_0 + beta_1*x
m = len(xs) 
#j = (y - h_teta)**2

plt.scatter(xs, ys)
plt.show()

def descenso_gradiente(j, alpha):
    beta_0 = 0
    beta_1 = 1
    return (beta_0, beta_1)

print(ys[0:5])