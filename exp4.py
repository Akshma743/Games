import numpy as np

a = np.array([[1, 12, 30, 40, 51],
             [14, 15, 16, 17, 18],
             [7, 80, 9, 5, 1],
             [2, 5, 6, 9, 10],
             [1, 2, 3, 4, 5]])

print("Original Array:\n", a)
a[:, [0, 2]] = a[:, [2, 0]]

print("\nArray After Swapping Column 0 and 2:\n", a)