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