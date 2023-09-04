#!/usr/bin/python3
"""
Rectangle defines a rectangle object
"""


class Rectangle:
    """
    Rectangle defines a rectangle object
    """

    @property
    def width(self):
        """
        Returns the width of a rectangle
        """

        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Sets the width of a rectangle

        Args:
        param1: value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be a integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Returns the height of a rectangle
        """

        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Sets the height of a rectangle

        Args:
        param1: value of height
        """

        if not isinstance(value, int):
            raise TypeError("height must be a integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def __init__(self, width=0, height=0):
        """
        initialises values
        """
        self.width = width
        self.height = height
