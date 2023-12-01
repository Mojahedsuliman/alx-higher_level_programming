#!/usr/bin/python3
if __name__ == "__main__":
    import sys as s
    result = 0
    for i in s.argv:
        if i != s.argv[0]:
            result += int(i)
            print("{}".format(result))
