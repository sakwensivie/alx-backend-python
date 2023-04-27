#!/usr/bin/env python3
''' returns the sum of a mixed list'''


from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' returns the sum of a mixed list'''
    return float(sum(mxd_lst))
