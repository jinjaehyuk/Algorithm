import datetime

H, M = map(int,input().split())

day = datetime.datetime(2023, 1, 23,H,M,0,0)
theday = day - datetime.timedelta(minutes=45)
print(theday.hour, theday.minute,sep=' ')
