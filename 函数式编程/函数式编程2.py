#filter 案例
#对于iyge列表，对其进行过滤，偶数组成一个新列表
#需要定义过滤函数
#过滤函数要求有输入，返回布尔值
def isEven(a):
    return a % 2 ==0

l = [2,314,31,2314,1312,123,31221,414,32,123]
rst = filter(isEven,l)
#返回的filter内容是一个可迭代对象
print(type(rst))
print(rst)
print([i for i in rst])

#排序的案例
a = [13,1451234,121,21,43,3211,2,4,5,12312]
al = sorted(a, reverse=True)
print(al)
#排序的案例2
b = [-313,3132,54,132,-31123,32,0]
#按照绝对值进行排序
#abs是求绝对值的意思
#即按照绝对值的倒序排序
bl = sorted(b, key=abs,reverse=True)
print(bl)
#排序案例3
astr = ['mimi','yiyi','yijie','colin','mama']
str1 = sorted(astr)
print(str1)

str2 = sorted(astr,key=str.lower)
print(str2)

#定义一个普通函数
def myF(a):
    print("In myF")
    return None

a = myF(8)
print(a)

#函数作为返回值返回，被返回的函数在函数体内定义
def myF2():
    def myF3():
        print("in myF3")
        return 3
    return myF3
#使用上面定义
#调用myF2,返回一个函数myF3,赋值给f3
f3 = myF2()
print(type(f3))
print(f3)

print(f3())

#复杂一点的返回函数的例子
#args:参数列表
#1. myF4定义函数，返回内部定义的函数myF5
#2. myF5使用了外部变量，这个变量是myF4的参数
def myF4(*args):
    def myF5():
        rst = 0
        for n in args:
            rst += n
        return rst
    return myF5

f5 = myF4(12,13,1,34123,13241,12)
print(f5())
f6 = myF4(1,2,3,421,123)
print(f6())

#闭包常见坑
def count():
    #定义列表，列表里存放的是定义的函数
    fs = []
    for i in range(1,4):
        #定义了一个函数f
        #f是一个闭包结构
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())
##出现的问题
#造成上述情况的原因是，返回函数引用了变量i，i并非立即执行，而是等到三个函数都返回的时候才统一使用，此时i已经变成了3，最终调用的时候，都返回的是3*3
# 此问题描述成：返回闭包时，返回函数不能引用任何循环变量
#解决方案：再创建一个函数，用该函数的函数绑定循环变量的当前值，无论该循环变量以后如何改变，已经绑定的函数参数值不再改变
def count1():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs
f1,f2,f3 = count1()
print(f1())
print(f2())
print(f3())

def hello():
    print("hello world")

hello()

f = hello
f()

print(id(f) == id(hello))
#对hello函数进行功能扩展，前提是不改变原有的代码
#每次打印hello之前打印当前系统时间
#使用装饰器
import time
#高阶函数，以函数作为参数
def printTime(f):
    def wrapper(*args,**kwargs):
        print("Time:",time.ctime())
        return f(*args,**kwargs)
    return wrapper
#上述定义了装饰器，使用的时候需要用到@,此符号是python的语法糖
@printTime
def hello():
    print("Hello world")

hello()

@printTime
def hello2():
    print("mimi")

hello2()
hello()
#上面对函数的装饰使用了系统定义的语法糖
#下面开始手动执行下装饰器
#先定义函数
def hello3():
    print("我是手动的")

hello3()

hello3 = printTime(hello3)
hello3()


f = printTime(hello3)
f()
#作业：解释下面的执行结果

#偏函数
#把字符串转化成十进制数字
print(int("23141"))
#求八进制的12345表示成十进制是多少
print(int("12345",base=8))
#新建一个函数，此函数是默认输入的字符串是16进制数字
#把此字符串返回十进制的数字
def int16(x,base=16):
    return int(x,base)
print(int16("12345"))

import functools
#实现上面int16的功能
int16 = functools.partial(int,base=16)

print(int16("12345"))

