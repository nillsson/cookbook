# os-操作系统相关
- 跟操作系统
- 与系统相关的操作，主要包含在模块里
    - `os`, 操作系统目录相关
    - `os.path`, 系统路径相关操作
    - `shutil`， 高级文件操作，目录树的操作，文件复制，删除，移动
- 路径：
    - 绝对路径：总是从根目录上开始
    - 相对路径：基本以当前环境为开始的一个相对的地方

# os 模块
- `getcwd()` 获取当前的工作目录
    - 格式：`os.getcwd`
    - 返回值：当前工作目录的字符串
    - 当前工作目录就是程序在进行文件相关操作，默认查找文件的目录
- `chdir()` 改变当前的工作目录
    - 格式：`os.chdir(路径)`
    - 返回值：无
- `listdir()` 获取一个目录中所有子目录和文件的名称列表
    - 格式：`os.listdir(路径)`
    - 返回值：所有子目录和文件名称的列表
- `makedirs()`递归船舰文件夹
    - 格式：`os.makedirs(路径)`
    - 返回值：无
    - 递归路径：多个文件夹层层包含的路径就是递归路径
- `system()` 运行系统shell命令
    - 格式：`os.system(系统命令)`
    - 返回值： 打开一个shell或者终端截面
- `getenv()`获取指定的系统环境变量值
    - 格式：`os.getenv(环境变量名)`
    - 返回值：指定环境变量名对应的值
- `exit()`退出当前程序
    - 格式：`exit()`
    - 返回值：无

# 值部分
- `os.curdir`:current dir当前目录
- `os.pardir`:parent dir父目录
- `os.sep`:当前系统的路径分隔符
    - windows:`\\`
    - linux:`/`
- `os.linesep`:当前系统的换行符号
    - windows: `\r\n`
    - unix,linux,macos:`\n`
- `os.name`：当前系统名称
    - windows:`nt`
    - mac, unix,linux:`posix`
- 在路经相关的操作中，不要手动拼写地址，因为手动拼写的路径可能不具有移植性

# `os.path` 模块，跟路径相关的模块
- `abspath()`将路径转化为绝对路径
    - 格式： `os.path.abspath(路径)`
    - 返回值： 路径的绝对路径形式
- `basename()`获取路径中的文件名部分
    - 格式:`os.path.basename(路径)`
    - 返回值：文件名字符串
- `join()`将多个路径拼合成一个路径
    - 格式:`os.path.join(路径1，路径2，...)`
    - 返回值：组合之后的新路径字符串
- `split()` 将路径且各位文件夹部分和当前文件部分
    - 格式:`os.path.split(路径)` 
    - 返回值：路径和文件名组成的元组
- `isdir()` 检测是否是目录
    - 格式：`os.path.ispath(路径)`
    - 返回值：布尔值
- `exists()`检测文件或者目录是否存在
    - 格式：`os.path.exists(路径)`
    - 返回值：布尔值

# shutil 数据模块
- `copy()` 复制文件
    - 格式： `shutil.copy(来源路径，目标路径)`
    - 返回值：返回目标路径
    - 拷贝的同时，可以给文件重命名
- `copy2()`复制文件，保留元数据（文件信息）
- `copyfile()` 将一个文件中的内容复制到另一个文件中
- `move()` 移动文件/文件夹
# 归档和压缩
- 归档： 把多个文件或者多个文件合并到一个文件当中 
- 压缩： 用算法把多个文件或者问急啊急啊无损或者有损合并到一个文件当中
- `make_archive()`归档操作
    - 格式：`shutil.make_archive("归档之后的目录和文件名"，"后缀"，"需要归档的文件夹")`
    - 返回值：  归档之后的地址
- `unpack_archive()`解包操作
    - 格式:`shutil.unpack_archive("归档文件地址","解包之后的地址")`
    - 返回值：解包之后的地址
# zip-压缩包
- 模块名称叫做 `zipfile`
- `zipfile.Zipfile(file[,mode[,compression[,allowZip64]]])`
    - 创建一个Zipfile对象，表示一个zip文件。参数fle表示文件的路径或类文件对象(file-like)
- `ZipFile.getinfo(name)`
    - 获取zip文档内指定文件的信息，返回一个zipfile.ZipInfo对象，它包括我呢见的详细信息
- `ZipFile.namelist()`
    - 获取zip文档内所有文件的名称列表
- `ZipFile.extractall([path[,members[,pwd]]])`
    - 解压zip文档中的所有文件到当前目录，参数members的默认值为zip文档内的所有文件名称列表
# random
- 随机数
- 所有的随机模块都是伪随机
- `random()`获取0-1之间的随机小数
    - 格式：`random.random()`
- `choice()`随机返回序列中的某个值
    - 格式：`rando.choice(序列)`
- `shuffle()`随机打乱列表(**原地打乱**)
    - 格式:`random.shuffle(列表)`
- `randin()`随机产生一个整数[a,b]
    - 格式：`random.randin()`
    