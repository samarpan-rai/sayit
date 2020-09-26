"""Main module."""

from .conversion import int2text


def say(number: int):
    """
    Convert large number to  sayable text format.

    Arguments:
        number : A (large) number
    """

    # Handle the first 10 positive numbers
    
    return int2text(number)
