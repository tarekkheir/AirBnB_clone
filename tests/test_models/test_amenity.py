#!/usr/bin/python3
"""
Unittest for the Amenity class that inherit from BaseModel
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Tests for the Amenity class
    """
    def setUp(self):
        """
        To define instructions that will be executed before each test
        """
        self.my_amenity = Amenity()

    def test_instance(self):
        """
        Test the instance of the class
        """
        self.assertIsInstance(self.my_amenity, Amenity)

    def test_inheritence(self):
        """
        Test if the class inherit from BaseModel
        """
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attr(self):
        """
        Test the attributes
        """
        self.assertTrue(hasattr(self.my_amenity, 'id'))
        self.assertTrue(hasattr(self.my_amenity, 'created_at'))
        self.assertTrue(hasattr(self.my_amenity, 'updated_at'))
        self.assertTrue(hasattr(self.my_amenity, 'name'))

    def test_name_type(self):
        """
        Test the type of the attribute name
        """
        self.assertIsInstance(self.my_amenity.name, str)

    def test_set_name(self):
        """
        Test to set the name
        """
        self.my_amenity.name = "???"
        self.assertEqual(self.my_amenity.name, "???")

    def tearDown(self):
        """
        To define instructions that will be executed after each test
        """
        del self.my_amenity
