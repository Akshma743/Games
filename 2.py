import numpy as np
d= np.genfromtxt("info.csv", delimiter=",", dtype=str, skip_header=1)

print("Imported Dataset:\n", d)


names = d[:, 0]   
age = d[:, 1]    
mark = d[:, 2]

print("\nNames:", names)
print("Age:", age.astype(int))   
print("Mark:", mark.astype(int))