#!/usr/bin/python3
"""
Unittest for the City class that inherit from BaseModel
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    Tests for the State class
    """
    def setUp(self):
        """
        To define instructions that will be executed before each test
        """
        self.my_city = City()

    def test_instance(self):
        """
        Test the instance of the class
        """
        self.assertIsInstance(self.my_city, City)

    def test_inheritence(self):
        """
        Test if the class inherit from BaseModel
        """
        self.assertTrue(issubclass(City, BaseModel))

    def test_attr(self):
        """
        Test the attributes
        """
        self.assertTrue(hasattr(self.my_city, 'id'))
        self.assertTrue(hasattr(self.my_city, 'created_at'))
        self.assertTrue(hasattr(self.my_city, 'updated_at'))
        self.assertTrue(hasattr(self.my_city, 'state_id'))
        self.assertTrue(hasattr(self.my_city, 'name'))

    def test_attr_type(self):
        """
        Test the type of the attribute name
        """
        self.assertIsInstance(self.my_city.name, str)
        self.assertIsInstance(self.my_city.state_id, str)

    def test_set_attr(self):
        """
        Test to set the name
        """
        self.my_city.name = "Denver"
        self.assertEqual(self.my_city.name, "Denver")

    def tearDown(self):
        """
        To define instructions that will be executed after each test
        """
        del self.my_city
