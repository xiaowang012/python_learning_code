import time,datetime

#暂停10秒输出并获取当前的时间

time_1 = datetime.datetime.now()
print(time_1.strftime("%Y.%m.%d %H:%M:%S"))
time.sleep(10)
time_2 = datetime.datetime.now()
print(time_2.strftime("%Y.%m.%d %H:%M:%S"))