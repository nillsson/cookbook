# 持久化- pickle
- 序列化(持久化，落地)：把程序运行中的信息保存在磁盘上
- 反序列化：序列化的逆过程
- pickle： python提供的序列化模块
- `pickle.dump`：序列化
- `pickle.load`：反序列化
# 持久化- shelve
- 持久化工具
- 类似字典，用kv对保存数据，存取方式跟字典也类似
- `open`, `close`
- shelve特性：
    - 不支持多个应用并行写入
        - 为了解决这个问题，open的时候可以使用`flag=r`
    - 写回问题
        - shelve情况下不会等待持久化对象进行任何修改
        - 解决方法：强制写回：`writeback=True`
        