#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l = len(sys.argv) - 1

    if l == 0:
        print("{:d} arguments.".format(l))
    elif l == 1:
        print("{:d} argument:".format(l))
    else:
        print("{:d} arguments:".format(l))
    if l >= 1:
        l = 0
        for argu in sys.argv:
            if l != 0:
                print("{:d}: {:d}".format(l, argu))
                l += 1
