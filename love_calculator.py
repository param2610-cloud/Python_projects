print(".......Love calculator.......")
partner1=input("Enter your partner name:")
partner2=input("Enter your name:")
b=0
d=0
check = "true love"
for j in check:
   for i in partner1:
      if i==j:
          b+=1
for j in check:
   for i in partner2:
      if i==j:
          d+=1
total= b*10+d
print("Your love percentage with your partner is ",total)