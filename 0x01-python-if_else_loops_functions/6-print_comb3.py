#!/usr/bin/python3
for num in range(0, 10):
    for j in range((num + 1), 10):
        if (num is not 8) or (j is not 9):
            print("{}{}, ".format(num, j), end='')
        else:
            print("{}{}".format(num, j))
