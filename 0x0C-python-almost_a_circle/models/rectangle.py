#!/usr/bin/python3
from models.base import Base
"""
This is a class for a rectangle
"""


class Rectangle(Base):
    """This is a class for a rectangle"""

    @property
    def width(self):
        """Method for width getter param"""

        return self.__width

    @width.setter
    def width(self, value):
        """
        Method for width setter param
        
        Args:
        param: value of width
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Method for height getter param"""

        return self.__height

    @height.setter
    def height(self, value):
        """
        Method for height setter param
            
        Args:
        param: value of height
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Method for x getter param"""

        return self.__x

    @x.setter
    def x(self, value):
        """Method for x setter param"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Method for y getter param"""

        return self.__y

    @y.setter
    def y(self, value):
        """Method for y setter param"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __init__(self, width=0, height=0, x=0, y=0, id=None):
        """initialises all instances of variables"""

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def area(self):
        """Calculates area of rectangle"""

        return (self.width * self.height)

    def display(self):
        """Displays a rectangle using #"""

        rectangle = self.y * "\n"
        for i in range(0, self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"
        print(rectangle, end='')

    def __str__(self):
        """Overrides str method using customised method"""

        str_rec = "[Rectangle]"
        str_id = " ({:d})".format(self.id)
        str_xy = " {:d}/{:d}".format(self.x, self.y)
        str_wh = " {:d}/{:d}".format(self.width, self.height)

        return str_rec + str_id + str_xy + " -" + str_wh

    def update(self, *args, **kwargs):
        """Method to update field of instance"""

        if args is not None and len(args) != 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns a dictionary representation of rectangle"""

        list_att = ['id', 'width', 'height', 'x', 'y']
        dic = {}

        for key in list_att:
            dic[key] = getattr(self, key)

        return dic
