import numpy as np

x = np.arange(0, 6).reshape(-1, 2)
theta = np.array([2, 5]).reshape(-1, 2)
print("x_shape = {}, theta_shape = {}".format(x.shape, theta.shape))
print("x :")
print(x)
print("theta :")
print(theta)

print("============")
print(np.dot(x, theta.T))
print("Cach 2: ")
print(np.sum(theta * x, axis=1))
