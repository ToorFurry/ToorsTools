import os, datetime

d = os.path.abspath(input('Folder: ')) + '\\'
min_time = 0
max_time = 0
sum_time = 0
for i in os.listdir(d):
    tc = os.path.getctime(d + i)
    tm = os.path.getmtime(d + i)
    sum_time += tm - tc
    if not min_time:
        min_time = tc
    else:
        min_time = min(min_time, tc)
    max_time = max(max_time, tm)
    
print('StartTime:', datetime.datetime.fromtimestamp(min_time).strftime("%A, %d %B, %Y, %H:%M:%S"))
print('End Time: ', datetime.datetime.fromtimestamp(max_time).strftime("%A, %d %B, %Y, %H:%M:%S"))
print('Sum Time: ', str(datetime.timedelta(seconds = sum_time)))
print('Duration: ', str(datetime.timedelta(seconds = max_time - min_time)))
input()
