#!/usr/bin/env python3
'''
takes a float n as argument and returns the floor of the float
'''


def floor(n: float) -> int:
    '''
    Computes the floor of a floating-point number
    '''
    return int(n) if n >= 0 else int(n) - 1
