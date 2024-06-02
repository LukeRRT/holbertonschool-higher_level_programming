#!/usr/bin/python3
"""
a function to write class Student
"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance
        with the given attributes.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation
        of the Student instance.
        If attrs is a list of strings, only attributes
        names contained in this list will be retrieved.
        Otherwise, all attributes will be retrieved.
        """
        if attrs is None:
            return self.__dict__
        else:
            for key in attrs:
                if key in self.__dict__:
                    dict[key] = self.__dict__[key]
            return dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student
        instance based on the json dictionary.
        A dictionary key will be the public attribute name.
        A dictionary value will be the value of the public attribute.
        """
        for key in json:
            self.__dict__[key] = json[key]
