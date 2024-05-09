import random
print("..........Rock, Paper, Scissor game..........")
print("if you want to play with computer press 1 \n if you have game partner press 2")
mode=input()
result=['Rock','Paper','scissor']
if (mode=='1'):
    p1=0
    p2=0
    print("Here is the rules of games:\nRock = 1\nPaper=2\nScissor=3")
    for i in range(1,5):
        v=int(input("Your turn:"))
        print("You give ",result[v-1])
        i=random.randint(1,3)
        print("computer give ",result[i-1])
        if v==i:
           print("Equal point.")
           print("Your point=",p1+1,"Computer point",p2+1)
           p1+=1
           p2+=1
        elif (v==1 and i==2) or (i==1 and v==3) or (i==3 and v==2):
            print("computer win")
            print("your score",p1,"computer score",p2+1)
            p2+=1
        else:
            print("you win.")
            print("your score",p1+1,"computer score",p2)
            p1+=1
    if(p1>p2):
        print( "The Final result:\n You win",)
    else:
        print("The Final result:\n Computer win")

if (mode=='2'):
    p1=0
    p2=0
    print("Here is the rules of games:\nRock = 1\nPaper=2\nScissor=3")
    for i in range(1,6):
        v=int(input("Player 1 turn:"))
        x=int(input("Player 2 turn:"))
        print("P1 give ",result[v-1])
        print("P2 give ",result[x-1])
        if v==x:
           print("Equal point.")
           print("P1 point=",p1+1,"P2 point",p2+1)
           p1+=1
           p2+=1
        elif (v==1 and x==2) or (i==1 and x==3) or (i==3 and x==2):
            print("p2 win")
            print("P1 score",p1,"P2 score",p2+1)
            p2+=1
        else:
            print("P1 win.")
            print("P1 score",p1+1,"P2 score",p2)
            p1+=1
    if(p1>p2):
        print( "The Final result:\n P1 win",)
    else:
        print("The Final result:\n P2 win")

