#!/usr/bin/python3
for s in range(0, 100):
    if s == 99:
        print(s)
    else:
        print("{:0>2d}".format(s), end=", ")
