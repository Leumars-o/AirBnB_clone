#!/usr/bin/python3
"""A module that defines an Place creating class
"""
from models.base_model import BaseModel
import models


class Place(BaseModel):
    """User class inherits from BaseModel

    Attributes:
        - city_id (str): Public class attribute for Places's email
        - user_id (str): Public class attribute for Places's password
        - name (str): Public class attribute for Place's first name
        - description (str): Public class attribute for Place's last name
        - number _rooms(int): Public class attribute for Places number_rooms
        - number_bathrooms(int): Public class attribute for Place's
            number_bathrooms
        - max_guest(int): Public class attribute for Place's max_guest
        - price_by_night(int): Public class attribute for Places's
            Prince by night
        - latitude(0.0): Public class attribute for Places's latitude
        - longitude(0.0): Public class attribute for Place's longitude
        - aenity_ids(list): public class attributes for place's amenity_id's

    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
