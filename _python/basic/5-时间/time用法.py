import datetime, re
import time

# 字符类型的时间
tss1 = '19-1-22'
# 字符串转为时间数组
timeArray = time.strptime(tss1, "%y-%m-%d")
# 时间数组转为时间戳
timeStamp = int(time.mktime(timeArray))
# 时间戳转时间数组
timeArray2 = time.localtime(timeStamp)
# 时间数组转字符串年月日替换
otherStyleTime= time.strftime("%Y{y}%m{m}%d{d}", timeArray2).format(y='年', m='月', d='日')

# 采集值
collectValue = "1963-8-15"
timeArray = time.strptime(collectValue, "%Y-%m-%d")
memory = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print("memory", memory)

# 输出值
outputTimeArray = time.strptime(memory, "%Y-%m-%d %H:%M:%S")
output = time.strftime("%y{y}%m{m}%d{d}", outputTimeArray).format(y='年', m='月', d='日')
print("output", output)
# memory = str(timeArray.tm_year) + '-' + str(timeArray.tm_mon) + '-' + str(timeArray.tm_mday) + ' ' + str(timeArray.tm_hour) + ":" + str(timeArray.tm_min) + ":" + str(timeArray.tm_sec)

# time_str = "1993-02-10"
# if time_str:
#     time_array = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
#     print("time_array", time_array)

assign_time = "19-07-11"

time_array = time.strptime(assign_time, "%y-%m-%d")
var = time.strftime("%Y-%m-%d ", time_array).format(y='年', m='月',
                                                         d='日')
print("var", var)


print(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))


# 时间去零
aaa = "2019年04月09日"
aaa = "2019-04-09"
re_aaa = re.findall("\d+", aaa)
print(re_aaa)

aaa = re.sub("2019", "${zn1}", aaa, count=1)
aaa = re.sub("04", "${zn1}", aaa, count=1)

var = "2019-04-04 04:04:04"
var = "2019年04月04日"
re_var = re.findall("\d+", var)
if len(re_var) > 0:
    var = re.sub("\d+", "{zn}", var)
    for rv in re_var:
        if rv.startswith("0"):
            rv = rv[1:]
        var = re.sub("{zn}", rv, var, 1)
print(var)

print(time.time())
print(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))
# print(time.strftime('%Y{y}%m{}%d{}%H{}%M{}%S{}',time.localtime(time.time())).format(y="年"))
print(time.strftime('%Y{}%m{}%d{}%H{}%M{}%S{}',time.localtime(time.time())).format("年", "月", "日", "时", "分", "秒"))


# 字符类型的时间
tss1 = '2019-02-10 00:00:00'
# 字符串转为时间数组
timeArray = time.strptime(tss1, "%Y-%m-%d %H:%M:%S")
# 时间数组转为时间戳
timeStamp = time.mktime(timeArray)*1000
print(timeStamp)


_id = "1"
id_set = ["1"]
assert _id not in id_set, print("@22222")
print("111111")


