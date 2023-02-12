import numpy as np

# Metode Eliminasi Gauss-Jordan:

def gauss_jordan(A, b):
    n = len(A)
    for i in range(n):
        for j in range(i+1, n):
            ratio = A[j][i] / A[i][i]
            for k in range(n):
                A[j][k] = A[j][k] - ratio * A[i][k]
            b[j] = b[j] - ratio * b[i]
    for i in range(n-1, -1, -1):
        for j in range(i-1, -1, -1):
            ratio = A[j][i] / A[i][i]
            for k in range(n):
                A[j][k] = A[j][k] - ratio * A[i][k]
            b[j] = b[j] - ratio * b[i]
    x = np.zeros(n)
    for i in range(n):
        x[i] = b[i] / A[i][i]
    return x

A = np.array([[-1, 0, 6, 4], [1, 3, 2, 1], [2, 9, 1, 2], [8, 1, 3, 2]])
b = np.array([4, 3, 2, 1])

x = gauss_jordan(A, b)
print("Solusi sistem persamaan linier:")
print(x)

# Metode Iterasi Jacobi:

def jacobi(A, b, x0, tol, max_iter):
    n = len(A)
    x = np.zeros(n)
    for i in range(max_iter):
        for j in range(n):
            s = 0
            for k in range(n):
                if k != j:
                    s += A[j][k] * x0[k]
            x[j] = (b[j] - s) / A[j][j]
        if np.linalg.norm(x - x0) < tol:
            return x
        x0 = x.copy()
    return x

A = np.array([[-1, 0, 6, 4], [1, 3, 2, 1], [2, 9, 1, 2], [8, 1, 3, 2]])
b = np.array([4, 3, 2, 1])
x0 = np.zeros(len(A))
tol = 1e-6
max_iter = 100

x = jacobi(A, b, x0, tol, max_iter)
print("Solusi sistem persamaan linier:")
print(x)
