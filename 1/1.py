import numpy as np
import matplotlib.pyplot as plt

# Генерация массива x
x = np.linspace(0, 10, 100)

# Расчет y и z
y = np.sin(x)
z = np.cos(x)

# Построение графиков
plt.plot(x, y, label='sin(x)')
plt.plot(x, z, label='cos(x)')

# Добавление легенды, подписей осей и заголовка
plt.legend()
plt.xlabel('x')
plt.ylabel('y, z')
plt.title('Графики функций sin(x) и cos(x)')

# Отображение графиков
plt.show()
