user_input=int(input("Enter how many task you want to do? "))
list_n=[]
for i in range(user_input):
    u_i=input("Enter task: ")
    list_n.append(u_i)

print(list_n)
u_d=input("Do you want to add/remove? (add/remove)")
add=str("add")
remove=str("remove")
for i in range(user_input):
    if(u_d==add):
        r=input("Enter new task: ")
        list_n.append(r)
        break

if(u_d==remove):
        r=input("Enter which task?")
        list_n.remove(r)
   
print(list_n)