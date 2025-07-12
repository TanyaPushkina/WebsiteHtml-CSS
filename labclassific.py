import numpy as np
import matplotlib.pyplot as plt
import random

w_1 = np.array([[-0.5, 1, 0], [0.5, 1, -1]])
w_2 = np.array([1, -1])

def active(z):
    if (z > 0):
        return 1
    else:
        return 0


x_values = [0, 1]
y_values = [0, 0.5]
x1_values = [0, 1]
y1_values = [1, 0.5]


plt.plot(x_values, y_values, color='blue')
plt.plot(x1_values, y1_values, color='blue')
plt.title('Определение кота и собаки')

dogs_x = []
dogs_y = []
cats_x = []
cats_y = []
for i in range(10):
    x = np.array([[random.uniform(0, 1)], [random.uniform(0, 1)], [1]])
    ans = np.dot(w_1, x)
    ans_1 = [active(x) for x in ans]
    result = np.dot (w_2,ans_1)
    if active(result):
        cats_x.append(x[0])
        cats_y.append(x[1])
    else:
        dogs_x.append(x[0])
        dogs_y.append(x[1])



plt.scatter(dogs_x, dogs_y, s=10, color='blue', label='Собака')
plt.scatter(cats_x, cats_y, s=10, color='red', label='Кошка')
plt.grid(True)
plt.legend()
plt.show()