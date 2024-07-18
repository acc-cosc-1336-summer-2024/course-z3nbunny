import unittest
from src.homework.j_classes.class_a import Die

class Test_Config(unittest.TestCase):

    def test_get_rolled_value_1 (self):
        die = Die()
        die.roll()
        roll_value = die.get_rolled_value()
        self.assertTrue(1 <= roll_value <= 6, f"The die roll value {roll_value} is outside of the expected range")

    def test_get_rolled_value_2 (self):
        die = Die()
        die.roll()
        roll_value = die.get_rolled_value()
        self.assertTrue(1 <= roll_value <= 6, f"The die roll value {roll_value} is outside of the expected range")

    def test_get_rolled_value_3 (self):
        die = Die()
        die.roll()
        roll_value = die.get_rolled_value()
        self.assertTrue(1 <= roll_value <= 6, f"The die roll value {roll_value} is outside of the expected range")