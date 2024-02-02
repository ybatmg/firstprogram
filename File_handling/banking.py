print("Welcome to Kabhre Central Bank!!\n")

dictt={
    "Rahul Zain":{"address":"Banepa","balance":250000,"history":[]},
    "Laxman Padey":{"address":"Khopase","balance":300000,"history":[]},
    "Pemba Tmg":{"address":"Dhulikhel","balance":275000,"history":[]},
    "Nishan Prasai":{"address":"Sankhu","balance":400000,"history":[]}
}
def login(name):
        user_input=input("Enter your name: ")

        if(user_input in dictt):
            print(user_input)

        else:
            print("User not found!!") 

        # userExist=False
        # for i in dictt:
        #         a=dictt[i]['name']
        #         if(user_input==a):
        #             userExist=True
        
                    
        
        # if(userExist==True):
        #                 for i in dictt:
        #                     a=dictt[i]['name']

        #                     if(user_input==a):
        #                         print("Successfully logged in!")
        #                         print(dictt[i])
        #                         break
        # else:
        #     print("User not found!!")

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