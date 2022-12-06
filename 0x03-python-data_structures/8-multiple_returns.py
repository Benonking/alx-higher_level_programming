#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) <= 0:
        return None
    else:
        Length, char = len(sentence), sentence[0]
    return (Length, char)
