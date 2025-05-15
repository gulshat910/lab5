import numpy as np

# Создание матрицы 5×5 со случайными целыми числами от 1 до 10
matrix = np.random.randint(1, 11, size=(5, 5))
print("Матрица:")
print(matrix)

# Среднее значение
mean_value = np.mean(matrix)
print("Среднее значение:", mean_value)

# Максимальный элемент
max_value = np.max(matrix)
print("Максимальный элемент:", max_value)

# Минимальный элемент
min_value = np.min(matrix)
print("Минимальный элемент:", min_value)

# Сумма по столбцам
column_sums = np.sum(matrix, axis=0)
print("Сумма по столбцам:", column_sums)
