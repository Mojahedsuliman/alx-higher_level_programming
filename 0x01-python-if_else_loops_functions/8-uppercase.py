#!/usr/bin/python3
def uppercase(s):
    for c in s:
        diff = ord('a') - ord('A')
        if ord('a') >= ord(c) >= ord('a'):
            print(chr(ord(c) - diff), end='')
        else:
            print(c, end='')
    print()
