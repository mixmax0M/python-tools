from os import system
from time import sleep

print('========================')
print('Calorie Calculator\n')
print('Gender')
print('[1] Male')
print('[2] Female')
gender = int(input('\nSelection: '))
print('========================')

print('System')
print('[1] Metric')
print('[2] Imperial')
syst = int(input('\nSelection: '))
print('========================')
age = float(input('\nEnter your age: '))
print('========================')

if syst == 1:
    weight = float(input('Enter your weight: '))
    height = float(input('Enter your height: '))
    
elif syst == 2:
    lbs = float(input('Enter your weight: '))
    ft = float(input('Enter your height (ft): '))
    inc = float(input('Enter your height (in): '))
    
    weight = lbs / 2.205 
    height = ft * 30.48 + inc + 2.54
else:
    print("Invalid Input. Closing in 3 seconds")
    sleep(3)
    exit

def main(gender, weight, height, age):
    if gender == 1:
        cal = 66.47 + (13.7*weight) + (5.0*height) - (6.8*age)
    elif gender == 2:
        cal = 655.1 + (9.6*weight) + (1.8*height) - (4.7*age)

    print('========================')
    print('Activity')
    print('[1] None')
    print('[2] Little to None')
    print('[3] Light exercise (1 - 3 Days/Week)')
    print('[4] Moderate exercise (3 - 5 Days/Week)')
    print('[5] Intensive exercise (6 - 7 Days/Week)')
    print('[6] Daily intensive exercise (Everyday)\n')

    activitys = int(input('Selection: '))

    if activitys == 1:
        cal = cal * 1
    elif activitys == 2:
        cal = cal * 1.2
    elif activitys == 3:
        cal = cal * 1.375
    elif activitys == 4:
        cal = cal * 1.55
    elif activitys == 5:
        cal = cal * 1.725
    elif activitys == 6:
        cal = cal * 1.9
    else:
        cal = cal * 1
        print('Invalid Selection.')

    print('========================')
    print(f'Your basal metabolic rate is {cal}')
    print('========================')
    input()

main(gender, weight, height, age)
