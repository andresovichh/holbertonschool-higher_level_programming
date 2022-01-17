#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    length = 0
    for x in range (list_length):
        try:
            length = [my_list_1(x) / my_list_2(x)]
            x += 1
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            "division by 0"
        except IndexError:
            print("out of range")
        finally:
            return length
