# Mail 编程
## 电子邮件的历史
- 起源
    - 1969 Leonard K. 教授发给同事的"LO"
    - 1971 美国国防部自主的阿帕网（Arpanet）的通讯机制
    - 通讯地址里用@.
    - 1987年中国的第一份邮件
        `Across the Great Wall we can reach every corner in the world`
    - 管理程序
        - Euroda（邮件管理程序）使邮件普及
        - Nestscape, Outlook, Foxmail后来居上
        - Hotmail 使用浏览器发送邮件
    - 参考资料
        - [官网](https://docs.python.org/3/library/email.mime.html)
   
## 邮件工作流程
- MUA(MailUserAgent)邮件用户代理
- MTA(MailTransferAgent)邮件传输代理
- MDA(MailDeliverAgent)邮件投递代理
- 发件人: 3105862757@qq.com
- 收件人：nillsson@163.com
- 流程
    1. MUA -> MTA, 邮件已经在服务器上了
    2. qq MTA -> ... -> 163 MTA, 邮件在163的服务器上了
    3. 163 MTA -> ... -> 163 MDA, 此时邮件已经在你的邮箱里
    4. 163 MDA -> MUA(Foxmail/Outlook), 邮件下载到本地电脑
- 编写程序
    - 发送： MUA -> MTA with SMTP: SimpleMailTransferProtocal, 包含MTA -> MTA
    - 接受： MDA -> MUA with POP3 and IMAP: PstOfficeProtocal v3 and InternetMessageAccessprotocal v4
- 准备工作
    - 注册邮箱
    - 第三方邮箱需要特殊设置， 以qq邮箱为例
        - 进入设置中心
        - 取得授权码
- Python for mail
    - SMTP 协议负责发送邮件
        - 使用Email模块构建模块
            - 纯文本邮件
            - 案例p01.py
        - HTML格式邮件发送
            - 准备HTML代码作为内容
            - 把邮件的subtype设为html
            - 发送
            - 案例p02.py
        - 发送带附件的邮件
            - 可以把邮件看作是一个文本邮件和一个附件的合体
            - 一封邮件如果涉及多个部分，需要使用MIMEMultipart格式构建
            - 添加一个MIMEText正文
            - 添加一个MIMEBase或者MEMEText作为附件
            - 案例p03.py
        - 添加邮件头， 抄送等信息
            - mail["From"] 表示发送着信息，包括姓名和邮件
            - mail["To"] 表示接收者信息，包括姓名和邮件地址
            - mail["Subject"] 表示摘要或者主题信息
            - 案例p04.py
        - 同时支持html和text格式
            - 构建一个MIMEMultipart格式邮件
            - MIMEMultipart的subtype设置成alternative格式
            - 添加HTML和text邮件
            - 案例p05.py
        - POP3协议接受邮件
            - 本质上是MDA到MUA的一个过程
            - 从 MDA下载下来的是一个完整的邮件结构体，需要解析才能得到每个具体可读的内容
                - 步骤：
                    1. 用poplib下载邮件结构体原始内容
                        1. 准备相应的内容（邮件地址，密码，POP3实例）
                        2. 身份认证
                        3. 一般会先得到邮箱内邮件的整体列表
                        4. 根据相应序号，得到某一封信的数据流
                        5. 利用解析函数进行解析出相应的邮件结构体
                    2. 用email解析邮件的具体内容
                - 案例p06.py
        