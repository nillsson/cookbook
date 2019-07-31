#序列化案例
import pickle
yiyi = [19,"yiyi","IT",[176,65]]
age = 19
with open(r'test02.txt','wb') as f:
    pickle.dump(yiyi, f)

# 反序列化案例
with open(r'test02.txt','rb') as f:
    b = pickle.load(f)
    print(b)

# 使用shelve创建文件并使用
import shelve
#打开文件，shv相当于一个字典
shv = shelve.open(r'yiyi.db')

shv['name'] = {"name":"yiyi","nickname":"Jiumi"}
shv['age'] = 19
shv['height'] = 176
shv['weight'] = 65

shv.close()
#通过以上案例发现，shelve自动创建的不仅仅是一个shv.db文件，还包括其他相关文件

#shelve读取案例
shv2 = shelve.open(r'yiyi.db')
try:
    print(shv2['name'])
    print(shv2['sex'])
except Exception as e:
    print("烦死了")
finally:
    shv.close()

# shelve之只读打开
shv3 = shelve.open(r'yiyi.db',flag='r')
try:
    print(shv3['name'])
    print(shv3['score'])
except Exception as e:
    print("出错了")
finally:
    shv3.close()

#shelve 忘记写回，需要使用强制写回
shv4 = shelve.open(r'yiyi.db')
try:
    k1 = shv4['name']
    print(k1)
    #此时，一旦shelve关闭，则内容还是存在内存中，没有写回数据库
    k1['name'] = "YiYi"
finally:
    shv4.close()

shv = shelve.open(r'yiyi.db')
try:
    k = shv['name']
    print(k)
finally:
    shv.close()

#shelve 忘记写回，需要使用强制写回
shvv = shelve.open(r"yiyi.db",writeback=True)
try:
    kk = shvv['name']
    print(kk)
    #此时，一旦shelve关闭，则内容还是存在于内存中，没有写回数据库
    kk['name'] = "YiYi"
finally:
    shvv.close()

shv = shelve.open(r'yiyi.db')
try:
    k1 = shv['name']
    print(k1)
finally:
    shv.close()

#shelve 使用with管理上下文环境

with shelve.open(r'yiyi.db',writeback=True) as shv:
    ka = shv['name']
    print(ka)
    #此时，一旦shelve关闭，则内容还是存在于内存中，没有写回数据库
    ka['name'] = "Yiyi"

with shelve.open(r'yiyi.db') as shv:
    print(shv['name'])