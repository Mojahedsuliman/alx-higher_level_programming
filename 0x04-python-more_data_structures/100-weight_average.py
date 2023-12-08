#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total_weight = 0
    total_sum = 0
    for i in my_list:
        total_weight += i[1]
        total_sum += i[0] * i[1]
        return total_sum / total_weight
