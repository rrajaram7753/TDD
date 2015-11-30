""" unit test for Order
"""
import unittest
from order import Order


class TestOrder(unittest.TestCase):

    def test_checkForEmptyString(self):
        self.assertRaises(ValueError, Order, "")

    def test_checkForInvalidInput(self):
        self.assertRaises(ValueError, Order, "Hello World")
        self.assertRaises(ValueError, Order, "HelloWorldHelloWorldHelloWorldHelloWorld")

if __name__ == "__main__":
    unittest.main()


