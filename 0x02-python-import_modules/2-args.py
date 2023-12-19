#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l = len(sys.argv) - 1

    if l == 0:
        print("{} arguments.".format(l))
    elif l == 1:
        print("{} argument:".format(l))
    else:
        print("{} arguments:".format(l))
    if l >= 1:
        l = 0
        for argu in sys.argv:
            if l != 0:
                print("{}: {}".format(l, argu))
                l += 1
