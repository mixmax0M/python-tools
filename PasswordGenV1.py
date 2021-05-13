import random

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzöäüß1234567890!"§$%&/()=?-.,;_:@#<>^°²³{[]}\\'

numbers = input('How many passwords would you like to generate?\n')
numbers = int(numbers)

length = input('Password strenght? Type Numbers \n')
length = int(length)

for n in range(numbers):
    passw = ''
    for l in range(length * 2):
        passw += random.choice(chars)
    print(passw)