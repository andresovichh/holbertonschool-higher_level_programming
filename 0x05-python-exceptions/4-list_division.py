#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for x in range (list_length):
        length = 0
        try:
            length = my_list_1(x) / my_list_2(x)
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            "division by 0"
        except IndexError:
            print("out of range")
        finally:
            new_list.append(length)
    return(new_list)