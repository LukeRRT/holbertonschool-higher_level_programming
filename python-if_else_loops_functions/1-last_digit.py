#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} ", end="")
if number > 5:
    print("and is greater then 5")
elif number == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
