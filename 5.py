import matplotlib.pyplot as plt
import numpy as np

# Создание фигуры с 3 областями
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(6, 10))

# Линейный график y = x^2
x = np.linspace(-5, 5, 100)
y = x**2
axes[0].plot(x, y)
axes[0].set_title('Линейный график y = x^2')
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')

# Точечный график случайных точек
random_x = np.random.rand(50)
random_y = np.random.rand(50)
axes[1].scatter(random_x, random_y)
axes[1].set_title('Точечный график случайных точек')
axes[1].set_xlabel('x')
axes[1].set_ylabel('y')

# Столбчатая диаграмма для категориальных данных
categories = ['A', 'B', 'C']
values = [3, 7, 2]
axes[2].bar(categories, values)
axes[2].set_title('Столбчатая диаграмма')
axes[2].set_xlabel('Категории')
axes[2].set_ylabel('Значения')

# Отображение графика
plt.tight_layout()
plt.show()
