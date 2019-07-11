class A():
    name = "dana"
    age = 19

    # 注意say的写法，参数由一个self
    def say(self):
        self.name = "aaa"
        self.age = 2009
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(self.age))

    def sayagain(s):
        print("I am {0}".format(s.name))
        print("My age {0}".format(s.age))


# 此案例说明类实例的属性和其对象的实例的属性在不对对象的实例属性赋值的前提下，指向同一个变量

# 此时，A称为类实例
print(A.name)
print(A.age)

print("*" * 20)

# id 可以鉴别一个变量是否和另一个变量是同一变量
print(id(A.name))
print(id(A.age))

print("*" * 20)
a = A()

print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))

print("*" * 20)
a = A()
a.name = "yaona"
a.age = 11

print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))

print(a.__dict__)

a.say()
a.sayagain()


class Teacher():
    name = "dana"
    age = 19

    def say(self):
        self.name = "yaona"
        self.age = 17
        print("My name is {0}".format(self.name))
        print("My name is {0}".format(self.age))

    def sayAgain():
        print(__class__.name)
        print(__class__.age)
        print("Hello, nice to see you again")


t = Teacher()
t.say()
# 调用绑定类函数使用类名
Teacher.sayAgain()

#关于self的案例
class Hj():
    name = "HJ"
    age = 29

    def __init__(self):
        self.name = "aaa"
        self.age = 200

    def say(self):
        print(self.name)
        print(self.age)

class B():
    name = "bbb"
    age = 90

ood = Hj()
#此时，系统会默认把ood作为第一个参数传入函数
ood.say()

#此时，self 被ood替换
Hj.say(ood)
# 同样可以把Hj作为参数传入
Hj.say(Hj)
#此时，传入的B是类实例B，因为B具有name和age属性，所以不会报错
Hj.say(B)

#以上代码，利用了鸭子模型


class Person():
    name = "daya"
    __age = 12

j = Person()
#name是公有变量
print(j.name)
#__age是私有变量，注意报错信息
#print(j.__age)

#name mangling 技术
print(Person.__dict__)
print(j._Person__age)