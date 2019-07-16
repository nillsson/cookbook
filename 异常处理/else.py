try:
    num = int(input("plz input your number:"))
    rst = 100/num
    print("计算结果是：{0}".format(rst))
except Exception as e:
    print("Exception")
else:
    print("No Exception")
finally:
    print("反正我会被执行的")