import random

random_n=random.randint(1,10)
while(True):
    user_input=int(input("Guess a number from 1 to 10: "))
    if(user_input<=10):
        if(user_input==random_n):
            print("Your guess is correct")
            break
        elif(user_input>=random_n):
            print("Your number is greater \n")
        else:
            print("Your number is smaller\n")
        print("Random num is: ",random_n) 
    else:
     print("Your number is exceeded")