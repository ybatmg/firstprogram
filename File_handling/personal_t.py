# Personal Information Logger: Create a script that asks for the user's name, age, and favorite color, 
# then prints a personalized message based on the input.

print("\\\\\\\\\\\\-----Personal Information Logger-----////////////")

def main():
    user_name=input("Enter your name:")
    user_age=input("Enter your age: ")
    user_col=input("Enter your favourite color: ")
    user_input=input("Enter 1.Name\t2.Age\t3.Favourite Color\n4.Exit")
    if(user_input=='1'):
        print(user_name)
    elif(user_input=='2'):
        print(user_age)
    elif(user_input=='3'):
        print(user_col)
    elif(user_input==4):
        return
    else:
        print("Entered number is incorrect!!")
    
main()