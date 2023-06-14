#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for a in my_list:
        if a == search:
            a = replace
        new_list.append(a)
    return new_list
