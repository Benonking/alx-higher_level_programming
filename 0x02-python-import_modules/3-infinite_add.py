#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    args = len(sys.argv)
    if (args > 1):
        for i in range (1, arguments):
            result += int(sys.argv[i])
    print("{:d}".format(result))
