"""
@Date: 2020-01-02 14:53:04
@LastEditors: xieminhui
@LastEditTime: 2020-01-02 14:53:24
"""

list = [1, 10, 100, 1000]

# 取值

print(f"list第一位的值是{list[0]}")

# 更新

list[0] = 2
list1 = [11]

print(f"list更新后第一位的值是{list[0]}")

#  删除
print(f"list是{list}")

del list[2]
print(f"list删除第3位后是{list}")

# list 函数

print(f"list是{list}")

list.append(1001)

print(f"list append 1001 是{list}")

list.append(list1)

print(f"list append list1 是{list}")
