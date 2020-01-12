# a program that calculates when the user will be 50 years old
#

name = input("What is your name?: ")
age = int(input("How old are you?: "))
currentYear = int(input("What year is it?: "))
year = str((currentYear - age) + 50)

print(name + " will be 50 years old in the year of " + year)
