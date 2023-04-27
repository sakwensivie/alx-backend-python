#!/usr/bin/env python3
''' A module that takes a float and
returns a function that multiplies a float'''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates a multiplier function'''
    return lambda x: x * multiplier
