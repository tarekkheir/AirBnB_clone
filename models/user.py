#!/usr/bin/python3
"""
Module User class
"""


from models.base_model import BaseModel


class User(BaseModel):
    """class User set all parameters of users"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """init execution"""
        super().__init__(*args, **kwargs)
