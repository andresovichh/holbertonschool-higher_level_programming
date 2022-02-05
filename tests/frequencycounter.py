def search_for_str():
    str_to_search = input("Type what you want to search for: ")
    where_to_search = input("Type where you want to search for: ")
    print("IM here")

    return ''.join((set(str_to_search).intersection(set(where_to_search))))
