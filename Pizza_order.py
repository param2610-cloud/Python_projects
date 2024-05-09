print("........Welcome to the pizza hut.........")
print("We have 3 size.\n 1) small \n 2) medium \n 3) large. \nwhat you want to take?")
size=int (input())
if size==1:
    print("You choose small size. \n are  you want to take pepperoni?(if yes type \'y\')")
    pep=input()
    if pep=='y':
        b=130
        print("with pepperoni the total amount will be 130")
    else:
       b=100
       print("Your total amount is: 100")
if size==2:
    print("You choose medium size. \n are  you want to take pepperoni?(if yes type \'y\')")
    pep=input()
    if pep=='y':
        b=250
        print("with pepperoni the total amount will be 250")
    else:
       b=200
       print("Your total amount is: 200")
       
if size==3:
    print("You choose large size. \n are  you want to take pepperoni?(if yes type \'y\')")
    pep=input()
    if pep=='y':
        b=350
        print("with pepperoni the total amount will be 350")
    else:
       b=300
       print("Your total amount is: 300")
print("if you like to take extra cheese for only 20 ruppes. press A")
a=input()
if(a=='A'):
    print("The total amount is",b+20)
else:
    print("then your amount is",b)