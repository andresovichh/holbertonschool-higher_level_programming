#!usr/bin/python3

"""

"""
def text_indentation(text):
    """
    """
    
    if not(isinstance(text, str)):
        raise TypeError("text must be a string")
    
    res = text.split()
    dott = "."
    for i in res:
        for x in i:
            if(x == "."):
                print("\n")
            else:
                print(i, end=" ")
