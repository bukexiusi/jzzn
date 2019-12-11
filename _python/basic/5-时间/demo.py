import time
import math
import sys

sys.version_info
print(int(time.time()*1000))

def timeStamp(timeNum):
    timeStamp = float(timeNum/1000)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(otherStyleTime)

print(timeStamp(1574230260588))
print(timeStamp(1573210260588))
import calendar
print(calendar.isleap(2000))
print(calendar.isleap(1900))

from datetime import datetime

currentSecond = datetime.now().second
currentMinute = datetime.now().minute
currentHour = datetime.now().hour

currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year
print(currentYear)
print(currentMonth)
print(currentDay)

a = 1
x = (1 if a == 1 else 0)*12123
print(x)

print(1574230260588 - 1573210260588)
print(1000*60*60*24)
print(1020000000 // 86400000)
print(math.ceil(1020000000 / 86400000))
# print((1574230260588 - 1573210260588) % 1000*60*60*24)
print(1000*60*60*24)
