import numpy as np


def solve(grad_y, A, b):
    grad_y = grad_y.reshape((-1, 1))
    grad_x = np.sum(grad_y * A, axis=0)

    return grad_x


if __name__ == "__main__":
    grad_y = np.array([5, 12])

    A = np.array([[5, 3], [7, 2]])
    b = np.array([1, 9])

    grad_x = solve(grad_y, A, b)
    print("Gradient of f respect to x : ", grad_x)
