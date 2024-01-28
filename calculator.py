input1=int (input("Enter a number: "))
input2=int (input("Enter a number: "))
a=input1
b=input2
print("What do you want to do?")
user_add=int (input("1.Add\n2.Substract\n3.Divide\n4.Multiply\n"))
if(user_add==1):
    c=a+b
    print("The addition is: ",c)
elif(user_add==2):
    c=a-b
    print("The substraction is: ",c)
elif(user_add==3):
    c=a/b
    print("The division is: ",c)
elif(user_add==4):
    c=a*b
    print("The multiplication is: ",c)
else:
    print("incorrect")