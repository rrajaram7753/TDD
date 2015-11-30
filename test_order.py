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

    def test_validateLineNoDataType(self):
        self.assertRaises(TypeError, Order, " a10 P15678923   SPORTING856    1012399")

    def test_checkLineNoIsSet(self):
        o = Order(" 100 P15678923   SPORTING856    1012399")
        self.assertEqual(self, o.create()._lineNo, 100)

    def test_validateLineProductCodeDataType(self):
        self.assertRaises(TypeError, Order, " 100 015678923   SPORTING856    1012399")

    def test_checkProductCodeIsSet(self):
        o = Order(" 100 P15678923   SPORTING856    1012399")
        self.assertEqual(self, o.create()._code, "P15678923")

    def test_validateCategoryDataType(self):
        self.assertRaises(TypeError, Order, " 100 P15678923   SPORTING856    1012399")

    def test_checkCategoryIsSet(self):
        o = Order(" 100 P15678923   SPORTING856    1012399")
        self.assertEqual(self, o.create()._category, "SPORTING")

    def test_validateQuantityDataType(self):
        self.assertRaises(TypeError, Order, " 100 P15678923  SPORTING856     10AB399")

    def test_checkProductQuantityIsSet(self):
        o = Order(" 100 P15678923   SPORTING856    1012399")
        self.assertEqual(self, o.create()._quantity, 856)

    def test_validatePriceDataType(self):
        self.assertRaises(TypeError, Order, " 100 015678923 SPORTING99856    1012399")

    def test_checkProductPriceIsSet(self):
        o = Order(" 100 P15678923 SPORTING99856    1012399")
        self.assertEqual(self, o.create()._category, 10123.99)

if __name__ == "__main__":
    unittest.main()


