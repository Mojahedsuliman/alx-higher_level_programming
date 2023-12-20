#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in my_list:
            if count >= x:
                break
            try:
                print("{:d}".format(i), end="\n" if count == x - 1 else " ")
                count += 1
            except ValueError:
                continue
    except TypeError:
        pass  # Do nothing if the list is not iterable
    finally:
        return count
