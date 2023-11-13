import datetime

def get_time_stamp(result):
    utct_date1 = datetime.datetime.strptime(result, "%Y-%m-%dT%H:%M:%S.%f%z")
    time_array1 = utct_date1.timestamp()
    return time_array1

#获取utc时间戳
#print(int(datetime.datetime.now(datetime.timezone.utc).timestamp()*1000))
print(datetime.datetime.now())