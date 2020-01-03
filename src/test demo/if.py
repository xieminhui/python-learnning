"""
@Date: 2020-01-03 11:09:31
@LastEditors  : xieminhui
@LastEditTime : 2020-01-03 11:14:36
"""

# if

person = {"name": "tom", "age": 18, "sex": "man"}

if person["age"] >= 18:
    print(f"{person['name']} is adult")
else:
    print(f"{person['name']} is not adult")

print("============= end end end ==============")

# 嵌套if

print("========== 嵌套if start ==============")

if person["age"] >= 18:
    print(f"{person['name']} is adult")
    if person["sex"] == "man":
       print(f"{person['name']} is also a {person['sex']}")
else:
    print(f"{person['name']} is not adult")