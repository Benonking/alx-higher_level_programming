#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    last_Digit = number % (-10)
else:
    last_Digit = number % (10)
if (last_Digit > 5):
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, last_Digit))
elif (last_Digit == 0):
    print("Last digit of {:d} is {:d}".format(number, last_Digit))
elif(last_Digit < 6 and last_Digit != 0):
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, last_Digit))
