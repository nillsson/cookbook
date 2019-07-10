'''
定义一个学生类，用来形容学生
'''

#定义一个空的类
class Student():
    # 一个空类，pass代表直接跳过
    #此处pass必须有
    pass

#定义一个对象
mingyue = Student()

#再定义一个类，用来描述听python的学生

class PythonStudent():
    #用None 给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    #需要注意
    #1. def doHomework 的缩进层级
    #2. 系统默认有一个self参数
    def doHomework(self):
        print("I 在做作业")
        #推荐在函数末尾使用return语句
        return None

#实例化一个叫yueyue的学生
yueyue = PythonStudent()
mimi = PythonStudent()

print(yueyue.name)
print(yueyue.age)
print(PythonStudent.__dict__)
#注意成员函数的调用没有传递进入参数
yueyue.doHomework()