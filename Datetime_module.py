
#'datetime'  - combination of date and time
              #It contains attributes : year, month, day, hour, minute, second, microsecond and tzinfo
#date class -  Date of Gregorian calender
              # It contains attribute : year, month , date
#time class - 24 * 60 * 60
#timedelta class - Diffrenece between two time class


#ctime() - function of time module  (current time)
#today() - Datetime module


#Format code used in strftime()
#%a - abbrivate name Sun, Mon
#%A - weekday full name - Sunday, Monday
#%w - 0, 1, 2,3 4, 5, 6
#%d - 01, 02 ----, 31
#%b - Month as a abbreviated name -- Jan, Feb, -- Dec
#%B - month as full name - January , February-- December
#%m - Month as zero - padded decimal number. 01, 02, --- 12

#import time
#t = time.ctime()
#print(t)

from datetime import*
now = datetime.now()
print(now)
print('Date: {}/{}/{}'.format(now.day,now.month, now.year))
print('Time: {}:{}:{}'.format(now.hour, now.minute, now.second))

now = date.today()
print(now)
str = now.strftime("%e, %A")
print(str)


