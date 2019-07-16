#简单的异常案例
try:
    num = int(input("plez input your number:"))
    rst = 100/num
    print("计算结果是：{0}".format(rst))
except:
    print("你输入的啥东西")
    #exit是退出程序的意思
    exit()