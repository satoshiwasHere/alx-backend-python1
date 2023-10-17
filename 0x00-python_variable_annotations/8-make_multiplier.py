#!/usr/bin/env python3
'''
Accepts a float multiplier as argument and returns a function
that multiplies a float by the multiplier
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Creates a multiplier function.
    '''
    return lambda x: x * multiplier
