import json
import os
from datetime import datetime
from cake_model import MyCake

cakes=[]
parsedData=[]
cakefile='cakefile.json'


# def read_data():
#         if not os.path.exists(cakefile):
#             return []
#         with open(cakefile, "r") as file:
#             return json.load(file)

def write_data():
        # previousdata=read_data()
        # parsedData.extend(previousdata)
        with open(cakefile, "w") as file:
            for cake in cakes:
                parsedData.append(MyCake.toJson(cake=cake))

            json.dump(parsedData, file, intend=4)

# def write_data(cakes):
#     with open(data_file, 'w') as file:
#         for cake in cakes:


#             parsedData.append(Cake.toJson(cake=cake))
#         json.dump(parsedData, file, indent=4)

def add_order():
        user_id=input("Enter order id: ")
        user_n=input("Enter cake name: ")
        user_s=input("Enter shape: ")
        user_size=input("Enter size in pounds: ")
        cakes.append(MyCake(order_id=user_id,cake_name=user_n,cake_shape=user_s,cake_size=user_size))

        write_data()


def view_order():

        pass

def main():
        while True:
            print("Welcome to Our Kabhre Bakery!!")
            user_c=input("1.Add order\t2.View Order\t3.Exit : ")
            if(user_c=='1'):
                add_order()
            elif(user_c=='2'):
                view_order()
            elif(user_c=='3'):
                break
            else:
                print("Enter correct number: ")
        
    
main()