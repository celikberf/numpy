import numpy as np

#python list
py_list = [1,2,3,4,5,6,7,8,9]

#numpy array
np_array = np.array([1,2,3,4,5,6,7,8,9])

print(type(py_list))
print(type(np_array))

py_multi = [[1,2,3],[4,5,6],[7,8,9]]
np_multi = np_array.reshape(3,3)# nummpy dizisini şekillendirme.Matris oluşturma

print(py_multi)
print(np_multi)

print(np_array.ndim) # 1 boyutlu
print(np_multi.ndim) # 2 boyutlu

print(np_array.shape) # (9,) tek boyutlu matris
print(np_multi.shape) # (3,3) 2 boyutlu matris