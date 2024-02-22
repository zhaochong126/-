'''
时间戳中有十三位和十位
十三位的代表是毫秒
十位代表的是秒
'''
import time

t1 = 1704879917000

time2 = time.localtime(t1/1000)
# print(time)
time1 = time.strftime('%Y-%m-%d,%Y:%m:%d',time2)
print(time1)