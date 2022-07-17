import numpy as np

arr = np.array([1, 5, 6, 20])
#a = 3int b = 3int while a = b the
arr2 = np.sqrt(arr)
arr3 = np.linspace (1, 50, 20)
arr4 = np.random.random(6)
arr5 = np.exp(arr4)

print(arr)
print(arr2)
print(arr2.size)
print(arr3)
print('По русски понимает даже это рандомный массив',arr4)
print('Это экспонента чтоли',arr5)
a = arr5
b = arr4
c = a + b
print('Это сумма',c)
print(c.max())
d = np.insert(arr5, 1, 5)
print('Вставляем в массив на позицию 1 цифру5', d)
d[0] = 3
print('Тут первое ну нулевое число изменили на 3 по индексу ',d)
h = 'Тут все из списка что меньше 2 и каждый раз разные потому что выше рандомные'
print(h, arr5 [arr5 < 2])
