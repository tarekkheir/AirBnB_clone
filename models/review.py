#!/usr/bin/python3
"""
Module Review class
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """class Review"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initexecution"""
        super().__init__(*args, **kwargs)
