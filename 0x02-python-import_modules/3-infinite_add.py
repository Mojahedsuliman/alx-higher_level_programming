#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sz = len(sys.argv)
    sum = 0
    for i in range(1, sz):
        sum += int(sys.argv[i])
    print(sum))
