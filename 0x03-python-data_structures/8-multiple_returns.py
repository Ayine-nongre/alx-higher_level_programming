#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return
    tuple_data = (len(sentence), sentence[0])
    return tuple_data
