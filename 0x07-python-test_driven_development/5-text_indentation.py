#!/usr/bin/python3

"""
text text_indentation
"""
def text_indentation(text):
    """
    text indentation
    args:
    text (str): a strig
    """
    
    if not(isinstance(text, str)):
        raise TypeError("text must be a string")
    for delim in ".:?":
        text = (delim + "\n\n").join\
            ([line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
