#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    num_s = len(argv) - 1
    if num_s == 0:
        print("0 arguments.")
    elif num_s == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_s))
        for i in range(nume_s):
            print("{}: {}".format(i + 1, argv[i]))
            i += 1
