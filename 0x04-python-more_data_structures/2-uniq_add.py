#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = set()
    total = 0
    for number in my_list:
        if isinstance(number, int) and number not in result:
            result.add(number)
            total += number
            return totalt
