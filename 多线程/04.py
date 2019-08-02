import time
import threading

def loop1(in1):
    # ctime 得到当前时间
    print("start loop 1 at :", time.ctime())
    print("我是参数",in1)
    time.sleep(4)
    print("end loop 1 at :", time.ctime())


def loop2(in1,in2):
    print("start loop 2 at :", time.ctime())
    print("我是参数",in1,"和参数",in2)
    time.sleep(2)
    print("end loop 2 at :", time.ctime())


def main():
    print("starting at :", time.ctime())
   # 生成Threading实例
    t1 = threading.Thread(target=loop1, args=("yiyi",))
    t1.start()

    t2 = threading.Thread(target=loop2, args=("yiyi","dodo"))
    t2.start()

    print("all done at :", time.ctime())



if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)