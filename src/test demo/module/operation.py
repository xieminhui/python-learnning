"""
@Date: 2020-01-06 10:36:38
@LastEditors: xieminhui
@LastEditTime: 2020-01-06 10:49:11
"""
"""
@Date: 2020-01-06 10:36:38
@LastEditors: xieminhui
@LastEditTime: 2020-01-06 10:41:22
"""


def addNum(*num):
    sum = 0
    for i in num:
        sum += i
    return sum


def multiplication(*num):
    sum = 1
    for i in num:
        sum *= i
    return sum

