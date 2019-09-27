# import random
import random

name = input('Enter your name: ')
char = 'ABCDEfghijkLMNOPQ123456789'

code = ' '
for c in range(5):
    code += random.choice(char)
print('Hello ' +name.upper() + ' Your ID number is ' + code)