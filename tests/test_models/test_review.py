#!/usr/bin/pyhon3
"""
Tests class Review
"""

import unittest
import json
from datetime import datetime
from models import base_model
from models import review


class TestReview(unittest.TestCase):
    """Test all attributes"""
    def test_place_id(self):
        """test place_id"""
        test = Review()
        self.assertEqual(type(test.place_id), str)
        self.assertTrue(hasattr(test, "place_id"))
        self.assertEqual(test.place_id, "")

    def test_user_id(self):
        """test user_id"""
        test = Review()
        self.assertEqual(type(test.user_id), str)
        self.assertTrue(hasattr(test, "user_id"))
        self.assertEqual(test.user_id, "")

    def test_text(self):
        """test text"""
        test = Review()
        self.assertEqual(type(test.text), str)
        self.assertTrue(hasattr(test, "text"))
        self.assertEqual(test.text, "")
