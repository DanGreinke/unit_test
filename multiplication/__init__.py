"""
It's best to use math.prod() in real life. This is just for my own practice.
https://docs.python.org/3/library/math.html#math.prod
"""

def my_mult(args):
    """
    Accepts an iterable and returns the product of all elements.
    """
    result = 1
    for arg in args:
            result *= arg
    return result