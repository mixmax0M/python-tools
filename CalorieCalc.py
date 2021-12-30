from time import sleep

def main():
    print('========================')
    print('Calorie Calculator\n')
    print('Gender')
    print('[1] Male')
    print('[2] Female\n')
    gender = int(input('Selection: '))
    age = float(input('Enter your age: '))
    weight = float(input('Enter your weight in kg: '))
    height = float(input('Enter your height in cm: '))

    cal = 0

    if gender == 1:
        cal = 66.47 + (13.7*weight) + (5.0*height) - (6.8*age)
    elif gender == 2:
        cal = 655.1 + (9.6*weight) + (1.8*height) - (4.7*age)
    else:
        print('Invalid Input\n')
        main()

    print('========================')
    print('Activity')
    print('[1] None')
    print('[2] Little to None')
    print('[3] Light exercise (1 - 3 Days/Week)')
    print('[4] Moderate exercise (3 - 5 Days/Week)')
    print('[5] Intensive exercise (6 - 7 Days/Week)')
    print('[6] Daily intensive exercise (Everyday)\n')

    activitys = int(input('Selection: '))

    match (activitys):
        case 1:
            cal = cal * 1
        case 2:
            cal = cal * 1.2
        case 3:
            cal = cal * 1.375
        case 4:
            cal = cal * 1.55
        case 5:
            cal = cal * 1.725
        case 6:
            cal = cal * 1.9
        case _:
            cal = cal * 1
            print('Invalid Selection')

    print('========================')
    print(f'Your basal metabolic rate is {cal}')
