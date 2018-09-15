'''
Viết chương trình giải hệ phương trình tuyến tính sau bằng phương pháp khử Gauss
'''

import numpy as np


def solve_linear_system(A, b):
    # Find vector x that Ax = b
    matrix = np.concatenate((A, b), axis=1)

    # Khử xuôi
    for row in range(matrix.shape[0] - 1):
        factor = - matrix[row + 1:, row] / matrix[row, row]
        factor = factor.reshape((-1, 1))
        matrix[row + 1:] = matrix[row + 1:] + matrix[row] * factor

    # Thế ngược
    for row in range(matrix.shape[0] - 1, 0, -1):
        factor = - matrix[:row, row] / matrix[row, row]
        factor = factor.reshape((-1, 1))
        matrix[:row] = matrix[:row] + matrix[row] * factor

    x = matrix[:, -1] / matrix.diagonal()
    return x


if __name__ == "__main__":
    A = np.array([
        [3, 4, 2, 7],
        [7, 5, 1, 9],
        [8, 12, 25, 3],
        [9, 11, 15, 7]
    ], dtype=np.float32)

    b = np.array([129, 151, 709, 505], dtype=np.float32).reshape((-1, 1))

    x = solve_linear_system(A, b)
    print("Solve linear system of equations : ")
    print(x)
