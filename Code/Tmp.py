import numpy as np

x = np.arange(0, 6).reshape(2, 3)
y = np.array([-1, 2, 3])

z = np.dot(x,y)
print(x)
print(y)
print('==========')
print(z)