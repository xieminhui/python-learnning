"""
@Date: 2020-01-06 17:09:08
@LastEditors  : xieminhui
@LastEditTime : 2020-01-06 17:15:56
"""


# 类

print("基类person")


class person:
    name: ""
    age: 1
    sex: ""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myprint(self):
        print(f"name and age are {self.name, self.age}")


p1 = person("tom", 20)

p1.myprint()

# 继承

print("我是student,我要继承person")


class student(person):
    grade = ""

    def __init__(self, n, a, g):
        super().__init__(n, a)
        self.grade = g

    def myprint(self):
        super().myprint()
        print(f"i am a {self.grade} student, likes sports!")


boy1 = student("jan", 11, "四年级")

boy1.myprint()

# 多重继承

print("多重继承")


class studentRoles:
    job = ""
    special = ""

    def __init__(self, j, s):
        self.job = j
        self.special = s

    def myprint(self):
        print("i am a special student!")


class test(studentRoles, student):
    def __init__(self, name, age, grade, job, special):
        student.__init__(self, name, age, grade)
        studentRoles.__init__(self, job, special)


t1 = test("jack", 23, "大学", "monitor", "class management")

t1.myprint()
