#协程案例2
def simple_coroutine(a):
    print("-> Start")

    b = yield a
    print("-> Recived", a, b)

    c = yield a + b
    print("-> Recived", a, b, c)

#主线程
sc = simple_coroutine(5)

aa = next(sc)
print(aa)

bb = sc.send(6)
print(bb)

cc = sc.send(7)
print(cc)