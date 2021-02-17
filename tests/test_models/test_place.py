#!/usr/bin/python3
"""
Tests all places attributes
"""


import unittest
import json
from datetime import datetime
from models import base_model
from models import place


class TestPlace(unittest.TestCase):
    """Test attributes"""
    def test_city_id(self):
        """test city_id"""
        test = Place()
        self.assertEqual(type(test.city_id), str)
        self.assertTrue(hasattr(test, "city_id"))
        self.assertEqual(test.city_id, "")

    def test_user_id(self):
        """test user_id"""
        test = Place()
        self.assertEqual(type(test.user_id), str)
        self.assertTrue(hasattr(test, "user_id"))
        self.assertEqual(test.user_id, "")

    def test_name(self):
        """test name"""
        test = Place()
        self.assertEqual(type(test.name), str)
        self.assertTrue(hasattr(test, "name"))
        self.assertEqual(test.name, "")

    def test_description(self):
        """test description"""
        test = Place()
        self.assertEqual(type(test.description), str)
        self.assertTrue(hasattr(test, "description"))
        self.assertEqual(test.description, "")

    def test_number_rooms(self):
        """test number_rooms"""
        test = Place()
        self.assertTrue(hasattr(test, "number_rooms"))
        self.assertEqual(type(test.number_rooms), int)
        self.assertEqual(test.number_rooms, 0)

    def test_number_bathrooms(self):
        """test number_bathrooms"""
        m1 = Place()
        self.assertEqual(type(test.number_bathrooms), int)
        self.assertTrue(hasattr(test, "number_bathrooms"))
        self.assertEqual(test.number_bathrooms, 0)

    def test_max_guest(self):
        """test max_guest"""
        test = Place()
        self.assertEqual(type(test.max_guest), int)
        self.assertTrue(hasattr(test, "max_guest"))
        self.assertEqual(test.max_guest, 0)

    def test_price_by_night(self):
        """test price_by_night"""
        test = Place()
        self.assertEqual(type(test.price_by_night), int)
        self.assertTrue(hasattr(test, "price_by_night"))
        self.assertEqual(test.price_by_night, 0)

    def test_latitude(self):
        """test latitude"""
        test = Place()
        self.assertEqual(type(test.latitude), float)
        self.assertTrue(hasattr(test, "latitude"))
        self.assertEqual(test.latitude, 0.0)

    def test_longitude(self):
        """test longitude"""
        test = Place()
        self.assertEqual(type(test.longitude), float)
        self.assertTrue(hasattr(test, "longitude"))
        self.assertEqual(test.longitude, 0.0)

    def test_amenity_ids(self):
        """test amenity_ids"""
        test = Place()
        self.assertEqual(type(test.amenity_ids), list)
        self.assertTrue(hasattr(test, "amenity_ids"))
        self.assertEqual(len(test.amenity_ids), 0)
