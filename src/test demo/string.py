"""
@Date: 2020-01-02 14:28:44
@LastEditors: xieminhui
@LastEditTime: 2020-01-02 14:34:50
"""

var1 = "hello world!"

# 字符串截取

print(f"{var1[:6]}tom")

print(f"截取部分是{var1[1]}")

# 格式化
print("格式化=====start")
print("我叫 %s 今年 %d 岁!" % ("小明", 10))
print("格式化=====end")

# 字符串函数
print("将字符串的第一个字符转换为大写：capitalize")

print(f"{var1} => {var1.capitalize()}")
