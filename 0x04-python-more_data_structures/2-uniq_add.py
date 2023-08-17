#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    unique.append(my_list[0])

    for i in my_list:
        if i not in unique:
            unique.append(i)

    sum = 0
    for j in unique:
        sum = sum + j
    return sum
