#!/usr/bin/python3
from models.rectangle import Rectangle
"""
This is a class for a square instance
"""


class Square(Rectangle):
    """This is a class for a square instance"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialises square instance"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""

        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""

        self.width = value
        self.height = value

    def __str__(self):
        """Overrides str method"""

        str_sq = "[Square]"
        str_id = " ({:d})".format(self.id)
        str_xy = " {:d}/{:d} -".format(self.x, self.y)
        str_wh = " {:d}".format(self.width)

        return str_sq + str_id + str_xy + str_wh

    def update(self, *args, **kwargs):
        """Method to update params"""

        if args != None and len(args) != 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Method to change square representation to dictionary"""

        list_att = ['id', 'size', 'x', 'y']
        dic = {}

        for key in list_att:
            if key == 'size':
                dic[key] = getattr(self, 'width')
            else:
                dic[key] = getattr(self, key)

        return dic
