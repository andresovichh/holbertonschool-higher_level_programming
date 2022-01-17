#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
#!/usr/bin/python3
    def safe_print_list(my_list=[], x=0):
        i = 0
        try:
            for j in range (0, x):
                print("{}".format(my_list[j]), end="")
                i += 1
        except IndexError:
            return j
        else:
            return x
        finally:
            print ("")