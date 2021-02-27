#!/usr/bin/python3
"""
tests file storage
"""


import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import json
import os

class TestFileStorage(unittest.TestCase):
    """test all file storage methods"""
    def test_storage_all(self):
        """test all"""
        all_objs = storage.all()
        self.assertEqual(type(all_objs), dict)
        self.assertIs(all_objs, storage._FileStorage__objects)

    def test_save_and_load(self):
        """ test save and reload"""
        if os.path.exists('file.json'):
            os.remove("file.json")
        with open("file.json", "r") as f:
            self.assertEqual(0, len(f))
        test = BaseModel()
        test.name = "Holberton"
        test.my_number = 89
        test.save()
        with open("file.json", "r") as f:
            self.assertNotEqual(0, len(f))
        storage.reload()
        data = storage.all()
        k = "BaseModel." + test.id
        self.assertDictEqual(data[key].to_dict(), test.to_dict())
