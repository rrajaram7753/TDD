""" Homework Project
"""


class Order:

    def __init__(self, inputstring):
        if not inputstring:
            raise ValueError("Input string is empty")

        if not len(inputstring) == 39:
            raise ValueError("input string is not valid")

        lineNo = inputstring[:4].strip()
        if not lineNo.isdigit():
            raise TypeError("Invalid Input - LineNo is not integer")
        self._lineNo = int(lineNo)

        prodCode = inputstring[4:14].strip()
        """
        if not prodCode.isalpha():
            raise TypeError("Invalid Input - Product Code is not alphanumeric")
        """
        self._code = prodCode

        category = inputstring[14:24].strip()
        """
        if not category.isalpha():
            raise TypeError("Invalid Input - Category is not alphanumeric")
        """
        self._category = category

        quantity = inputstring[24:28].strip()
        if not quantity.isdigit():
            raise TypeError("Invalid Input - Quantity is not numeric")
        self._quantity = quantity

        price = inputstring[29:39].strip()
        if not price.isdigit():
            raise TypeError("Invalid Input - Price is not numeric")

        price = inputstring[29:37].strip() + "." + inputstring[37:39].strip()
        self._price = float(price)
        
    def create(self):
        return self










