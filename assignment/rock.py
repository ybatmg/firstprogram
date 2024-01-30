import random

choices=["rock","paper","scissor"]
b=0
c=0
rock="rock"
paper="paper"
scissor="scissor"
comp_choice=random.choice(choices)
for i in choices:
    
    user_input=input("Choose rock, paper, scissor: ")
    if(user_input==rock and comp_choice==choices[2]):
                print("Computer choice: ",comp_choice)
                print("You Win!! ")
    elif(user_input==paper and comp_choice==choices[0]):
            print("Computer Choice: ",comp_choice)
            print("You Win!!")
    elif(user_input==scissor and comp_choice==choices[1]):
        print("Computer Choice: ",comp_choice)
        print("You Win!!")
    else:
           print("Computer choice: ",comp_choice)
           print("You Lose!!")
