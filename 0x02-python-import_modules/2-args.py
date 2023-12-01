#!/usr/bin/python3
from sys import argv
if len(argv) - 1 == 0:
    print("0 arguments.")
elif len(argv) - 1 == 1:
    print("1 argument:".format(argv[1]))
    print("{}: {}".format(1, argv[1]))
else:
    print("{} arguments:".format(len(argv) - 1))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))

