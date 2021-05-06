#!/usr/bin/python3
def search_replace(my_list, search, replace):
    rep = []
    for i in len(my_list):
        if i == search:
            rep.append(replace)
        else:
            rep.append(i)
    return (rep)
