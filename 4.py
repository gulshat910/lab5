import numpy as np
import matplotlib.pyplot as plt

# Создание матрицы 5×5 со случайными целыми числами от 1 до 10
matrix = np.random.randint(1, 11, size=(5, 5))
print("Матрица:")
print(matrix)

# Построение тепловой карты
plt.imshow(matrix, cmap='viridis')
plt.colorbar()

# Добавление аннотаций чисел в ячейках
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        plt.text(j, i, str(matrix[i, j]), ha='center', va='center', color='white')

# Отображение тепловой карты
plt.title("Тепловая карта матрицы")
plt.show()
