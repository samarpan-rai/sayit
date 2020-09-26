"""Main module."""

from .conversion import int2text

def sayit(number:int):
    """
    Convert large number to  sayable text format.

    Arguments:
        number : A (large) number
    """

    # Handle the first 10 positive numbers 
    if 0 <= number < 10:
        return int2text(number)
