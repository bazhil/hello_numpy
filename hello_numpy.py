import numpy as np

# создание списка numpy
np_arr = np.array([i for i in range(10)])
print('создание списка numpy: \n', np_arr)
print('-'*80, '\n')

# получение максимального элемента в списке
max_in_np_arr = np_arr.max()
print('получение максимального элемента в списке: \n', max_in_np_arr)
print('-'*80, '\n')

# создание списка длинной в 10 элементов из случайных элементов
rand_arr = np.random.random(10)
print('создание списка длинной в 10 элементов из случайных элементов: \n', rand_arr)
print('-'*80, '\n')

# умножение всех элмементов списка на число
rand_arr_proc = rand_arr * 100
print('умножение всех элмементов списка на число: \n', rand_arr_proc)
print('-'*80, '\n')

# объединение массивов
combined_arr = np.stack((np_arr, rand_arr, rand_arr_proc))
print('объединение массивов ({}, {}, {}): \n'.format(np_arr, rand_arr, rand_arr_proc), combined_arr)
print('-'*80, '\n')

# получение суммы всех элементов списка
rand_arr_sum = rand_arr.sum()
print('получение суммы всех элементов списка: \n', rand_arr_sum)
print('-'*80, '\n')

# получение среднего значение суммы всех элементов списка
rand_arr_av = rand_arr.mean()
print('получение среднего значение суммы всех элементов списка: \n', rand_arr_av)
print('-'*80, '\n')

# умножение всех элементов списка
rand_arr_pr = rand_arr.prod()
print('умножение всех элементов списка: \n', rand_arr_pr)
print('-'*80, '\n')

# получение среднего квадратичного всех элементов списка
rand_arr_std = rand_arr.std()
print('получение среднего квадратичного всех элементов списка: \n', rand_arr_std)
print('-'*80, '\n')

# создание матрицы из двух списков одинаковой размерности
matrix = np.array([np_arr, rand_arr])
print('создание матрицы из двух списков одинаковой размерности: \n', matrix)
print('-'*80, '\n')

# создание матрицы заданной размерности из рандомных чисел
random_matrix = np.random.random((2, 10))
print('оздание матрицы заданной размерности из рандомных чисел: \n', random_matrix)
print('-'*80, '\n')

# сложение матриц
sum_matrix = random_matrix + matrix
print('сложение матриц: \n', sum_matrix)
print('-'*80, '\n')

# скалярное умножение матриц
scalar_multiplex = random_matrix.dot(np.random.random((10, 3)))
print('скалярное умножение матриц: \n', scalar_multiplex)
print('-'*80, '\n')

# транспонирование матрицы (поворот)
scalar_transpon = scalar_multiplex.T
print('транспонирование матрицы (поворот): \n', scalar_transpon)
print('-'*80, '\n')

# создание ndarray
nd_arr = np.array([np_arr, np_arr*2.3])
print('создание ndarray: \n', nd_arr)
print('-'*80, '\n')

# вычисление среднеквадратической ошибки
error = (1/len(np_arr)) * np.sum(np.square(np_arr - np_arr*0.3))
print('вычисление среднеквадратической ошибки: \n', error)
print('-'*80, '\n')

# взять размеры уже существующего массива
b = np.zeros_like(scalar_transpon)
print('Использование размеров уже существующего массива {}: \n'.format(scalar_transpon), b)
print('-'*80, '\n')

# массив чисел от From (включая) до To (не включая) с шагом Step:
From = rand_arr_av
To = (np_arr * 100).mean()
Step = 0.5
A = np.arange(From, To, Step)
print('Построение массива чисел от {} (включая) до {} (не включая) с шагом {}:\n'.format(From, To, Step), A)
print('-'*80, '\n')
B = np.arange(10)
print('Построение массива чисел со значениями по умолчанию (from = 0, step = 1): \n', B)
print('-'*80, '\n')

# форма массива и её изменение
A = np.arange(100)
B = A.reshape(10, 10)
C = B.reshape(5, 10, 2)
print('B\n', B)
print('\nC\n', C)
print(A.ndim, A.shape, len(A.shape), A.size)
print(B.ndim, B.shape, len(B.shape), B.size)
print(C.ndim, C.shape, len(C.shape), C.size)
print('-'*80, '\n')

# клонирование данных
A = np.repeat(rand_arr_proc, 3)
B = np.stack((A, A))
print(A)
print(B)
print('-'*80, '\n')

# агрегаторы
Ag = np.random.rand(4, 6)
print('A\n', Ag, '\n')
print('min\n', np.min(Ag, 1), '\n')
print('max\n', np.max(Ag, 0), '\n')
print('mean\n', np.mean(Ag, 1), '\n')
print('average\n', np.average(Ag, 0), '\n')
print('mean\n', np.mean(Ag, (0, 1)), '\n')
print('-'*80, '\n')