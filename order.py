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
            raise TypeError("Invalid Input - LineNo is not integer")
        self._lineNo = int(linenum)

        prodcode = inputstring[linenumlen:(linenumlen+codelen)].strip()
        if not prodcode.isalnum():
            raise TypeError("Invalid Input - Product Code is not alphanumeric")
        self._code = prodcode

        category = inputstring[(linenumlen+codelen):(linenumlen+codelen+catelen)].strip()
        if not category.isalnum():
            raise TypeError("Invalid Input - Category is not alphanumeric")
        self._category = category

        quantity = inputstring[(linenumlen+codelen+catelen):(linenumlen+codelen+catelen+quanlen)].strip()
        if not quantity.isdigit():
            raise TypeError("Invalid Input - Quantity is not numeric")
        self._quantity = int(quantity)

        price = inputstring[(linenumlen+codelen+catelen+quanlen):inputlen].strip()
        if not price.isdigit():
            raise TypeError("Invalid Input - Price is not numeric")

        self._price = float(price)/100

    def create(self):
        return self










