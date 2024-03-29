#!/usr/bin/env python3
"""A module that provides a class `BaseModel` that defines all
common attributes/methods for other classes.

classes:
    - BaseModel


"""
import uuid
import datetime
# from models import storage
import models


class BaseModel():
    """A class that defines all
    common attributes/methods for other classes.

    Methods:
        - __str__
        - save
        - to_dict

    """

    def __init__(self, *args, **kwargs):
        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"
                        )
                if key != "__class__":
                    try:
                        setattr(self, key, value)
                    except ValueError:
                        raise ValueError
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """A Method that returns the class details in string format

        Returns:
            str: string represemtation of the class
        """

        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        model_dict = self.__dict__.copy()
        model_dict["__class__"] = self.__class__.__name__
        model_dict['created_at'] = model_dict['created_at'].isoformat()
        model_dict['updated_at'] = model_dict['updated_at'].isoformat()
        return (model_dict)
