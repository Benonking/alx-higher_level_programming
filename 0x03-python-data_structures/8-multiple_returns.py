#!/usr/bin/python3
def multiple_returns(sentence):
    Length = len(sentence)
    First_char = sentence[0] if Length > 0 else None
    return (Length, First_char)
