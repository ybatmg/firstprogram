print("Welcome to Kabhre Central Bank!!\n")

dictt={
    1:{"name":"Rahul Zain","address":"Banepa","balance":250000,"history":[]},
    2:{"name":"Laxman Padey","address":"Khopase","balance":300000,"history":[]},
    3:{"name":"Pemba Tmg","address":"Dhulikhel","balance":275000,"history":[]},
    4:{"name":"Nishan Prasai","address":"Sankhu","balance":400000,"history":[]}
}
def login(name):
        user_input=input("Enter your name: ")
        userExist=False
        if(userExist==False):
            for i in dictt:
                a=dictt[i]['name']
                if(user_input!=a):
                    userExist=True
        
        if(userExist==True):
            for i in dictt:
                a=dictt[i]['name']
       
            if(user_input==a):
                print("Successfully logged in!")
                print(dictt[i])
        else:
             print("User not found!!")
# def deposit():
#     yes="Y"
#     no="N"
#     user_d=input("Want to deposi t?? (Y/N)")
#     if(user_d==yes):
#         user_a=int(input("Enter amount in Rs. "))
#         print("Total Balance: ",user_a)
#     elif(user_d==no):
#         pass

current_user=login('name')