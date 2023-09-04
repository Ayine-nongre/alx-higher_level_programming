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

        Args:
        param1: width value
        param2: height value
        """
        self.width = width
        self.height = height

    def area(self):
        """
        returns area of rectangle
        """

        return (self.__width * self.__height)

    def perimeter(self):
        """
        returns perimeter of rectangle
        """

        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """
        returns a string
        """

        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return (rectangle)
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                rectangle += "#"
            rectangle += "\n"
        return rectangle
