#!/usr/bin/python3
"""Module to represent Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class to represent the Amenity

    Attributes:
        name (str): Amenity name.
    """
    name = ""
