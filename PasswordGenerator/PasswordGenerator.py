
import random
import pyperclip

symbol = 0 # 33 to 47, 91 to 96, 123 to 126
lower = 0  # 97 to 122
upper = 0  # 65 to 91
number = 0 # 48 to 57
count = 0  
password = []

length = input("How many characters do you want in your password? (default 128)\n")
length = 128 if length is '' else int(length)

#randomly select ascii character classes and individual characters

while count < length:
    rand = random.randint (0,3)
    if rand == 0:
        lower += 1
        b = int(random.randint (97,122))
        password.append(b)
    elif rand == 1:
        upper += 1
        b = random.randint (65,91)
        password.append(b)
    elif rand == 2:
        number += 1
        b = random.randint (48,57)
        password.append(b)
    elif rand == 3:
        r = random.randint(0,2)
        symbol += 1
        if r == 0:
            b = random.randint (33,47)
            password.append(b)
        elif r == 1:
            b = random.randint (91,96)
            password.append(b)
        elif r == 2:
            b = random.randint (123,126)
            password.append(b)
    count += 1

#convert ascii code to characters
word = "".join([chr(c) for c in password])

#copy pass to clipboard
pyperclip.copy(word)

#print the result
print ("Random password of length %s is: \n" % length)

print('******')
print(word)
print('******')

print ("\nIt contains",lower,"lowercase,",upper,"uppercase,",number,"numbers and",symbol,"symbol characters")
input('Password copied to clipboard, push a button to exit...')


