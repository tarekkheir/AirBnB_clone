#!/usr/bin/python3
"""
Unittest for the BaseModel class
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Tests for the BaseModel class
    """
    def setUp(self):
        """
        Define instructions that will be executed before each test method
        """
        self.base = BaseModel()

    def test_instance(self):
        """
        Test the instance of the initialization of the class
        """
        self.assertIsInstance(self.base, BaseModel)
        self.assertIsInstance(self.base.id, str)
        self.assertIsInstance(self.base.created_at, datetime)
        self.assertIsInstance(self.base.updated_at, datetime)

    def test_str(self):
        """
        Test for the str method
        """
        test_str = self.base.__str__()
        self.assertIsInstance(test_str, str)

    def test_to_dict(self):
        """
        Test for the to_dict method
        """
        test_json = self.base.to_dict()
        self.assertIsInstance(test_json, dict)

    def test_save(self):
        """
        Test for the save method
        """
        test_up = self.base.updated_at
        self.base.save()
        self.assertTrue(self.base.updated_at != test_up)

    def test_kwargs(self):
        """
        Test for kwargs
        """
        my_model_json = self.base.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertFalse(self.base is my_new_model)

if __name__ == '__main__':
    unittest.main()
