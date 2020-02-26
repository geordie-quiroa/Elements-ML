import numpy as np

def logistic(vector_t, vector_x):
    return 1/(1 + np.power(np.e, -1*np.matmul(vector_t.T, vector_x)))

t = np.array([[-3],[1],[1]])
x = np.array([[1],[3],[0]])

print(logistic(t,x))