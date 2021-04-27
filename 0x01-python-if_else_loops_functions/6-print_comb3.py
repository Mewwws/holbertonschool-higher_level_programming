#!/usr/bin/python3
for i in range(0, 8):
    for j in range(i + 1, 10):
        if i == 8 & j == 9:
            break
        print(i, j,", ", sep='', end='')
i = 8
print(i, j, sep='')
