#!/usr/bin/python3
"""Module to represent City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class to represent the City

    Attributes:
        state_id (str): state id.
        name (str): City name.
    """
    state_id = ""
    name = ""
