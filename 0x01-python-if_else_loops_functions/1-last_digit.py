#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    last_digit = number % 10
    if last_digit > 5:
        str = 'greater than 5'
    elif last_digit < 6 and last_digit != 0:
        str = 'less than 6 and not 0'
    elif last_digit == 0:
        str = '0'
elif number < 0:
    last_digit = ((number * -1) % 10) * -1
    if last_digit == 0:
        str = '0'
    else:
        str = 'less than 6 and not 0'

print(f"Last digit of {number:d} is {last_digit:d} and is {str:s}")
