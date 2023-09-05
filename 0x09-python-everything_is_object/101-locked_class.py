#!/usr/bin/python3
"""
dynamically creates a class that allows only first_name variable to be created
"""


class LockedClass:
    """
    dynamically creates a class that allows only first_name
    variable to be created
    """

    __slots__ = ['first_name']

    def __init__(self):
        """
        passes
        """

        pass
