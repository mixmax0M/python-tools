import random

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzöäüß1234567890!"§$%&/()=?-.,;_:@#<>^°²³{[]}\\'

numbers = int(input('How many passwords would you like to generate?\n'))
length = int(input('Password strenght? Type Numbers \n'))

for n in range(numbers):
    passw = ''
    for l in range(length * 2):
        passw += random.choice(chars)
    print(passw)
