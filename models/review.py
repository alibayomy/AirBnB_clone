"""Module to represent Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class to represent the Review

    Attributes:
        place_id (str): place_id
        user_id (str): user_id
        text (str): review text
    """

    place_id = ""
    user_id = ""
    text = ""
