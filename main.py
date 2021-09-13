import random
letter=['a'',b','c','d','e','f','g','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number=['1','2','3','4','5','6','7','8','9','0']
symbol=['!','@',',','$','%','^','&','*','+','-']
print("Welcome to password generator.")
a=int(input("How many letters would you like in your password?\n "))
b=int(input("How many symbols would you like in your password?\n"))
c=int(input("How many numbers would you like in your password?\n"))

# EASY LEVEL (NON-SUFFLED PASSWORD)
# password=""
# for char in range(1,a+1):
#     choice=random.choice(letter)
#     password+=choice
#
# for char in range(1,b+1):
#     choice=random.choice(symbol)
#     password+=choice
#
# for char in range(1,c+1):
#     choice=random.choice(number)
#     password+=choice

# print(password)



# HARD LEVEL (SUFFLED PASSWORD)


password_list=[]
for char in range(1,a+1):
    choice=random.choice(letter)
    password_list+=choice

for char in range(1,b+1):
    choice=random.choice(symbol)
    password_list+=choice

for char in range(1,c+1):
    choice=random.choice(number)
    password_list+=choice
random.shuffle(password_list)
# print(password_list

password=""
for i in password_list:
    password+=i
print(f"Your password is {password}.")