"""
@Date: 2020-01-06 10:33:50
@LastEditors: xieminhui
@LastEditTime: 2020-01-06 10:45:29
"""
# 模块

import sys

import operation

from operation import multiplication

print("命令行参数如下:")
for i in sys.argv:
    print(i)

print("\n\nPython 路径为：", sys.path, "\n")


# module add.py

print("module add.py")

print(f"1 + 1 = {operation.addNum( 1, 1)}")


# from import

print("from import start")

print(f"2 * 3 * 4 = {multiplication(2, 3, 4)}")
