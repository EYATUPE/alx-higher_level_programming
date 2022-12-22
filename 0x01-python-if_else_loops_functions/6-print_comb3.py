#!/usr/bin/python3
for s in range(0, 9):
    for e in range(s + 1, 10):
	    if s == 8:
	        print("{}{}".format(s, e))
	    else:
	        print("{}{}".format(s, e), end=", ")
