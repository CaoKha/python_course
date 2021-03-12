import numpy as np
# a = np.array([1, 2, 3])
# print(a)

# # dtype parameter
# a = np.array([1, 2, 3], dtype=complex)
# print(a)

a = np.array([1, 2, 3, 4, 5])
np.save('/home/kha/Documents/python_course/files/outfile', a)

b = np.load('files/outfile.npy') 
print(b)