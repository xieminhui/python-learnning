"""
@Date: 2020-01-03 11:22:44
@LastEditors: xieminhui
@LastEditTime: 2020-01-03 16:22:47
"""
"""
@Date: 2020-01-03 11:22:44
@LastEditors: xieminhui
@LastEditTime: 2020-01-03 16:09:20
"""
"""
@Date: 2020-01-03 11:22:44
@LastEditors  : xieminhui
@LastEditTime : 2020-01-03 16:08:50
"""
# 循环

# while

print("while 循环 start ==============")

var1 = 10

while var1 > 0:
    print(f"var1 = {var1}")
    var1 -= 2
else:
    print(f"while 循环结束，var1 = {var1}")

print("while 循环 end ==============")


print("for in 循环 start ==============")

var2 = [1, 2, 3, 4, 5]

for i in var2:
    print(i)

print("for in 循环 end ==============")


# break
print("break start ==============")

var3 = 10

while var3 > 0:
    if var3 % 2 == 0:
        break
    print(var3)
    var3 -= 1

print("break end ==============")

# continue

print("continue start ==============")

var3 = 10

while var3 > 0:
    var3 -= 1
    if var3 % 2 == 0:
        print(var3)
    else:
        continue

print("continue end ==============")
