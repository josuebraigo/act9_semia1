import numpy as np

def sphere(x):
    total=0
    for i in range(len(x)):
        total += x[i] ** 2
    return total

def rosenbroc(x):
    total=0
    for i in range(len(x) - 1):
        total += 100 * (x[i + 1] - x[i] ** 2) ** 2 + (x[i] - 1) ** 2
    
    return total

def rastring(x):
    total = 0
    for i in range(len(x)):
        total += (x[i]**2 - 10 * np.cos(2 * np.pi * x[i])) + ((x[i] + 1)**2 - 10 * np.cos(2 * np.pi * (x[i] + 1))) + 20
    return total

def quartic(x):
    total = 0
    for i in range(len(x)):
        total += i * x[i] ** 4
    return total