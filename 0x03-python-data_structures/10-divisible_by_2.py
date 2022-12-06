#!/usr/bin/pyhton3
def divisible-by_2(my_list=[]):
    new_list = []
    if len(my_list) < 1:
        return None
    else:
        for i in my_list:
            new_list = new_list.append(if(i % 2 == 2))
        return new_list
