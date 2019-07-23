import time
#时间模块的属性
#timezone：当前时区和UTC时间相差的秒数，在没有夏令时的情况下的间隔，东八区的是-28800
#altzone:当前时区和UTC时间相差的秒数，在有夏令时的情况下的间隔
#daylight:检测当前是否是夏令时时间状态，0表示是
print(time.timezone)
print(time.altzone)
print(time.daylight)

#得到时间戳
print(time.time())

#localtime,得到当前时间的时间结构
#可以通过点号操作符得到相应的属性元素的内容
t = time.localtime()
print(t)
print(t.tm_hour)

#asctome() 返回元组的正常字符串化之后的时间格式
#格式：time.asctime(时间元组)
#返回值：字符串 Tue Jun 6 11:11:00 2017
tt = time.asctime(t)
print(tt)

#ctime:获取字符串化的当前时间
c = time.ctime()
print(c)

#mktime() 使用时间原则获取对应的时间戳
#格式：time.mktime(时间元组)
#返回值：浮点数时间戳

ts = time.mktime(t)
print(type(ts))
print(ts)


#sleep:使程序进入睡眠，n秒后继续
for i in range(10):
    print(i)
    #time.sleep(1)

#clock:获取cpu时间，3.0-3.3版本直接使用，3.6调用有问题
t0 = time.clock()
time.sleep(3)
t1 = time.clock()
print(t1-t0)

#表示时间的格式
#strftime:将时间元组转化为自定义的字符串格式

#把时间表示成 2019 7.16 19：17
ft = time.strftime("%Y-%m-%d %H:%M",t)
print(ft)

#timeit
def doIt():
    for i in range(10):
        print("repeat {0}".format(i))

t = timeit.timeit(stmt = doIt,number = 3)
print(t)