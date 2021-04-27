#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if (ord(str(i)) > 96 and ord(str(i)) < 123):
            print("{}".format(chr(ord(i) - 32)), end='')
        else:
            print("{}".format(i), end='')
