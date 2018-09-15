'''
Cho 3 điểm 𝑎, 𝑏, 𝑐 trong không gian 3 chiều với tọa độ (2, 4, 5), (4, 7, 9), (7, 9, 2). Viết chương
trình tìm hình chiếu của điểm 𝑑 với tọa độ (30, 25, 56) trên mặt phẳng tạo bởi ba điểm 𝑎, 𝑏, 𝑐.
'''

import numpy as np


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_coordinate(self, axis=None):
        if axis == 0:
            return self.x
        elif axis == 1:
            return self.y
        elif axis == 2:
            return self.z
        else:
            return np.array([self.x, self.y, self.z])


class Plane:
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

        self.build_vector_n()
        self.build_vector_params()

    def build_vector_n(self):
        # Tính vector pháp tuyến của mặt phẳng
        u1 = get_vector(self.point1, self.point2)
        u2 = get_vector(self.point1, self.point3)
        # Vector pháp tuyến n bằng tích có hướng của 2 vector chỉ phương
        self.vector_n = get_direction_product(u1, u2)

    def build_vector_params(self):
        a, b, c = self.vector_n[0], self.vector_n[1], self.vector_n[2]
        d = - np.sum(self.vector_n * self.point1.get_coordinate())

        # Phương trình mặt phẳng có dạng ax + by + cz + d = 0
        self.params = np.array([a, b, c, d])

    def get_params(self):
        return self.params.tolist()

    def get_foot_of_perpendicular(self, point):
        # Tìm hình chiếu vuông góc của 1 điểm trên mặt phẳng
        x0 = point.get_coordinate(axis=0)
        y0 = point.get_coordinate(axis=1)
        z0 = point.get_coordinate(axis=2)
        a, b, c, d = self.get_params()

        t = (-d - a*x0 - b*y0 - c*z0) / (a*a + b*b + c*c)

        return Point(x0 + a*t, y0 + b*t, z0 + c*t)


def get_vector(point1, point2):
    return point2.get_coordinate() - point1.get_coordinate()


def get_direction_product(vector1, vector2):
    '''
    :param vector1:
    :param vector2:
    :return: Tính tích có hướng của 2 vector
    '''

    x1, y1, z1 = vector1[0], vector1[1], vector1[2]
    x2, y2, z2 = vector2[0], vector2[1], vector2[2]

    x = y1 * z2 - y2 * z1
    y = z1 * x2 - z2 * x1
    z = x1 * y2 - x2 * y1
    result = np.array([x, y, z])

    print("Direction_Product : {} * {} = {}".format(vector1, vector2, result))
    return result


if __name__ == "__main__":
    p1 = Point(2, 4, 5)
    p2 = Point(4, 7, 9)
    p3 = Point(7, 9, 2)

    plane = Plane(p1, p2, p3)

    m = Point(30, 25, 56)
    print("Params of plane : ", plane.get_params())
    print("Foot of perpendicular : ", plane.get_foot_of_perpendicular(m).get_coordinate())
