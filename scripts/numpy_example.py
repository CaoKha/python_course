import numpy as np
import sympy as sym
import math as m

# a = np.array([1, 2, 3])
# print(a)

# # complex number with numpy
# a = np.array([1, 2, 3], dtype=complex)
# print(a)

# # file handle
# a = np.array([1, 2, 3, 4, 5])
# np.save('/home/kha/Documents/python_course/files/outfile', a)

# b = np.load('files/outfile.npy')
# print(b)

x = sym.symbols("x")
y = sym.symbols("y")
z = sym.symbols("z")


print(
    f"simplification of sin(x)**2 + cos(x)**2= {sym.simplify(m.sin(x)**2+m.cos(x)**2)}"
)
