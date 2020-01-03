"""
@Date: 2020-01-03 16:27:22
@LastEditors: xieminhui
@LastEditTime: 2020-01-03 16:35:51
"""
"""
@Date: 2020-01-03 16:27:22
@LastEditors  : xieminhui
@LastEditTime : 2020-01-03 16:32:41
"""


# 迭代器

list = [1, 2, 3, 4, 5]

it = iter(list)

print(f"list is {list}")
print(f"next(it) is {next(it)}")
print(f"next(it) is {next(it)}")

for x in it:
    print(x, end=" ")

