import datetime

#datetime常见属性
#datetime.date 一个理性的日期，提供year，month，day属性
#print(hasattr(datetime,"date"))

#datetime.time 提供一个理想的时间，居于hour，minute，sec，microsec等内容
#datetime.datetime 提供日期跟时间的组合
#datetime.timedelta 提供一个时间差，时间长度

#datetime.datetime
#from datetime import datetime
#常用类方法
#today
#now
#utcnow
#fromtimestamp 从时间戳返回本地时间
dt = datetime.datetime(2017, 7, 16)
print(dt)


#timedelta
from datetime import datetime,timedelta
t1 = datetime.now()
print(t1)
print(t1.strftime("%Y-%m-%d %H:%M:%S"))

#td表示以小时的时间长度
td = timedelta(hours = 1)
#当前时间加上时间间隔后，得到一个小时候的时间格式化输出
print((t1+td).strftime("%Y-%m-%d %H:%M:%S"))
