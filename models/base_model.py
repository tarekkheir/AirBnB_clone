#!/usr/bin/python3
"""
Class BaseModel that defines all common attributes/methods for ther classes:
"""
from datetime import datetime
import uuid


class BaseModel:
    """
    Class Base that creates an ID and date  when an instance is created
    """

    def __init__(self, *args, **kwargs):
        """
        Initialization of class Base model
        With the class attribute :
         - id
         - created_at
         - updated_at
        """
        if len(kwargs) > 0 and kwargs is not None:
            arg = self.__dict__
            time = '%Y-%m-%dT%H:%M:%S.%f'
            arg.update(kwargs)
            del arg['__class__']
            arg['created_at'] = datetime.strptime(self.created_at, time)
            arg['updated_at'] = datetime.strptime(self.updated_at, time)
        else:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Str method
        """
        name = type(self).__name__
        return ("[{}] ({}) {}".format(name, self.id, self.__dict__))

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        """
        to_dict = self.__dict__.copy()
        to_dict['__class__'] = type(self).__name__
        to_dict['updated_at'] = self.updated_at.isoformat()
        to_dict['created_at'] = self.created_at.isoformat()
        return to_dict
