import numpy as np
import matplotlib.pyplot as plt
import random

# матрица весов 1ого слоя (2 нейрона, входа каждый)
w_1 = np.array([[-0.5, 1, 0], [0.5, 1, -1]])

# нейрон 1:        z = -0.5 * x + 1 * y + 0
# z > 0, когда y > 0.5x
# Нейрон 2:        z = 0.5 * x + 1 * y - 1
# z > 0, когда y > -0.5x + 1



#матрица весов 2ого слоя (выходной слой с 2умя выходами)
w_2 = np.array([1, -1])

# понадобится для result

#функция активации
def active(z):
    if (z > 0):
        return 1
    else:
        return 0



#координаты первой линии треугольника
x_values = [0, 1]
y_values = [0, 0.5]

#координаты второй линии треугольника
x1_values = [0, 1]
y1_values = [1, 0.5]


plt.plot(x_values, y_values, color='purple')
plt.plot(x1_values, y1_values, color='purple')
plt.title('Определение кота и собаки')

#списки пустые для координат точек, класифицированных как собаки
dogs_x = []
dogs_y = []


#списки пустые для координат точек, класифицированных как кошки
cats_x = []
cats_y = []

for i in range(20):

#генерируем случайною точку от 0 до 1, добавляем 1 для смещения 
    x = np.array([[random.uniform(0, 1)], [random.uniform(0, 1)], [1]])

#считаем выход 1ого слоя нейронов(веса перемножаем с входными данными)
    ans = np.dot(w_1, x)

#применяем функцию активации для каждого нейрона первого слоя 
    ans_1 = [active(x) for x in ans]

#считаем выход 2ого слоя нейронов
    result = np.dot (w_2,ans_1)


    if active(result) == 1:

        cats_x.append(x[0])
        cats_y.append(x[1])

    else:

        dogs_x.append(x[0])    
        dogs_y.append(x[1])



plt.scatter(dogs_x, dogs_y, s=11, color='green', label='Собака')
plt.scatter(cats_x, cats_y, s=11, color='pink', label='Кошка')
plt.grid(True)
plt.legend()
plt.show()