list1=[2,4,5,6,67,45,23]
#accessing all elements of list
print("List elements are : ")
for i in list1:
    print(i)
    
#pop() operation
print("poped element : ",list1.pop(3))

#append operation
list1.append(3)
print("After Appending",list1)

#insert operator
list1.insert(0,24)
print("After insertion",list1)

#sorting operation
list1.sort()
print("after Sorting : ",list1)

#print length of list
r=len(list1)
print("Length of list : ",r)

#reverse of list
list1.reverse()
print("Revrse : ",list1)

#slicing
print("Slicing : ",list1[1::2])

#remove operation 
list1.remove(23)
print("After removing : ",list1)

list.append(34)
print(list             )

