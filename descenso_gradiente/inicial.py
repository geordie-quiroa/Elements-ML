xs = []
ys = []

h_teta = beta_0 + beta_1*x

j = (y - h_teta)**2

def descenso_gradiente(j, alpha):
    beta_0 = 0
    beta_1 = 1
    return (beta_0, beta_1)