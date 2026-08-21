import random
import string

alpha = string.ascii_letters
numbers = string.digits
password =''
all_charc = alpha + numbers
for i in range(12):
    random_choice = random.choice(all_charc)
    password = password + random_choice
print('Your password is',password)



