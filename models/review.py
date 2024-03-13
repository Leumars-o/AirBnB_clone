#!/usr/bin/python3
"""A module that defines a Review creating class
"""
from models.base_model import BaseModel
import models


class Review(BaseModel):
    """Review class inherits from BaseModel

    Attributes:
        place_id (str): Public class attribute for Review's place_id
        user_id (str): Public class attribute for Review's user_id
        text (str): Public class attribute for Review's text
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
