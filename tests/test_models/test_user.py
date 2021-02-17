#!/usr/bin/python3
"""
Tests all attributes of User class
"""


import unittest
import json
from datetime import datetime
from models import base_model
from models import user


class TestUser(unittest.TestCase):
    """Test User class"""
    def test_email(self):
        """test email attribute"""
        test = User()
        self.assertEqual(type(test.email), str)
        self.assertTrue(hasattr(test, "email"))
        self.assertEqual(test.email, "")

    def test_password(self):
        """test password attribute"""
        test = User()
        self.assertEqual(type(test.password), str)
        self.assertTrue(hasattr(test, "password"))
        self.assertEqual(test.password, "")

    def test_first_name(self):
        """test first_name attribute"""
        test = User()
        self.assertEqual(type(test.first_name), str)
        self.assertTrue(hasattr(test, "first_name"))
        self.assertEqual(test.first_name, "")

    def test_last_name(self):
        """test last_name attribute"""
        test = User()
        self.assertEqual(type(test.last_name), str)
        self.assertTrue(hasattr(test, "last_name"))
        self.assertEqual(test.last_name, "")
