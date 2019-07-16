
class Student():
    def __init__(self,name="NoName",age=19):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0}".format(self.name))

def sayHello():
    print("Hi, welcome!")

#此判断语句建议一直作为程序入口
if __name__ == '__main__':#仅在作为主文件时才执行这句
    print("我是模块p01呀")