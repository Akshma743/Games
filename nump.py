import numpy as np;
n1=np.array([2,4,6,8])

n2=np.array([5,2,7,9])
print("vstack")
print(np.vstack((n1,n2)))
print("hstack")
print(np.hstack((n1,n2)))
print("columnstack")
print(np.column_stack((n1,n2)))
print("Sum is")
print(n1+n2)
print("Substraction is : ")
print(n1-n2)
print("Multiplication is : ")
print(n1*n2)
print(np.sort(n1))
print(np.power(n1,2))
print(np.divide(n1,3))



