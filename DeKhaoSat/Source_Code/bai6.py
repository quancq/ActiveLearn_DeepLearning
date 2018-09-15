'''
Cho hàm 𝑓(𝑥) = 4𝑥4 + 5𝑥3 − 2𝑥2 + 3𝑥 + 7. Viết chương trình tìm ít nhất một giá trị của 𝑥 (giá
trị xấp xỉ) để 𝑓(𝑥) = 1000
'''

import numpy as np
from math import pow


def solve_equation_by_newton(f, grad, epsilon=1e-8):
    x = 1
    while abs(f(x)) > epsilon:
        x = x - f(x) / grad(x)

    return x


def f(x):
    return 4*pow(x, 4) + 5*pow(x, 3) - 2*x*x + 3*x - 993


def grad(x):
    return 16*pow(x, 3) + 15*x*x - 4*x + 3


if __name__ == "__main__":
    root = solve_equation_by_newton(f, grad)

    print("Root = ", root)
