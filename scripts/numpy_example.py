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

# # example 0
# entry = np.array([[1, 2], [3, -4]])
# outry = np.array([[3], [1]])

# solution = np.linalg.solve(entry, outry)
# print(f"x = {solution[0,0]:1.2f} and y = {solution[1,0]}") 
# names = np.array(["Denis", "Reant", "Formator"])
# matricules = np.array([0.0701, 15.5895, 0.11723])

# data = np.zeros(
#     names.size, dtype=[("var1", "U8"), ("var2", float)]
# )  # U7 = unicode string with 8 characters
# data["var1"] = names
# data["var2"] = matricules

# np.savetxt(
#     "files/example3.txt",
#     data,
#     fmt="%10s %2.3f",
#     newline="\n",
#     header="Liste and matricule of formator: ",
#     footer="This is a footer!",
#     comments="# This is a comment!\n",
# )

x = sym.symbols("x")
y = sym.symbols("y")
z = sym.symbols("z")

# simplify function
a = sym.simplify(sym.sin(x) ** 2 + sym.cos(x) ** 2)
b = sym.simplify((x ** 3 + x ** 2 - x - 1) / (x ** 2 + 2 * x + 1))
print(f"simplification of sin(x)**2 + cos(x)**2= {a}")
print(f"simplification of (x**3 + x**2 - x - 1)/(x**2 + 2*x + 1) = {b}")

# expand function
c = sym.expand((x + 1) ** 2)
d = sym.expand((x+2)*(x+3))
e = sym.expand_trig(sym.sin(x+y))
print(f"Development of (x + 1)**2 = {c}")
print(f"Development of (x+2)*(x+3) = {d}")
print(f"Development of sin(x+y) = {e}")

# factor function
f = sym.factor(x**2*z + 4*x*y*z + a*y**2*z)
g = sym.factor(sym.cos(x)**2 + 2*sym.cos(x)*sym.sin(x) + sym.sin(x)**2)
print(f"Factor of x**2*z + 4*x*y*z + a*y**2*z = {f}")
print(f"Factor of cos(x)**x + 2*cos(x)*sin(x) + sin(x)**2 = {g}")

# derivative function
h = sym.diff(sym.cos(x),x)
i = sym.diff(x**4,x,3)
print(f"The derivative of cos(x) = {h}")
print(f"The 3rd derivative of x**4 = {i}")

# integrate function
k = sym.integrate(1/x,x)
l = sym.integrate(sym.exp(-x),(x,0,m.inf))
print(f"Integrate of 1/x = {k}")
print(f"Integrate of exp(-x) from 0 to infinite = {l}")

# limit function
m = sym.limit(sym.sin(x)/x,x,0)
n = sym.limit(1/x,x,0,'+')
print(f"The limit of sin(x)/x with x close to 0 = {m}")
print(f"The limit of 1/x with x close to 0+ = {n}")
