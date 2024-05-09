# import random


# print("............ICC............")
# print("Ind VS Aus")
# print("Rohit Sharma will t oss the coin. ")
# print("now that's time to call------")
# print("if head type H /// if tail type T")
# c=input()
# e=random.randint(0,1)
# if e==1:
#     a='H'
#     print("it's head and")
#     if(a==c):
#         print("Aus win the toss.")
#     else:
#         ("India win the toss.")
# if e==0:
#     a='T'
#     print("it's tail and")
#     if(a==c):
#         print("Aus win the toss.")
#     else:
#         print("India win the toss.")
import random 
print("Everybody's name seperated by comma:")
names=input()
names_list=names.split(",")
t=len(names_list)
o=random.randint(0,t)
print(names_list[o-1],"will pay the bill.")