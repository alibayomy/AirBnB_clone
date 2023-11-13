#!/usr/bin/python3
"""Module to represent Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Class to represent the Place

    Attributes:
        city_id (str): City.id
        user_id (str): User.id
        name (str): name
        description (str): description
        number_rooms (int): number_rooms
        number_bathrooms (int): number_bathrooms
        max_guest (int): max_guest
        price_by_night (int): price_by_night
        latitude (float): latitude
        longitude (float): longitude
        amenity_id (list): list of Amenity.id
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_id = ""
