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
        self.assertRaises(TypeError, Order, " A00 P15678923  SPORTING856     1012399")

    def test_checkLineNoIsSet(self):
        o = Order(" 100 P15678923  SPORTING856     1012399")
        self.assertEqual(o.create()._lineNo, 100)

    def test_validateLineProductCodeDataType(self):
        self.assertRaises(TypeError, Order, " 100 %15678923  SPORTING856     1012399")

    def test_checkProductCodeIsSet(self):
        o = Order(" 100 P156923    SPORTING856     1012399")
        self.assertEqual(str(o.create()._code), "P156923")

    def test_validateCategoryDataType(self):
        self.assertRaises(TypeError, Order, " 100 P156923    SP!RT*NG856     1012399")

    def test_checkCategoryIsSet(self):
        o = Order(" 100 P156923    SPORTING856     1012399")
        self.assertEqual(o.create()._category, "SPORTING")

    def test_validateQuantityDataType(self):
        self.assertRaises(TypeError, Order, " 100 P156923    SPORTING8X6     1012399")

    def test_checkProductQuantityIsSet(self):
        o = Order(" 100 P156923    SPORTING856     1012399")
        self.assertEqual(o.create()._quantity, 856)

    def test_validatePriceDataType(self):
        self.assertRaises(TypeError, Order, " 100 015678923 SPORTING99856    10_A39 ")

    def test_checkProductPriceIsSet(self):
        o = Order(" 100 015678923 SPORTING99856    101239 ")
        self.assertEqual(o.create()._price, 1012.39)

if __name__ == "__main__":
    unittest.main()


