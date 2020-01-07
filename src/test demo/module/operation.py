"""
@Date: 2020-01-06 10:36:38
@LastEditors: xieminhui
@LastEditTime: 2020-01-06 19:45:25
"""
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
    print(f"opea.py {__name__}")

    sum = 1
    for i in num:
        sum *= i
    return sum

