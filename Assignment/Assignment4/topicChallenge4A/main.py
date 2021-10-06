from __future__ import division
# define a list of number that are going to use to test function later
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def avg_cal(list):
    """
    this function calculate average of list of number and return the average value
    """
    aver = 0
    sum = 0
    for item in list:
        sum += item
    aver = sum/len(list)
    return aver


def stand_diviation(list):
    # """
    # this function calculate and return standar diviation of list of number
    # """
    result = 0
    ss = 0
    leng = len(list)
    for item in range(0, leng):
        ss += (list[item] - avg_cal(list)) ** 2
    result = (ss/(leng-1))**0.5
    return result


print("the average value is: %a" % avg_cal(num))
print("the standard diviation is: %a" % stand_diviation(num))
