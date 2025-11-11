# a=int(input("Enter a Number :"))
# if(a==1):
#    print("Monday")
# elif(a==2):
#     print("Tuesday")
# elif(a==3):
#     print("Wednesday")
# elif(a==4):
#     print("Thursday")
# elif(a==5):
#     print("Friday")
# elif(a==6):
#     print("Saturday")
# elif(a==7):
#     print("Sunday")
# else:
#     print("Wrong Input") 

           
num=int(input("Enter a Number :"))  
while(num%2==0):
    print("Number is even")      
    break
else:
    print("Number is odd")