#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = 0
    for i in set(my_list):
        new += i
        return new
