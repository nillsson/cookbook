#打开文件，用写的方式

#f称为文件句柄
#r表示后面字符串内容不需要转义
f = open(r"test01.txt",'r')
#文件打开后必须关闭
f.close()
#此案例说明，以写方式打开文件，默认是如果没有文件，则创建

#with 语句案例
with open(r"test01.txt",'r') as f:
    pass
    #下面语句块开始对文件f进行操作
    #在本模块中不需要在使用close关闭文件f

with open(r'test01.txt','r') as f:
    #按行读取内容
    strline = f.readline()
    #此结构保证能够完整读取文件知道结束
    while strline:
        print(strline)
        strline = f.readline()

#list 能用打开的文件作为参数，把文件内每一行内容作为一个元素
with open(r'test01.txt','r') as f:
    #以打开的文件f作为参数，创建列表
    l = list(f)
    for line in l:
        print(line)
#read 是按字符读取文件内容
#允许输入参数决定读取几个字符，如果没有指定，从当前位置读取到结尾
#否则，从当前位置读取指定个数字符
with open(r'test01.txt', 'r') as f:
    strChar = f.read(3)
    print(len(strChar))
    print(strChar)
#作业：使用read读取文件，每次读取一个，使用循环读完
#尽量保持格式
with open(r'test01.txt', 'r') as f:
    strChar = f.read()
    while strChar:
        print(strChar)
        strChar = f.read()



#seek的案例
#打开文件后，从第五个字节开始读取
#打开读写指针在0处，即文件的开头
with open(r'test01.txt', 'r') as f:
    f.seek(6,0)
    strChar2 = f.read()
    print(strChar2)
#关于读取文件的联系
#打开文件，三个字符一组读出内容，然后显示在屏幕上
#每读一次，休息一秒钟
import time

with open(r'test01.txt', 'r') as f:
    strChar3 = f.read(3)
    while strChar3:
        print(strChar3)
        time.sleep(1)
        strChar3 = f.read(3)
# 解释以下运行结果，为什么不是每行三个字符
# 转义字符:\n(换行符-将光标移动到下一行的开头)

with open(r'test01.txt', 'r') as f:
    strChar3 = f.read(3)
    pos = f.tell()
    while strChar3:
        print(pos)
        print(strChar3)
        pos = f.tell()
        strChar3 = f.read(3)

# write 案例
#1. 向文件追加一句诗
#a 代表追加方式打开
with open(r'test01.txt', 'a') as f:
    #注意字符串内含有换行符
    f.write("\n生活不仅有眼前的苟且\n还有远方的苟且")
    l = ["\n还有远方的枸杞","\n但庆幸一直有你"]
    f.writelines(l)