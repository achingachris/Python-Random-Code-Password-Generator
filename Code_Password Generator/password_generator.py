# import the random module 
import random

# characters that would be used to create the passwords
char = 'zcbnadgjlwryipXVBMKHFSQETUIO1230987645)(*&^%$#@)'

# ask for password length and number of passwords as integers
length = int(input('Enter prefered password length: '))
passwords = int(input('How many passwords? '))

for password in range(passwords):
# a variable where the password will be stored
    password = ' '  #empty variable to add a character at a time

    for entry in range(length):
        password += random.choice(char)

    print(password)
