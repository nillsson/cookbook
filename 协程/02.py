# 协程代码案例1

def simple_coroutine():
    print("-> Start")
    x = yield
    print("-> Recieved", x)

#主线程
sc = simple_coroutine()
print(1111)
#可以使用sc.send(None)，效果一样
#预激
next(sc)

print(2222)
sc.send("Zhexiao")