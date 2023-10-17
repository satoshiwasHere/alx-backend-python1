#!/usr/bin/env python3
'''
accepts a list mxd_lst of floats and integers then
returns their sum as a float
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    Evaluates the sum of a list of integers and floating-point numbers
    '''
    return float(sum(mxd_lst))
