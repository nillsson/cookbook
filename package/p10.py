from pkg02 import *

stu = p01.Student()
stu.say()

#因为定义了__all__，所以下列代码会报错
inInit()