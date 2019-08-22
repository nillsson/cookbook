# HTTP简介
- 超文本（HyperText）: 包含有超链接（Link）和各种多媒体元素标记(Markup)的文本，这些超文本文件彼此链接，形成网状（web）, 因此又被称为网页（Web Page)。 这些链接使用URL表示，最常见的超文本格式是超文本标记语言HTML。
- URL(UniformResourceLocator）: 统一资源定位符，用来唯一地标识万维网中的某一个文档。
    - URL由协议，主机和端口（默认为80）以及文件名三部分构成。
        `Http://www.sxtyu.com:80/news/index.html`
        `协议：//主机端口（80）//文件名及其路径`
    - 例子
        ```
        ftp://rtfm.mit.edu
        ftp://rtfm.mit.edu/pub/abc.txt
        http://www.tsinghua.edu.cn
        http://www.tsinghua.edu.cn/docs/kjc/gjsys.html
        http://www.baidu.com/index.html
        ```
- 超文本传输协议HTTP: 一种按照URL指示，将超文本文档从一台主机（web服务器）传输到另一台主机（浏览器）的应用层协议，以实现超链接的功能
    - 例子：在用户点击URL为http://www.sxtyu.com/index.html的连接后，浏览器和web服务器执行一下动作：
        1. 浏览器分析超链接中的URL
        2. 浏览器向DNS请求解析www.sxtyu.com的IP地址
        3. DNS将机械出的IP地址202.2.16.21返回浏览器
        4. 浏览器与服务器建立TCP链接（80端口）
        5. 浏览器请求文档： GET/index.html\
        6. 服务器给出响应，将文档index.html发送给浏览器
        7. 释放TCP链接
        8. 浏览器显示index.html中的内容
    - 非持久链接：浏览器每请求一个web文档， 就船舰一个新的链接，当文档传输完毕后，链接立即释放
        - HTTP1.0, HTTP0.9采用此链接方式
        - 对于请求的web页中包含多个其他文档对象（如图像，声音，视频等）的链接的情况，由于请求每个链接对象的文档都要创建信的链接，效率低下
    - 持久链接：在一个连接中，可以进行多次文档的请求和相应，服务器在发送完响应后，并不理解释放链接，浏览器可以使用该链接继续请求其他文档，链接保持的时间可以由双方进行协商。
    - 无状态性：同一客户端（浏览器）第二次访问同一个web服务器上的页面时，服务器无法知道这个客户曾经访问过。 
        - HTTP的无状态性简化了服务器的设计，使其更容易支持大量并发的HTTP请求。
## HTTP 报文结构
- 请求报文：从客户端（浏览器）向web服务器发送的请求报文，报文的所有字段都是ACSCII码。
    ```
    方法 URL 版本 
    (请求行 如： GET /index.html HTTP/1.1)
    首部字段名 值 
    首部字段名 值
    \vdots          
    首部字段名 值
    （首部行：用来说明浏览器，服务器或报文主题的一些信息 如：
    Host: www.sxtyu.com
    Connection:close
    User-Agent: Mozilla/5.0
    Accept-Language: EN)
    实体主体（Entity Body）
    ```
- 返回报文: 从web服务器到客户机（浏览器）的应答，报文的所有字段都是ACSCII码
    ```
    版本 状态码 短语 
    （状态行 如 HTTp/1.1 200 OK)
    首部字段名 值
    首部字段名 值
    \vdots
    首部字段名 值
    （首部行：用来说明浏览器，服务器或报文主体的一些信息 如：
    Date: Wed 08 May 2008 22
    Server: Apache/1 3 2(Unix)
    Content-Length:DateDaDa2087
    Content-Type text/html）
    实体主体
    ```
- 请求报文中的方法：对所请求对象所进行的操作，也就是一些命令
    - GET 请求读取一个web页面
    - HEAD 请求读取一个web页面的首部
    - POST 附件一个命名资源（如web页面，给服务器发信息）
    - PUT 请求存储一个web页面
    - DELETE 删除web而页面
    - TRACE 用于测试，要求服务器送回收到的请求
    - CONNECT 用于代理服务器
    - OPTION 查询特定选项 
- 响应报文中的状态码（Status-Code): 相应报文状态行中包含的一个3位数字，指明特定的请求是否被满足，如果没有满足，原因是什么。
    - 1xx 通知信息 如：100=服务器正在处理客户请求
    - 2xx 成功 如：200=请求成功
    - 3xx 重定向 如：301=页面改变了位置
    - 4xx 客户错误 如： 403=禁止的页面，404=页面未找到
    - 5xx 服务器错误 如： 500= 服务器内部错误，503=以后再试
    - 具体状态码的含义，请参考[W3C的HTTP1.1标准规范RFC2616](http://w3.org/Protocols/rfc2616/rfc2616.html)
- 首部字段或消息头
    - User-Agent 请求 关于浏览器和它平台的信息，如Mozilla5.0
    - Accept 请求 客户端处理的页面的类型， 如text/html
    - Accept-Charset 请求 客户可以接受的字符集，如Unicode-1-1
    - Accept-Encoding 请求 客户能处理的页面的详细方法，如gzip
    - Accept-Language 请求 客户能处理
- 报文结构实例
## HTTP代理
- web缓存或代理服务器（proxy server）是一种网络实体，能代表浏览器发出HTTP请求，并将最近的额一些请求和响应暂存在本地磁盘中，当请求的web页面先前暂存过，则直接将暂存的页面发给客户端（浏览器），无需再次访问Internet

    
        

        
