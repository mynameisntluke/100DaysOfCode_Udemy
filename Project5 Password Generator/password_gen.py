import random

password = ""
password_list = []

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# DEBUG MODE
num_letters = 10
num_numbers = 2
num_symbols = 4

# USER VERSION
# input("Generate your password yo, press ENTER to begin")
# num_letters = int(input("How many letters should your password contain? "))
# num_numbers = int(input("How many numbers should your password contain? "))
# num_symbols = int(input("How many symbols should your password contain? "))

####### Easy Version #######
# for n in range(num_letters):
#     letter_index = random.randint(0, 25)
#     password_list.append(letters[letter_index])
#
# for m in range(num_numbers):
#     num_index = random.randint(0, len(numbers)-1)
#     password_list.append(numbers[num_index])
#
# for i in range(num_numbers):
#     sym_index = random.randint(0, len(symbols)-1)
#     password_list.append(symbols[sym_index])
#
####### Harder Version #######
## ie not all letters then all numbers....
for m in range(num_numbers):
    num_index = random.randint(0, len(numbers)-1)
    password_index = random.randint(0, len(password_list))
    password_list.insert(password_index, numbers[num_index])

for i in range(num_numbers):
    sym_index = random.randint(0, len(symbols)-1)
    password_index = random.randint(0, len(password_list))
    password_list.insert(password_index, symbols[sym_index])

for n in range(num_letters):
    letter_index = random.randint(0, 25)
    # Assumes password must start with a letter
    if n == 0:
        password_index = 0
    else:
        password_index = random.randint(0, len(password_list))
    # Random capital letters
    if random.randint(1, 3) % 2 == 1:
        password_list.insert(password_index, letters[letter_index].capitalize())
    else:
        password_list.insert(password_index, letters[letter_index])

if num_numbers == 42:
    password = "soLongAndThanksForAllTheFish"
elif num_numbers == 9000:
    password = "ITSOVER9000!!!!"
else:
    password = password.join(password_list)
print(password)
