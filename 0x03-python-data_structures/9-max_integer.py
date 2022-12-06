#!/usr/bin/pyhton3
def max_integer(my_list = []):
    if len(my_list) < 1:
        return None
    else:
        for i in my_list:
            if i > i+1:
               max = i
               return i
