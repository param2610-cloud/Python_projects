import random
def password_manager(length1,letter,digit,symbol):
        letter1= "abcdefghijklmnopqrstwxyzABCDEFGHIJKLMNOPQRSTWXYZ"
        digit1="1234567890"
        symbol1="!@#$%^&*()_+-="
        password1=''.join(random.sample(letter1,int(letter)))
        password2=''.join(random.sample(digit1,int(digit)))
        password3=''.join(random.sample(symbol1,int(symbol)))
        password=password1+password2+password3
        finalpassword=''.join(random.sample(password,int(length1)))
        
        return finalpassword
print("Type the Length of the password:")
len1=input()
print("what number of letter will be in password:")
let=input()
print("what number of digit will be in password:")
dig=input()
print("what number of symbol will be in password:")
sym=input()
print(password_manager(len1,let,dig,sym))
# import random

# def generate_password(length):
#     characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-"
#     password = ''.join(random.sample(characters,length))
#     return password

# # Example usage
# password_length = 10
# generated_password = generate_password(password_length)
# print(generated_password)
