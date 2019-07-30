#简单函数举例
def printA():
    print("AAA")

printA()

#lambda 表达式的用法
#1.以lambda开头
#2.紧跟一定的参数（如果有的话）
#3.参数后用冒号和表达式主体隔开
#4.只是一个表达式，所以没有return

#计算一个数字的100倍
stm = lambda x: 100*x
#使用上跟函数一模一样
print(stm(88))

stm2 = lambda x,y,z : x * x + y * y - z * z
print(stm2(6,8,10))

#函数名称就是一个变量
def funA():
    print("In funA")
print(funA)
funB = funA
print(funB())

#高阶函数举例
#funA是普通函数，返回一个传入数字的100倍数字
def funA(n):
    return n*100
#再写一个函数，把传入参数乘以300倍，利用高阶函数
def funB(n):
    return funA(n)*3
print(funB(7))
#写一个高阶函数
def funC(n,f):
    #假定函数是把n扩大100倍
    return f(n)*3
print(funC(7,funA))
#比较funC和funB,显然funC的写法要优于funB
#例如
def funD(n):
    return n*10
#需求变更，需要把n放大30倍，此时funB则无法实现
print(funC(7,funD))


#map举例
#有一个列表，相对列表里的每一个元素乘以10，并得到新的列表
l1 = [i for i in range(10)]
print(l1)
l2 = []
for i in l1:
    l2.append(i*10)
print(l2)
#利用map实现
def mulTen(n):
    return n*10

l3 = map(mulTen, l1)
#map类型是一个可迭代结构，所以可以使用for遍历
for i in l3:
    print(i)
#以下列表生成式得到的结果为空，why？
l4 = [i for i in l3]
print(l4)

from functools import reduce
def myAdd(x,y):
    return x+y

#对于列表[1,2,3,4,5,6]执行myAdd的reduce操作
rst = reduce(myAdd,[1,2,3,4,5,6])
print(rst)