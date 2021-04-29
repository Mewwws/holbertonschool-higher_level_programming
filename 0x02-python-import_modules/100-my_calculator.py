#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        s = sys.argv[2]
        if s == '+':
            print("{} {} {} = {}".format(a, s, b, add(a, b)))
        if s == '-':
            print("{} {} {} = {}".format(a, s, b, sub(a, b)))
        if s == '*':
            print("{} {} {} = {}".format(a, s, b, mul(a, b)))
        if s == '/':
            print("{} {} {} = {}".format(a, s, b, div(a, b)))
