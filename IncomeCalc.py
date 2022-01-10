import math


def WeeklyIncome(hourinc, hours, days):
    dayinc = hourinc * hours
    return days * dayinc


def YearlyIncome(hourinc, hours, days, holidays):
    week = WeeklyIncome(hourinc, hours, days)
    year = week * 360

    dayinc = hourinc * hours
    hol = dayinc * holidays

    return year - hol


hourinc = int(input("Please enter your income/h: "))
hours = int(input("Please enter how many h you work a day: "))
days = int(input("Please enter how many d you work a week: "))
holidays = int(input("Please enter how many holidays you have: "))

print(f"\n You make {WeeklyIncome(hourinc, hours, days)} a week (tax free).")
print(f"\n You make {YearlyIncome(hourinc, hours, days, holidays)} a year (tax free).")
