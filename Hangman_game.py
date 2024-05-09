import random
def hangman():
    image= [ " +--------+\n |        |\n          |\n          |\n          |\n          |\n          |\n==========|"," +--------+\n |        |\n o        |\n          |\n          |\n          |\n          |\n==========|"," +--------+\n |        |\n o        |\n/         |\n          |\n          |\n          |\n==========|"," +--------+\n |        |\n o        |\n/|        |\n          |\n          |\n          |\n==========|"," +--------+\n |        |\n o        |\n/|\\       |\n          |\n          |\n          |\n==========|"," +--------+\n |        |\n o        |\n/|\\       |\n |        |\n/ \\       |\n          |\n==========|"," +--------+\n |        |\n o        |\n/|\\       |\n |        |\n/ \\       |\n          |\n==========|"]
    wordstock=("banana","apple","mango","orange")
    print("Hint: this is a fruit")
    word=random.choice(wordstock)
    lives=6
    result='_'*len(word)
    g=0
    while lives>=0:
        
        guessed_word=input("Enter letter:")
        if guessed_word in word:
            
            print("you gor right")
            print("live=",lives)
            result_list=list(result)
            for i in range(len(word)):
                if word[i]==guessed_word:
                     result_list[i] = guessed_word
                result = ''.join(result_list)
            print(result)
            print(image[g])
            
            

        else:
            g+=1
            print("Nah, you got wrong.")
            lives-=1
            print(lives,"left.")
            print(image[g])
        if g==5:
            print("The man gotta hang and died, GAME OVER")
            break

    if '_' not in result:
        print("you guessed the word coorectly.")
    if(lives==0):
        print("you lost all your lives. Better luck next time.")
    
        
        

print("let's play the hangman.")
hangman()











# image=" +--------+\n ","|","        |\n ","o","        |\n","/","|","\\","         |\n ","|","        |\n","/"," \\","         |\n          |\n==========|"
# print(image[0],image[1],image[2],image[4],image[8],image[10],image[13])
# # 8 10 12 14