#!/usr/bin/python3
import sys as s
if len(s.argv) - 1 == 0:
    print("0 arguments.")
elif len(s.argv) - 1 == 1:
    print("1 argument:".format(s.argv[1]))
    print("{}: {}".format(1, s.argv[1]))
else:
    print("{} arguments:".format(len(s.argv) - 1))
    for i in range(1, len(s.argv)):
        print("{}: {}".format(i, s.argv[i]))

