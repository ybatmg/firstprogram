try:
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
    def add():
    
        return a+b

    def sub():
        return a-b

    def multi():
        return a*b

    def div():
        try:
            return a/b
        except ZeroDivisionError :
            print("Can't divide by zero.")   
        
    # finally:
    #     print("Calculation is done.")
 
    addition=add()
    subtraction=sub()
    multiplication=multi()
    division=div()
    print(f"The sum is {addition}\nThe subtraction is {subtraction}\nThe multiplication is {multiplication}\nThe divison is {division}")

except:
     print("value error")
    




























































































































































