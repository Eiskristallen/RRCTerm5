from __future__ import division
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def cal(list):
    aver = 0
    sum = 0
    for item in list:
        sum += item
    aver = sum/len(list)
    return aver


def numa(list):
    result = 0
    ss = 0
    leng = len(list)
    for item in range(0, leng):
        ss += (list[item] - cal(list)) ** 2
    result = (ss/(leng-1))**0.5
    return result


print(cal(num))
print(numa(num))
