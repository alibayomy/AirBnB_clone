#!/usr/bin/python3
"""Module to represent User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class to represent the user

    Attributes:
        email (str): user email
        password (str): user password
        first_name (str): user first_name
        last_name (str): user last_name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
