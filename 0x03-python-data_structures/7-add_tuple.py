#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lun = len(tuple_a)
    lan = len(tuple_b)
    if lun == 0:
        tuple_a = (0, 0)
    if lun == 1:
        tuple_a = (tuple_a[0], 0)
    if lan == 0:
        tuple_b = (0, 0)
    if lan == 1:
        tuple_b = (tuple_b[0], 0)
    tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return tuple
