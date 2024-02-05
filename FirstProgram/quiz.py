print("Welcome to Kabhre Quiz Contest")
quest={
        
    1: ["Which is JavaScript framework?\n 1.Nodejs 2.SpringBoot 3.Django 4.Swift","1"],
    2: ["Where is Mahatma Gandhi?\n 1.America 2.Africa 3.India 4.China","3"],
    3: ["What is full form of UPS?\n 1.Union Power Supply 2.Universal Power Supply 3.Unterruptile Power Supply 4.United Power Supply","3"],
    4: ["Who is first lady programmer?\n 1.Pasang Lhamu Sherpa 2. Guras Nani 3.Lady Aavasta Ada Love Lace 4.Lady Agusta Ada Love Lace","4"],
    5: ["Who is father of Computer Science?\n 1.Charles Darwin 2.Boston Brothers 3.Ravi Teja 4.Charles Babbage","4"]
    }
d=0
e=0
for i in quest:
    a=quest[i][0]
    print(a)
    b=quest[i][1]
    user_input=input("\t")
    if(user_input==b):
        d=d+1
    else:
        e=e+1
print("Total: ",d)
print("Incorrect: ",e)

