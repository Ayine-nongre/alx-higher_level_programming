#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        unique = set(my_list)

        summ = 0
        for j in unique:
            summ = summ + j
        return summ
