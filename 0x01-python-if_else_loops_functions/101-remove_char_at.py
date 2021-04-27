#!/usr/bin/python3
def remove_char_at(str, n):
    s = ""
    l = len(str)
    for i in range(0, l):
        if i != n:
            s = s + str[i]
    return(s)
        
