""" Homework Project
"""


class Order:

    def __init__(self, inputstring):
        if not inputstring:
            raise ValueError("Input string is empty")

        if not len(inputstring) == 39:
            raise ValueError("input string is not valid")

    def create(self):
        return self










