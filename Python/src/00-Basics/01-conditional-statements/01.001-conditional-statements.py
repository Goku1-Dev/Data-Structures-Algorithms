# NOTE: Basic Level if, else, and elif statements :

# 01 : Write a program to check if a number is even or odd 
def is_even(A):
    if A % 2 == 0:
        print(f"{A} is even")
    else:
        print(f"{A} is odd")

A = 8
is_even(A)

# 02 : Write a program to check if a number is positive, negative, or zero
def is_number(X):
    if X > 0:
        print(f"{X} is positive")
    elif X == 0:
        print(f"{X} is zero")
    else:
        print(f"{X} is negative")

X = 5
is_number(X)

# 03 : Check if a person is eligible to vote (age >= 18)
def voting_eligibility(age):
    if age > 18:
        print(f"{age} is eligible to vote")
    elif age == 18:
        print(f"{age} is eligible to vote")
    else:
        print(f"{age} is not eligible to vote")

age = 17
voting_eligibility(age)

# 04 : Find the greater or lesser numbers
def greater_or_lesser(number1, number2):
    if number1 > number2:
        print(f"{number1} is greater than {number2}")
    elif number1 < number2:
        print(f"{number1} is less than {number2}")
    else:
        print(f"{number1} is equal to {number2}")

number1 = 5
number2 = 10
greater_or_lesser(number1, number2)

# 05 : Check if a number is divisible by both 5 and 11
def divisible_by_both(num):
    divisible_eleven = num % 11 == 0
    divisible_five = num % 5 == 0

    if divisible_eleven:
        print(f"{num} is divisible by 11")
    elif divisible_five:
        print(f"{num} is divisible by 5")
    else:
        print(f"{num} is not divisible by both 5 and 11")

num = 55
divisible_by_both(num)

# 06 : Implement a leap year checker
def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year")
            else:
                print(f"{year} is not a leap year")
        else:
            print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

year = 2000
leap_year(year)

# 07 : Create a grade calculator (A, B, C, D, F based on marks)
def grade_calculator(marks):
    if marks > 90:
        print(f"{marks} is grade by A")
    elif marks > 80:
        print(f"{marks} is grade by B")
    elif marks > 70:
        print(f"{marks} is grade by C")
    elif marks > 60:
        print(f"{marks} is grade by D")
    else:
        print(f"{marks} is grade by F")

marks = 80
grade_calculator(marks)

# 08 : Check if three given sides form a valid triangle
def valid_triangle(side1,side2,side3):
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        print(f"{side1},{side2},{side3} is a valid triangle")
    else:
        print(f"{side1},{side2},{side3} is not a valid triangle")

side1 = 3
side2 = 4
side3 = 5
valid_triangle(side1,side2,side3)

# 09 : Identify if a character is a vowel, consonant, digit, or special character
def charter_type(character):
    if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
        print(f"{character} is a vowel")
    elif character.isalpha():
        print(f"{character} is a consonant")
    elif character.isdigit():
        print(f"{character} is a digit")
    else:
        print(f"{character} is a special character")

character = 'a'
charter_type(character)

# 10 : Build a simple calculator (+, -, *, /)
def calculator(num1,num2,num3):
    if num3 == '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif num3 == '-':
        print(f"{num1} -{num2} = {num1 - num2}")
    elif num3 == '*':
        print(f"{num1} * {num2} = {num1 * num2}")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")

num1 = 5
num2 = 10
num3 = '+'
calculator(num1,num2,num3)