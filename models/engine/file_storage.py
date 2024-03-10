#!/usr/bin/python3
from models.base_model import BaseModel
import json
import os

class FileStorage:
    __file_path = "./models/engine/file.json"
    __objects = {}

    def __init__(self):
        pass
    
    def all(self):
        return (self.__objects)
    
    def new(self, obj):
        my_dict = obj.to_dict()
        key = f"{self.__class__.__name__}.str({obj.id})"
        self.__objects[key] = obj
    
    def save(self):
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(my_dict, file)
    
    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, ) as file:
                try:
                    python_dic = json.load(file)
                    for key, value in python_dic.items():
                        FileStorage.__objects[key] = BaseModel(**value)
                except (FileNotFoundError, json.JSONDecodeError):
                    self.save()
        else:
            self.save()

