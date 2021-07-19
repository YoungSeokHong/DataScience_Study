import numpy as np
from numpy.core.fromnumeric import shape

array1 = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
print(array1)
print("Type of array1 : " + str(type(array1)))
print()

array2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(array2)
print("Type of array2 : " + str(type(array2)))
print("Shape of array2 : " + str(shape(array2)))
print()

array3 = np.full(6, 2)
print(array3)

array4 = np.zeros(6)
print(array4)

array5 = np.arange(1, 7)
print(array5)

print(array3 + array5)
print(array5 * 2)
print(array5)
print()

array5 *= 2
print(array5)