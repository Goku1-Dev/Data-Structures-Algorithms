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

# 11 : Find the largest of three numbers
def largest_of_three(arr):
    largest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    print(f"{largest} is the largest number")

arr = [1, 2, 3, 4, 5]
largest_of_three(arr)

# 12 : Implement a profit or loss calculator
def ProfitOrLoss(investment, earnings):
    investment = float(investment)
    earnings = float(earnings)

    if earnings > investment:
        print(f"You made a profit of {earnings - investment}")
    elif earnings < investment:
        print(f"You made a loss of {investment - earnings}")
    else:
        print(f"You made no profit or loss")

investment = 1000
earnings = 1200
ProfitOrLoss(investment, earnings)

# 13 : Write an electricity bill calculator with tiered pricing
def electricityBillCalculator(units):
    if units <= 100:
        print(f"Your electricity bill is {units * 0.5}")
    elif units <= 200:
        print(f"Your electricity bill is {100 * 0.5 + (units - 100) * 0.75}")
    else:
        print(f"Your electricity bill is {100 * 0.5 + 100 * 0.75 + (units - 200) * 1.2}")

units = 300
electricityBillCalculator(units)

# 14 : Determine the type of triangle (Equilateral, Isosceles, Scalene)
def typeOfTriangle(sideA,sideB,sideC):
    if sideA == sideB and sideB == sideC:
        print(f"{sideA},{sideB},{sideC} is an equilateral triangle")
    elif sideA == sideB or sideB == sideC or sideA == sideC:
        print(f"{sideA},{sideB},{sideC} is an isosceles triangle")
    else:
        print(f"{sideA},{sideB},{sideC} is a scalene triangle")

sideA = 3
sideB = 4
sideC = 5
typeOfTriangle(sideA,sideB,sideC)

# 15 : Map numbers 1-7 to corresponding days of the week
def dayOfTheWeek(day):
    if day == 1:
        print(f"Day {day} is Monday")
    elif day == 2:
        print(f"Day {day} is Tuesday")
    elif day == 3:
        print(f"Day {day} is Wednesday")
    elif day == 4:
        print(f"Day {day} is Thursday")
    elif day == 5:
        print(f"Day {day} is Friday")
    elif day == 6:
        print(f"Day {day} is Saturday")
    elif day == 7:
        print(f"Day {day} is Sunday")
    else:
        print(f"Invalid day")

day = 1
dayOfTheWeek(day)