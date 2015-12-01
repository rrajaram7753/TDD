""" Homework Project
"""


class Order:

    def __init__(self, inputstring):

        inputLen = 39
        lNumLen = 4
        codeLen = 10
        cateLen = 10
        quanLen = 5
        priceLen = 10

        if not inputstring:
            raise ValueError("Input string is empty")

        if not len(inputstring) == inputLen:
            raise ValueError("input string is not valid")

        lineNo = inputstring[:lNumLen].strip()
        if not lineNo.isdigit():
            raise TypeError("Invalid Input - LineNo is not integer")
        self._lineNo = int(lineNo)

        prodCode = inputstring[lNumLen:(lNumLen+codeLen)].strip()
        if not prodCode.isalnum():
            raise TypeError("Invalid Input - Product Code is not alphanumeric")
        self._code = prodCode

        category = inputstring[(lNumLen+codeLen):(lNumLen+codeLen+cateLen)].strip()
        if not category.isalnum():
            raise TypeError("Invalid Input - Category is not alphanumeric")
        self._category = category

        quantity = inputstring[(lNumLen+codeLen+cateLen):(lNumLen+codeLen+cateLen+quanLen)].strip()
        if not quantity.isdigit():
            raise TypeError("Invalid Input - Quantity is not numeric")
        self._quantity = int(quantity)

        price = inputstring[(lNumLen+codeLen+cateLen+quanLen):inputLen].strip()
        if not price.isdigit():
            raise TypeError("Invalid Input - Price is not numeric")

        self._price = float(price)/100

    def create(self):
        return self










