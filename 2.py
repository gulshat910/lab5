import numpy as np
import matplotlib.pyplot as plt

# Генерация массива из 1000 случайных чисел с нормальным распределением
data = np.random.normal(size=1000)

# Построение гистограммы с 20 столбцами
plt.hist(data, bins=20)

# Добавление подписей и заголовка
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.title('Гистограмма случайных чисел с нормальным распределением')

# Отображение гистограммы
plt.show()
