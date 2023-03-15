#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replaced_list = []
    for item in my_list:
        if item == search:
            item = replace
            replaced_list += [item]
        else:
            replaced_list += [item]
    return replaced_list
