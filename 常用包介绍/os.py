import os
mydir = os.getcwd()
print(mydir)

os.chdir("C:/Users/dodo/PycharmProjects/cookbook/2-OOP")
mydir = os.getcwd()
print(mydir)

os.chdir("C:/Users/dodo/PycharmProjects/cookbook/常用包介绍")
mydir = os.getcwd()
print(mydir)

ld = os.listdir("C:/Users/dodo/PycharmProjects/cookbook/2-OOP")
print(ld)

ld_1 = os.listdir()
print(ld_1)

#rst = os.makedirs('Testyiyi/yiyi/baby')
#print(rst)

#dir 是列出当前文件和文件夹的系统命令
sh = os.system("dir")
print(sh)

#type nul>文件名.后缀名创建文件
#newFile = os.system("type nul>haha.txt")
#print(newFile)

#newfile = os.system("type nul>C:/Users/dodo/PycharmProjects/cookbook/常用包介绍/Testyiyi/yiyi/haha.txt")
#print(newfile)

#env = os.getenv("PATH")
#print(env)

#print(os.name)
#print(os.sep)
import os.path as op

absp = op.abspath(".")
print(absp)

bn = op.basename("C:/Users/dodo/PycharmProjects/cookbook/常用包介绍")
print(bn)

bd = "C:/Users/dodo/PycharmProjects/cookbook/"
fn = "常用包介绍"
p = op.join(bd, fn)
q = op.basename(p)
print(q)

t = op.split(p)
print(t)

rst = op.isdir("C:/Users/dodo/PycharmProjects/cookbook/常用包介绍/Testyiyi/yiyi/haha.txt")
print(rst)

e = op.exists("C:/Users/dodo/PycharmProjects/cookbook/常用包介绍")
print(e)

import shutil
#rst = shutil.copy("C:/Users/dodo/PycharmProjects/cookbook/常用包介绍/Testyiyi/yiyi/haha.txt","C:/Users/dodo/PycharmProjects/cookbook/常用包介绍/Testyiyi/yiyi/baby/see.txt")
#print(rst)

#rst = shutil.copyfile("C:/Users/dodo/PycharmProjects/cookbook/常用包介绍/Testyiyi/yiyi/baby/see.txt","C:/Users/dodo/PycharmProjects/cookbook/常用包介绍/Testyiyi/yiyi/haha.txt")
#print(rst)

#rst = shutil.move("C:/Users/dodo/PycharmProjects/cookbook/常用包介绍/Testyiyi/yiyi/haha.txt","C:/Users/dodo/PycharmProjects/cookbook/常用包介绍/Testyiyi")
#print(rst)

#arxiv = shutil.make_archive("C:/Users/dodo/PycharmProjects/cookbook/常用包介绍/Testyiyi/baby","zip","C:/Users/dodo/PycharmProjects/cookbook/常用包介绍/Testyiyi/yiyi")
#print(arxiv)

import zipfile
#zf = zipfile.ZipFile("C:/Users/dodo/PycharmProjects/cookbook/常用包介绍/Testyiyi/baby.zip")
#print(zf)

#rst = zf.getinfo("see.txt")
#print(rst)

#nl = zf.namelist()
#print(nl)

#rst = zf.extractall("C:/Users/dodo/PycharmProjects/cookbook/常用包介绍/Testyiyi/bb")
#print(rst)

import random
#print(random.random())
print(int(100*random.random()))
print(random.choice(range(101)))
l1 = [i for i in range(10)]
print(l1)
random.shuffle(l1)
print(l1)
print(random.randint(0,100))

