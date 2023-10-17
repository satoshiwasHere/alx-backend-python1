#!/usr/bin/env python3
'''
Build upon the code with the correct
duck-typed annotations
'''

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    Outputs the first element of lst if there is any, otherwise Null
    '''
    if lst:
        return lst[0]
    else:
        return None
