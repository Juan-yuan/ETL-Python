import time
ts = 1652840528
timeArray = time.localtime(ts)
timeStyle = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(timeStyle)  # 2022-05-18 12:22:08