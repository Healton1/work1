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