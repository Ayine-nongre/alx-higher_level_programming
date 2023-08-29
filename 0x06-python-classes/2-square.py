#!/usr/bin/python3
"""
class Square defines a square
"""


class Square:
    """
    class Square defines a square
    """

    def __init__(self, size=0):
        """
        Initializes size of square

        Args:
        param1: size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
