# from datetime import date
# from datetime import datetime
# from datetime import time

from datetime import datetime


# x=datetime.datetime.now()
#
# print(x)
# print(x.strftime("%A"))

# my_date=date(1996,12,11)
# print("date passed",my_date)

# my_date=date(2000,12,39)

# my_date=date('1996',12,11)


# today=date.today()
# print("today's date is:",today)
# print("today's date is",today.year)
# print("current year",today.year)
# print("current month",today.month)
# print("current day",today.day)

#
# date_time=datetime.fromtimestamp(1882006587)
# print("Date time from:",date_time)

# my_time=time(13,24,56)
# print("enterd time ",my_time)

# my_time=time(minute=12)
# print("time with one argument",my_time)

# my_time=time()
# print("my time",my_time)

# Time=time(11,34,56,1200)
# print("hour=",Time.hour)
# print("minute=",Time.minute)
# print("secound=",Time.second)
# print("microsecound=",Time.microsecond)

# a=datetime(1999,12,12,12,12,12,342380)
# print(a)


a=datetime(1999,12,12,12,12,12)
print("year",a.year)
print("month=",a.month)
print("day=",a.day)
print("hour=",a.hour)
print("minute=",a.minute)
print("timestamp=",a.timestamp())