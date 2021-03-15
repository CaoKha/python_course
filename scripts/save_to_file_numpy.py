import numpy as np

# file handle
a = np.array([1, 2, 3, 4, 5])
np.save('/home/kha/Documents/python_course/files/outfile', a)

b = np.load('files/outfile.npy')
print(b)

# example 0
entry = np.array([[1, 2], [3, -4]])
outry = np.array([[3], [1]])

solution = np.linalg.solve(entry, outry)
print(f"x = {solution[0,0]:1.2f} and y = {solution[1,0]}") 
names = np.array(["Denis", "Reant", "Formator"])
matricules = np.array([0.0701, 15.5895, 0.11723])

data = np.zeros(
    names.size, dtype=[("var1", "U8"), ("var2", float)]
)  # U7 = unicode string with 8 characters
data["var1"] = names
data["var2"] = matricules

np.savetxt(
    "files/example3.txt",
    data,
    fmt="%10s %2.3f",
    newline="\n",
    header="Liste and matricule of formator: ",
    footer="This is a footer!",
    comments="# This is a comment!\n",
)