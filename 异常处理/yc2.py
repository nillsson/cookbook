#简单的异常案例
#给出异常提示
try:
    num = int(input("plez input your number:"))
    rst = 100/num
    print("计算结果是：{0}".format(rst))
#捕获一场后，把异常实例化，出错信息会在实例里
#注意一下写法
#以下语句是捕获ZeroDivisionError异常实例化实例e
except ZeroDivisionError as e:
    print("你输入的啥东西")
    print(e)
    #exit是退出程序的意思
    exit()
#作业：为什么我们可以直接打印出实例e，此时实例e应该实现了哪个函数
#如果是多个error的情况
#需要把越具体的错误，越往前放
#在异常类继承关系中，越是子类的异常，越往前放
#在处理异常的时候，一旦拦截到某一个异常，则不再继续
except NameError as e:
    print("名字起错了")
    print(e)
    exit()
except AttributeError as e:
    print("好像属性有问题")
    print(e)
    exit()
#所有的异常都是继承自Exception
#如果写上下面这句话，任何异常都会拦截住
except Exception as e:
    print("我也不知道哪儿出错了")
    print(e)
    exit()

print("hahaha")