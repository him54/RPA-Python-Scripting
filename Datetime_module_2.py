# from datetime import*
# d,m,y = [int(x) for x in input("Enter the date in India Timezone").split('/')]
# d1 = date(y,m,d)
# print(d1)
# print(d1.strftime('Day %w of the week.This is %A and %B is a month name'))



# from datetime import*
# d1,m1,y1 = [int(x) for x in input("Enter the date in India Timezone").split('/')]
# date1 = date(y1,m1,d1)
# print(d1)
# d2,m2,y2 = [int(x) for x in input("Enter the date in India Timezone").split('/')]
# date2 = date(y2,m2,d2)
# print(d2)

# diff = date1-date2 # Difference between two date
# #weaks = diff.days // 7
# weeks,days=(divmod(diff.days, 7))
# print(weeks,days)


# from datetime import*
# d1 = datetime(2016,4,29,16,45,0)
# p = timedelta(days=10, seconds=10, minutes=20, hours=12)
# print(d1+p)

#output
2016-05-10 05:05:10


from datetime import*
date1 = datetime(1996,6, 26)
print(date1 + timedelta(days = 10))

# output
1996-07-06 00:00:00
