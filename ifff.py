stu1=90
stu2=78
if(stu1>stu2):
   print("Student1 ")
elif(stu2>stu1):
   print("Student2")
else:
   print("Invalid")
    
a=10
if(a>0):
   if(a==10):
      print("Value of a=10")  
   elif(a<10):
       print("Value of a is less than 10")
   else:
       print("Value of a is greater than 10")


age=12
eligible="Adult" if age>18 else "Minor"
print(eligible)

for i in range(5):
   print(i)
   
   
i=5
while(i>0 and i==5):
   print(i)
   i+=1   

for i in range(5):
   for j in range(3):  
      print(i,j)   
 
for i in range(10):
    if(i==5):
        c    ontinue
    if(i==8):
        break
    print(i)      