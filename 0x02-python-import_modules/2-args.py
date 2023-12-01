#!/usr/bin/python3
import sys
if len(sys.argv) - 1 == 0:
    print("0 arguments.")
elif len(sys.argv) - 1 == 1:
    print("1 argument:".format(sys.argv[1]))
    print("{}: {}".format(1, sys.argv[1]))
else:
    print("{} arguments:".format(len(sys.argv) - 1))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))

