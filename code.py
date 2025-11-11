list=[2,5,3,5,7,2]
# print("Smallest element in the list : ",min(list))
# print("Largest element : ",max(list))
# n=len(list)
# print(list[0:n//2:1])
# print(list[n//2:n])
# print("First element : ",list[0])
# print("Last element : ",list[n-1])
for i in range(len(list)):
   print(list[i]*list[i])

# list1=[23,23,2,67,23,2,45,67]
# count=0
# for i in list1:
#    for j in list1:
#        if i==j:
#             count+=1
#             print(j)  

for i in range(len(list)):
    if i%2==0:
        print("Even Numbers",i)
for i in range(len(list)):        
    if i%2!=0:
        print("Odd Numbers",i)    
    
r=filter(lambda )    