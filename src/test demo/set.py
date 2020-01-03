"""
@Date: 2020-01-03 10:47:26
@LastEditors: xieminhui
@LastEditTime: 2020-01-03 10:54:38
"""
# 集合

set1 = {"tom", "jan", "jack"}

# value 是元组
set2 = set(("12", "23"))

# value是字符串
set3 = set("12")

# value是list
set4 = set([12, 23])

print(f"set1 = {set1}")

print(f"set2 = {set2}")

print(f"set3 = {set3}")

print(f"set4 = {set4}")


# 添加

print(f"更新前set1是{set1}")

set1.add("lucy")

print(f"更新前set1是{set1}")


# 移除

print(f"更新前set2是{set2}")

set2.remove("12")

print(f"更新前set1是{set2}")
