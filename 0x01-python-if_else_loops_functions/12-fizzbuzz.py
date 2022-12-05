#!/usr/bin/python3
def fizzbuzz():
    for num in range (1, 101):
        print("{} ".format(num))
        if (num % 3 == 0):
            print("Fizz")
        if (num % 5 == 0):
            print("Buzz")
