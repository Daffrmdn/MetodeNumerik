import numpy as np

def runge_kutta_3(func, y0, t0, tf, h):
    t = np.arange(t0, tf+h, h)
    y = np.zeros((len(t), len(y0)))
    y[0] = y0
    for i in range(1, len(t)):
        k1 = func(t[i-1], y[i-1])
        k2 = func(t[i-1] + 0.5*h, y[i-1] + 0.5*h*k1)
        k3 = func(t[i-1] + h, y[i-1] - h*k1 + 2*h*k2)
        y[i] = y[i-1] + (h/6) * (k1 + 4*k2 + k3)
    return t, y

def test_case_1(t, y):
    return -2*y[0] + 2*y[1]

def test_case_2(t, y):
    return np.array([y[1], -0.05*y[1] + 0.15*y[0]])

# Tes kasus (a)
t0, tf = 0, 2
h = 0.1
y0 = np.array([1, 1])
t, y = runge_kutta_3(test_case_1, y0, t0, tf, h)
print("Hasil y(2) untuk kasus (a) adalah:", y[-1][0])

# Tes kasus (b)
t0, tf = 0, 2
h = 0.1
y0 = np.array([1, 0])
t, y = runge_kutta_3(test_case_2, y0, t0, tf, h)
print("Hasil y(2) untuk kasus (b) adalah:", y[-1][0])
