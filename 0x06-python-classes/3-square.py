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
        initialises the size of a square

        Args:
        param1: size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        returns the area of a square

        Returns:
        the return value, square of the area
        """

        return (self.__size ** 2)
