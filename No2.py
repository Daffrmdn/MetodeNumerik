import numpy as np
import matplotlib.pyplot as plt

# Metode Lagrange:
def lagrange(x, y, t):
    z = 0
    for i in range(len(y)):
        p = 1
        for j in range(len(x)):
            if i != j:
                p *= (t - x[j]) / (x[i] - x[j])
        z += y[i] * p
    return z

x = [1, 2, 3]
y = [2, 1, 2]

for i in range(4, 6):
    t = np.linspace(1, 2, i)
    z = [lagrange(x, y, j) for j in t]
    print(f"Interpolasi polinom derajat {i-1}: {z}") 
    
# Metode Newton:
def newton(x, y, t):
    n = len(x)
    a = y.copy()
    for j in range(1, n):
        for i in range(n-j):
            a[i] = (a[i+1] - a[i]) / (x[i+j] - x[i])
    z = a[0]
    p = 1
    for i in range(1, n):
        p *= t - x[i-1]
        z += a[i] * p
    return z

x = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
y = [1.143, 1.000, 0.828, 0.667, 0.533, 0.428]

for i in range(5, 6):
    t = np.linspace(0.5, 3.0, i)
    z = [newton(x, y, j) for j in t]
    print(f"Interpolasi polinom derajat {i-1}: {z}")

# table
plt.plot(x, y, label='Interpolated function')
plt.scatter(x, y, label='Data points')
plt.legend()
plt.show()
