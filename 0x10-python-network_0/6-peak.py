#!/usr/bin/python3
"""
Function finf=ds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Define function fidd_peak
        Atrribiutes:
                list_of_integers
    """
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return max(list_of_integers)
    lft, right = 0, len(list_of_integers) - 1
    while lft < right:
        mid = (lft + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            lft = mid + 1
        else:
            right = mid

    return list_of_integers[lft]
