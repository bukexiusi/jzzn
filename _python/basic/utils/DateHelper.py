import time, datetime

date_map = {
    '0': '零',
    '1': '一',
    '2': '二',
    '3': '三',
    '4': '四',
    '5': '五',
    '6': '六',
    '7': '七',
    '8': '八',
    '9': '九'
}

date_map2 = {
    '0': '〇',
    '1': '一',
    '2': '二',
    '3': '三',
    '4': '四',
    '5': '五',
    '6': '六',
    '7': '七',
    '8': '八',
    '9': '九'
}

# 二零一九年二月十一号
def chinese_date(timeStr):
    result = ""
    timeArray = time.strptime(timeStr, "%Y-%m-%d %H:%M:%S")
    # 年
    for year_s in str(timeArray.tm_year):
        result = result + date_map.get(year_s)
    result = result + "年"
    # 月
    if len(str(timeArray.tm_mon)) == 1:
        result = result + date_map.get(str(timeArray.tm_mon))
    else:
        if str(timeArray.tm_mon)[0] == "1":
            result = result + "十" + date_map.get(str(timeArray.tm_mon)[1])
        else:
            result = result + date_map.get(str(timeArray.tm_mon)[0]) + "十" + date_map.get(str(timeArray.tm_mon)[1])
    result = result + "月"
    # 日
    if len(str(timeArray.tm_mday)) == 1:
        result = result + date_map.get(str(timeArray.tm_mday))
    else:
        if str(timeArray.tm_mday)[0] == "1":
            result = result + "十" + date_map.get(str(timeArray.tm_mday)[1])
        else:
            result = result + date_map.get(str(timeArray.tm_mday)[0]) + "十" + date_map.get(str(timeArray.tm_mday)[1])
    result = result + "日"
    return result

# 二零一九年二月十一号
def chinese_date2(timeStr):
    result = ""
    timeArray = time.strptime(timeStr, "%Y-%m-%d %H:%M:%S")
    # 年
    for year_s in str(timeArray.tm_year):
        result = result + date_map2.get(year_s)
    result = result + "年"
    # 月
    if len(str(timeArray.tm_mon)) == 1:
        result = result + date_map2.get(str(timeArray.tm_mon))
    else:
        if str(timeArray.tm_mon)[0] == "1":
            result = result + "十" + date_map2.get(str(timeArray.tm_mon)[1])
        else:
            result = result + date_map2.get(str(timeArray.tm_mon)[0]) + "十" + date_map2.get(str(timeArray.tm_mon)[1])
    result = result + "月"
    # 日
    if len(str(timeArray.tm_mday)) == 1:
        result = result + date_map2.get(str(timeArray.tm_mday))
    else:
        if str(timeArray.tm_mday)[0] == "1":
            result = result + "十" + date_map2.get(str(timeArray.tm_mday)[1])
        else:
            result = result + date_map2.get(str(timeArray.tm_mday)[0]) + "十" + date_map2.get(str(timeArray.tm_mday)[1])
    result = result + "日"
    return  result


if __name__ == "__main__":
    # 字符类型的时间
    tss1 = '2019-11-11 00:00:00'
    # 转为时间数组
    timeArray = time.strptime(tss1, "%Y-%m-%d %H:%M:%S")
    # 转为时间戳
    timeStamp = int(time.mktime(timeArray))
    chinese_date(timeStamp)

    print(chinese_date2(time.time()))

