#!/usr/bin/python3

"""

"""
def text_indentation(text):
    """
    """
    
    if not(isinstance(text, str)):
        raise TypeError("text must be a string")
    
    # res = text.split()
    # dott = "."
    # for i in res:
    #     if x in range(len(i)) == ".":
    #         print("\n")
    for delim in ".:?":
        text = (delim +"\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
