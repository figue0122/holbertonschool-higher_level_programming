#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
beg_string = f"Last digit of {number}"
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10
if last_digit > 5:
    