import unittest
from src.homework.c_decisions.decisions import get_faulty_rating, get_options_ratio
from src.homework.c_decisions.decisions import get_faculty_rating

class TestConfig(unittest.TestCase):
    def test_get_options_ratio_1(self):
        self.assertEqual(0.25, get_options_ratio(5, 20))

class TestConfig(unittest.TestCase):
    def test_get_options_ratio_1(self):
        self.assertEqual(0.5, get_options_ratio(10, 20))

    def test_get_faulty_rating_excellent(self):
        self.assertEqual("Excellent", get_faulty_rating(.91))

    def test_get_faulty_rating_very_good(self):
        self.assertEqual("Very Good", get_faulty_rating(.85))

    def test_get_faulty_rating_very_good(self):
        self.assertEqual("Good", get_faulty_rating(.71))

    def test_get_faulty_rating_very_good(self):
        self.assertEqual("Needs Improvement", get_faulty_rating(.66))

    def test_get_faulty_rating_very_good(self):
        self.assertEqual("Unacceptable", get_faulty_rating(.45))