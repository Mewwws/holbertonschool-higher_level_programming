#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None:
        j = 0
        new = ""
        for i in my_string:
            if i != 'c' and i != 'C':
                new = new + i
        return (new)
