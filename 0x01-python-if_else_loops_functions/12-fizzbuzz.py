#!/usr/bin/python3
def fizzbuzz():
    for num in range (1, 100):
        print("{} ".format(num))
        if (num % 3 == 0):
            num  = "Fizz"
            print("{}".format(num))
        if (num % 5 == 0):
            num  = "Buzz"
            print("{}".format(num))
