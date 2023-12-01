#!/usr/bin/python3

import hidden_4

name = dir(hidden_4)
for i in name:
    if i[:2] != "__":
        print(i)
