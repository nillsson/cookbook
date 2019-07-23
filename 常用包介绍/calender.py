import calendar
#calender： 获取一年的日历字符串
#参数
# w = 每个日期之间的间隔字符数
# l = 每周所占的行数
# c = 每个月之间的间隔字符数
#cal = calendar.calendar(2017)
#print(type(cal))
#print(cal)

cal = calendar.calendar(2017,l=0,c=5)
print(cal)

#isleap:判断某一年是否是闰年
calendar.isleap(2018)

#leapdays:获取指定年份之间的闰年的个数
calendar.leapdays(2001,2018)
help(calendar.leapdays)

#month() 获取某个月的日历字符串
#格式：calendar.month(年，月)
#回值：月日历的字符串

#monthrange() 获取一个月的周几开始及天数
#格式：calendar.monthrange(年，月)
#回值：tuple(周几开始，总天数)
#注意：周默认0-6表示周一到周天

#monthcalendar() 返回一个月每天的矩阵列表
#格式：calendar.monthcalendar(年，月)
#回值：二级列表
#注意：矩阵中没有天数用0表示

#prcal：直接打印日历
#calendar.prcal(2019)
#prmonth：直接打印某个月，返回值无

#weekday() 获取周几
#格式：calendar.weekday(年，月，日)
#返回值：周几对应的数字