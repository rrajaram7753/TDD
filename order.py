""" Homework Project
"""


class Order:

    def __init__(self, inputstring):

        inputlen = 39
        linenumlen = 4
        codelen = 10
        catelen = 10
        quanlen = 5
        pricelen = 10

        if not inputstring:
            raise ValueError("Input string is empty")

        if not len(inputstring) == inputlen:
            raise ValueError("input string is not valid")

        linenum = inputstring[:linenumlen].strip()
        if not linenum.isdigit():
            raise TypeError("Invalid Input - LineNo is not Numeric")

        prodcode = inputstring[linenumlen:(linenumlen+codelen)].strip()
        if not prodcode.isalnum():
            raise TypeError("Invalid Input - Product Code is not alphanumeric")

        category = inputstring[(linenumlen+codelen):(linenumlen+codelen+catelen)].strip()
        if not category.isalnum():
            raise TypeError("Invalid Input - Category is not alphanumeric")

        quantity = inputstring[(linenumlen+codelen+catelen):(linenumlen+codelen+catelen+quanlen)].strip()
        if not quantity.isdigit():
            raise TypeError("Invalid Input - Quantity is not Numeric")

        price = inputstring[(linenumlen+codelen+catelen+quanlen):inputlen].strip()
        if not price.isdigit():
            raise TypeError("Invalid Input - Price is not numeric")

        self._lineNo = int(linenum)
        self._code = prodcode
        self._category = category
        self._quantity = int(quantity)
        self._price = float(price)/100

    def create(self):
        return self












