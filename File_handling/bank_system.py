import json
import os

data_file='ddwt.json'

def read_data():
    if not os.path.exists(data_file):
        return {}
    with open(data_file, "r") as file:
        return json.load(file)

def write_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

def create_acc():
    users=read_data()
    user_name=input("Enter your name: ")
    user_password=input("Enter your password: ")

    users[user_name]={"password":user_password,"balance":0}
    write_data(users)
    print("Account created Successfully!!")
    

def login():
    users=read_data()
    user_name=input("Enter your user name: ")
    password=input("Enter your password: ")

    if(user_name in users and password==users[user_name]['password']):
        return user_name
    else:
        print("(Invalid username or password!!)\n")
        main()
    
def deposit(user):
    users=read_data()
    amount=float(input("Enter amount you want to deposit: "))

    users[user]['balance']+=amount
    write_data(users)
    print(f"Deposited Amount: {amount}, New Balance: {users[user]['balance']}")

def withdraw(user):
    users=read_data()
    amount=float(input("Enter amount you want to withdraw: "))

    if(amount<=users[user]['balance']):
        users[user]['balance']-=amount
        write_data(users)
    else:
        print("Insufficent balance.")

def viewaccount(user):
    users=read_data()
    amount=users[user]['balance']
    print(f"User Name: {user}\nBalance: {amount}")
    user_edit=input("1.Edit profile\t2.Exit")
    if(user_edit=='1'):
        user_n=input("Enter new username: ")
        users[user_n]=users.pop(user)
        print("Successfully updated.")
        write_data(users)
        return 'success'
    elif(user_edit=='2'):
        return
    else:
        print("Cannot Update!!")


def main():
    while True:
        print("Welcome To Central Bank Of Kabhre !!\n")
        print("1.Create Account\n2.Login\n3.Exit\t")
        user_in=input()
        if(user_in=='1'):
            create_acc()
        elif(user_in=='2'):
            user=login()
            if user:
                while True:
                    print("*\-----------Account Name---------/*")
                    print("1.Deposit\t2.Withdraw\t3.View Account\t4.Logout")
                    user_choice=input("Enter your Choice: ")
                    if(user_choice=='1'):
                        deposit(user)
                    elif(user_choice=='2'):
                        withdraw(user)
                    elif(user_choice=='3'):
                        response=viewaccount(user)
                        if(response=='success'):
                            break
                    elif(user_choice=='4'):
                        break
                    else:
                        print("Enter correct number.")

        elif(user_in=='3'):
            break
        else:
            print("Enter correct number")
        

main()