#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
#!/usr/bin/python3
    def safe_print_list(my_list=[], x=0):
        i = 0
        try:
            for i in range (0 <= x):
                print("{}".format(my_list[i]), end="")
                i += 1
            return("nb_print:{}".format(i))
        except (x > i):
            return("larger than list")