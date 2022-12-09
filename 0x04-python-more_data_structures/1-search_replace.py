#!/usr/bin/pythom3
'''
my_list: is the initial list
search : is the element to replace in the list
replace : is the new element
'''


def search_replace(my_list, search, replace):
    if my_list is not None:
        return ([i if i != search else replace for i in my_list])
