import numpy as np
from numpy.core._multiarray_umath import ndarray

arr = np.array([1, 5, 6, 20])
# a = 3int b = 3int while a = b the
arr2 = np.sqrt(arr)
arr3 = np.linspace(1, 50, 20)
arr4 = np.random.random(6)
arr5 = np.exp(arr4)

print(arr)
print(arr2)
print(arr2.size)
print(arr3)
print('По русски понимает даже это рандомный массив', arr4)
print('Это экспонента чтоли', arr5)
a = arr5
b = arr4
c = a + b
print('Это сумма', c)
print(c.max())
d = np.insert(arr5, 1, 5)
print('Вставляем в массив на позицию 1 цифру5', d)
d[0] = 3
print('Тут первое ну нулевое число изменили на 3 по индексу ', d)
h = 'Тут все из списка что меньше 2 и каждый раз разные потому что выше рандомные'
print(h, arr5[arr5 < 2])

matrix = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)], dtype=np.float64)
print(matrix)
print(matrix.min())
print(matrix.size)
print(matrix.reshape(1, 9))  # отбалды менять нельзя будет ошибка
mk = matrix = np.resize(matrix, (2, 3))
print('Отрезал', mk)  # здесь отрежет и выкенет лишнее по порядку вроде

matrix2 = np.arange(32).reshape(4, 8)
print(matrix2)
ma = np.zeros((4, 8))
print(ma)
nslo = np.eye(4)  # квадратная матрица и на главной диагонали 1
sw = matrix2 * matrix2
sd = np.delete(sw, 7, axis=1) # тут указываешь строку или столбец нумерация с0
print(sw)
print(sd)
print(sd.sum(),'Сумма и в квадрате', sd**2)
arr6 = np.concatenate((sd, ma), axis=1) # Надо по человечески переменые называть тут уже стал путатться
print(arr6)
sa = np.append(arr6, np.array([22, 42, 5, 6, 7, 8, 9, 1, 3, 4, 5, 6, 7, 7, 6]))
print('Тут выше добавили к ними строку чисел' ,sa) # без переменой не работает
print('Индекс чтоб найти число по номеру', sd[2, 1]) # тут уже лезут ошибки если искать в другом, надо снова переменую вводить???
arrtranspone = arr6.transpose()
print(arrtranspone) # разворот матрицы
#np.savetxt('с юьюба примеры.txt', arrtranspone, delimiter='')



