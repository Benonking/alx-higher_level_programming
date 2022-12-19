#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        return fct(*args)
    except (ValueError, ZeroDivisionError, IndexError, TypeError) as i:
        stderr.write("Exception: {}".format(i))
        return None

