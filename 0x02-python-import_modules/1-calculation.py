#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, summ = add(a, b)))
    print("{} + {} = {}".format(a, b,diff = sub(a, b)))
    print("{} + {} = {}".format(a, b,product = mul(a, b)))
    print("{} + {} = {}".format(a, b,div = div(a, b)))
