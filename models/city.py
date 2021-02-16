#!/usr/bin/python3
"""
City Class that inherit from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Public class attributes
    """
    state_id = ""
    name = ""
