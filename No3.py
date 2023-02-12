import numpy as np
# (a) Aturan trapesium:
def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    result = 0.5 * f(a) + 0.5 * f(b)
    for i in range(1, n):
        result += f(a + i * h)
    result *= h
    return result

def f(x):
    return np.exp(2 * x)

if __name__ == '__main__':
    a = 0
    b = 1
    n = int(input("Masukkan n: "))
    result = trapezoidal_rule(f, a, b, n)
    print("Hasil integral menggunakan aturan trapesium:", result)

# (b) Simpson 1/3
def simpson_13(f, a, b, n):
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n, 2):
        result += 4 * f(a + i * h)
    for i in range(2, n - 1, 2):
        result += 2 * f(a + i * h)
    result *= h / 3
    return result

def f(x):
    return np.exp(2 * x)

if __name__ == '__main__':
    a = 0
    b = 1
    n = int(input("Masukkan n: "))
    result = simpson_13(f, a, b, n)
    print("Hasil integral menggunakan Simpson 1/3:", result)
