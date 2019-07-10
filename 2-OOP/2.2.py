
class A():
    name = "dana"
    age = 19

    #注意say的写法，参数由一个self
    def say(self):
        self.name = "aaa"
        self.age = 2009


#此案例说明类实例的属性和其对象的实例的属性在不对对象的实例属性赋值的前提下，指向同一个变量

#此时，A称为类实例
print(A.name)
print(A.age)

print("*" * 20)

#id 可以鉴别一个变量是否和另一个变量是同一变量
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


