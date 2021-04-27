#!/usr/bin/python3
def uppercase(str):
    i = 0
    for i in str:
        if (ord(str(i)) > 96 and ord(str(i)) < 123):
            print("{}".format(chr(ord(i) - 32)), end='')
        else:
            print("{}".format(str(i)), end='')
