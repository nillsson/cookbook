try:
    print("Mimi")
    print(3.13140)
    #手动引发一个异常
    #注意语法 raise ErrorClassName
    raise ValueError
    print("有完没完")
except NameError as e:
    print("NameError")
except ValueError as e:
    print("ValueError")
except Exception as e:
    print("有异常")
finally:
    print("我肯定会执行的")


#自己定义异常
#需要注意：自定义异常必须是系统异常的子类
class DanaError(ValueError):
    pass
try:
    print("Mimi")
    print(3.13140)
    #手动引发一个异常
    #注意语法 raise ErrorClassName
    raise DanaError
    print("有完没完")
except NameError as e:
    print("NameError")
except DanaError as e:
    print("DanaError")
except Exception as e:
    print("有异常")
finally:
    print("我肯定会执行的")