"""
@Date: 2020-01-02 17:12:17
@LastEditors: xieminhui
@LastEditTime: 2020-01-02 17:12:54
"""

## 字典

dict = {"name": "tom", "age": 13, "weight": "32kg"}

# 访问

print(f"访问dict==={dict}")

print(f"{dict['name']} age is {dict['age']},体重是{dict['weight']}")


# 修改

dict["age"] = 11

print(f"修改tom年龄后是{dict['age']}")

# 删除

del dict["age"]

print(f"删除tom的年龄后dict{dict}")

# 函数

print(f"创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值fromkeys")
dict = {"name": "tom", "age": 13, "weight": "32kg"}
seq = ("name", "age", "weight")
value = "set a value"
dict1 = dict.fromkeys(seq)

print(f"fromkeys not set value: dict1{dict1}")

dict1 = dict.fromkeys(seq, value)

print(f"fromkeys  set value: dict1{dict1}")
