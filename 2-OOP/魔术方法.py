#__init__ 举例
class A():
    def __init__(self,name = 0):
        print("哈哈，我被调用了")

a = A()


#__call__ 举例
class A():
    def __init__(self,name = 0):
        print("哈哈，我被调用了")

    def __call__(self, *args, **kwargs):
        print("我被调用了again")

a = A()
a()


#__str__举例
class A():
    def __init__(self,name = 0):
        print("哈哈，我被调用了")

    def __call__(self, *args, **kwargs):
        print("我被调用了again")

    def __str__(self):
        return "这是__str__举例"

a = A()
print(a)

#__getattr__
class A():
    name = "Mimi"
    age = 12

    def __getattr__(self,name):
        print("没找到呀没找到")
        print(name)

a = A()
print(a.name)
print(a.addr)

#为什么会打印第四句话, 而且第四句话打印的None (因为__getattr__没有返回值，这里打印出来的None?)

#__setattr__举例
class Person():
    def __init__(self):
        pass

    def __setattr__(self, name, value):
        print("设置属性：{0}".format(name))
        #下面语句会导致问题，死循环
        #self.name = value
        #此种情况，为了避免死循环，规定统一调用父类魔法函数
        super().__setattr__(name,value)

p = Person()
p.addr = 18
p.age = 19
print(p.__dict__)
print(p.addr)
print(p.age)

p2 =Person()
p2.sex = "Female"
print(p2.__dict__)
