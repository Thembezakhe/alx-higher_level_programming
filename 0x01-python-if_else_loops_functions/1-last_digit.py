#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = (str(number))
last_digit = digit[-1]
condition = int(last_digit)
if condition > 5:
    print(f"Last digit of {number:d} is {last_digit} and is greater than 5")
elif condition == 0:
    print(f"Last digit of {number:d} is {last_digit} and is 0")
else:
    print(f"Last digit of {number:d} is {last_digit} and is less than 6 and not 0")
