"""
@Date: 2020-01-03 16:56:02
@LastEditors: xieminhui
@LastEditTime: 2020-01-03 17:15:25
"""
# define function


def myprint():
    print("hello world!")


myprint()

# 有参数
def myprint1(name):
    print(f"hello {name}")


myprint1("tom")


# 默认参数


def myprint2(name="jan"):
    print(f"hello {name}")


myprint2()

# 不定参


def myprint3(*name):
    print(f"hello {name}")


myprint3("jan", "tom")

myprint3(["jan", "tom"], "bill")

