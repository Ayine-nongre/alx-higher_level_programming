#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def check(x):
        if x == search:
            return replace
        else:
            return x

    new_list = list(map(check, my_list))
    return new_list
