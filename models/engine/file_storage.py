#!/usr/bin/python3
"""
FileStorage module
"""


import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """ class FileStorage that serializes instances
    to a JSON file
    and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj
        with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = str(value)

        with open(self.__file_path, "w") as f:
            f.seek(0)
            json.dump(new_dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                data = json.load(f)
            for key, value in data.items():
                self.__objects[key] = value
        except:
            pass
