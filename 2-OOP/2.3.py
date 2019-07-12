class Fish():
    def __init__(self):
        self.name = name

    def swim(self):
        print("I am swimming")

class Bird():
    def __init__(self):
        self.name = name

    def fly(self):
        print("I am flying")

class Person():
    def __init__(self,name):
        self.name = name

    def work(self):
        print("I am working")

class SuperMan(Person, Bird, Fish):
    def __init__(self, name):
        self.name = name


# 单继承的例子
class Student(Person):
    def __init__(self, name):
        self.name = name


s = SuperMan("mimi")
s.fly()
s.swim()

stu = Student("dama")
stu.work()

#菱形继承问题

class A():
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass

#构造函数1
class A():
   def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")

class C(B):
    pass

C = C()


#构造函数2
class A():
   def __init__(self):
        print("A")

class B(A):
    def __init__(self,name):
        print("B")
        print("this is {0}".format(name))

class C(B):
    #C想扩展B的构造函数，即调用B的构造函数后再添加一些功能
    #有两种方法实现
    '''
    #第一种通过父类名调用
    def __init__(self,name):
        B.__init__(self,name)
        print("Cc")
    '''

    #第二种使用super调用
    def __init__(self,name):
        super(C,self).__init__(name)
        print("Cc")

C = C("mimi")

