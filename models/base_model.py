#!/usr/bin/python3
"""Module to represent BaseModel class"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel():
    """Class to represent the base model of the AirBnB Clone project"""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of BaseModel class

        Arguments:
            *args (tuple): unused.
            **kwargs (dict): dictionary of key/value pairs of attributes.
        """

        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        iso_format = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(value, iso_format)
                else:
                    self.__dict__[key] = value
        else:
            storage.new(self)

    def __str__(self):
        """Print formatted representation of the class"""
        c_name = self.__class__.__name__
        output = "[{}] ({}) {}".format(c_name, self.id, self.__dict__)
        return output

    def save(self):
        """Update the public instance attribute 'updated_at'
        and Save serialized object to a file"""
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values
        of '__dict__' of the instance"""
        new_dict = self.__dict__.copy()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        return new_dict
