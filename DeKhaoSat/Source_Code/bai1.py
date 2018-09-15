'''
Viết chương trính tính 𝑓(𝑥) = √𝑥 với 𝑥 > 0 mà không sử dụng hàm thư viện sqrt có sẵn. Gợi ý:
Bạn không nên dùng phương pháp tìm kiếm nhị phân (binary search).
'''

import timeit
import math


def approximate_sqrt_newton(x, epsilon=1e-8):
    result = 1
    while abs(result * result - x) > epsilon:
        result = (result + x / result) / 2
    return result


def my_sqrt(x):
    if x == 0: return 0
    return math.tan(math.acos((x - x*x) / (x + x*x)) / 2)


if __name__ == "__main__":
    x = 2
    print("Epsilon = {}".format(abs(math.sqrt(x) - my_sqrt(x))))
    print("Epsilon = {}".format(abs(math.sqrt(x) - approximate_sqrt_newton(x))))