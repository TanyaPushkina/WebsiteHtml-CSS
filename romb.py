import numpy as np
import matplotlib.pyplot as plt
import random

# Функция проверки точки на попадание в ромб
def in_diamond(x, y, center=(0.5, 0.5), size=0.5):
    return abs(x - center[0]) + abs(y - center[1]) <= size

# Координаты для отрисовки ромба
diamond_x = [0.5, 1, 0.5, 0, 0.5]
diamond_y = [0, 0.5, 1, 0.5, 0]

# Рисуем ромб на графике
plt.plot(diamond_x, diamond_y, color='purple', linewidth=1.5)
plt.title('Задача классификация: определение кота и собаки')

# Списки координат для собак и кошек
dogs_x, dogs_y = [], []
cats_x, cats_y = [], []

# Генерация и классификация точек
for i in range(20):
    x, y = random.uniform(0, 1), random.uniform(0, 1)
    if in_diamond(x, y):
        cats_x.append(x)
        cats_y.append(y)
    else:
        dogs_x.append(x)
        dogs_y.append(y)

# Отрисовываем точки
plt.scatter(dogs_x, dogs_y, s=20, color='green', label='Собака')
plt.scatter(cats_x, cats_y, s=20, color='pink', label='Кошка')

# Настройки графика
plt.grid(True)
plt.legend()
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
