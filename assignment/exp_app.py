import json
import os

expfile='exp.json'

def read_dataa():
    if not os.path.exists(expfile):
        return []
    with open(expfile,"r") as file:
        return json.load(file)

def write_data():
    

def add_exp():


def view_exp():

def view_totalexp():

def main():
    while True:
        print("----------Expense Tracker Application----------")
        user_input=input(print("***Main Menu***\n1.Add Expense\n2.View Expenses by Category\n3.View Total Expenses\n4.Exit"))
        if(user_input=='1')
            add_exp()
        elif(user_input=='2')
            view_exp()
        elif(user_input=='3')
            view_totalexp()
        elif(user_input=='4')
            break
        else:
            print("Enter correct option!!")
        