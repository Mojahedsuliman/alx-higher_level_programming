#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="\n" if count == x - 1 else " ")
                count += 1
        except IndexError:
            break
    else:
        return count
    raise ValueError("x cannot be bigger than the length of my_list")
