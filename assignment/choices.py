import random

choices=["rock","paper","scissors"]
b=0
c=0
for i in choices:
    comp_choice=random.choice(choices)
    user_input=input("Choose rock, paper, scissors: ")
    if(user_input==comp_choice):
        b=b+1
        print("Computer choose: ",comp_choice)
    else:
        c=c+1
        print("Computer choose: ",comp_choice)
print("In the best of three match: \n")
if(b>c):    
    print("You Win!!")
else:
    print("You Lose!!")