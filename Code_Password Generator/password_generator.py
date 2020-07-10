# import the random module
import random

# characters that would be used to create the passwords

char = "zcbnadgjlwryipXVBMKHFSQETUIO1230987645)(*&^%$#@)"

# ask for password length
length = input("Enter prefered password length: ")
length = int(length)  # convert input to integer

number = input("How many passwords? ")
number = int(number)

for p in range(number):
    # a variable where the password will be stored
    password = " "  # empty variable to add a character at a time
    for c in range(length):
        password += random.choice(char)

    print(password)
