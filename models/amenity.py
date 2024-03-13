#!/usr/bin/python3
"""A module that defines an Amenity creating class
"""
from models.base_model import BaseModel
import models


class Amenity(BaseModel):
    """A class that defines and creates Amenities

    Args:
        BaseModel (parent):
    """

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
