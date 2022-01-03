#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        a_tuple = 0, None
        return a_tuple  
    else:
        a_tuple = len(sentence), sentence[0]
        return a_tuple
