#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    all_values = max(a_dictionary, key=lambda x: a_dictionary[x])
    return all_values
