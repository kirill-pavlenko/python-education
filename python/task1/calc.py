"""This module implements basic calculator class"""


class Calculator:
    """This class computes basic math operations:
    addition, subtraction, multiplication, division"""

    @staticmethod
    def add(first_term, second_term):
        """This method performs addition.
        Returns first_term + second_term"""
        return first_term + second_term

    @staticmethod
    def subtract(minuend, subtrahend):
        """This method performs subtraction.
        Returns minuend - subtrahend"""
        return minuend - subtrahend

    @staticmethod
    def multiply(first_factor, second_factor):
        """This method performs multiplication.
        Returns first_factor * second_factor"""
        return first_factor * second_factor

    @staticmethod
    def divide(dividend, divider):
        """This method performs division.
        Returns dividend / divider"""
        if divider == 0:
            return "You can't divide by zero!"
        return dividend / divider
