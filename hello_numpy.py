import numpy as np

# создание списка numpy
np_arr = np.array([i for i in range(10)])
print('создание списка numpy: \n', np_arr)
print(''*80, '\n')

# получение максимального элемента в списке
max_in_np_arr = np_arr.max()
print('получение максимального элемента в списке: \n', max_in_np_arr)
print(''*80, '\n')

# создание списка длинной в 10 элементов из случайных элементов
rand_arr = np.random.random(10)
print('создание списка длинной в 10 элементов из случайных элементов: \n', rand_arr)
print(''*80, '\n')

# умножение всех элмементов списка на число
rand_arr_proc = rand_arr * 100
print('умножение всех элмементов списка на число: \n', rand_arr_proc)
print(''*80, '\n')

# получение суммы всех элементов списка
rand_arr_sum = rand_arr.sum()
print('получение суммы всех элементов списка: \n', rand_arr_sum)
print(''*80, '\n')

# получение среднего значение суммы всех элементов списка
rand_arr_av = rand_arr.mean()
print('получение среднего значение суммы всех элементов списка: \n', rand_arr_av)
print(''*80, '\n')

# умножение всех элементов списка
rand_arr_pr = rand_arr.prod()
print('умножение всех элементов списка: \n', rand_arr_pr)
print(''*80, '\n')

# получение среднего квадратичного всех элементов списка
rand_arr_std = rand_arr.std()
print('получение среднего квадратичного всех элементов списка: \n', rand_arr_std)
print(''*80, '\n')

# создание матрицы из двух списков одинаковой размерности
matrix = np.array([np_arr, rand_arr])
print('создание матрицы из двух списков одинаковой размерности: \n', matrix)
print(''*80, '\n')

# создание матрицы заданной размерности из рандомных чисел
random_matrix = np.random.random((2, 10))
print('оздание матрицы заданной размерности из рандомных чисел: \n', random_matrix)
print(''*80, '\n')

# сложение матриц
sum_matrix = random_matrix + matrix
print('сложение матриц: \n', sum_matrix)
print(''*80, '\n')

# скалярное умножение матриц
scalar_multiplex = random_matrix.dot(np.random.random((10, 3)))
print('скалярное умножение матриц: \n', scalar_multiplex)
print(''*80, '\n')

# транспонирование матрицы (поворот)
scalar_transpon = scalar_multiplex.T
print('транспонирование матрицы (поворот): \n', scalar_transpon)
print(''*80, '\n')

# создание ndarray
nd_arr = np.array([np_arr, np_arr*2.3])
print('создание ndarray: \n', nd_arr)
print(''*80, '\n')

# вычисление среднеквадратической ошибки
error = (1/len(np_arr)) * np.sum(np.square(np_arr - np_arr*0.3))
print('вычисление среднеквадратической ошибки: \n', error)
print(''*80, '\n')
