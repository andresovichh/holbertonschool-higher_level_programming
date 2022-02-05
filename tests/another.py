def str_to_search():
    str_to_search = input("Type what you want to search for: ")
    str_to_search_in = input("Type where you want to search in: ")

    return ''.join(sorted(set(str_to_search).intersection(set(str_to_search_in))))
