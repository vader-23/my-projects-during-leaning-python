import time
from calendar import isleap

def judge_leap_year(year):
    if isleap(year):
        return True
    else:
        return False

def days_in_month(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if leap_year:
            return 29
        else:
            return 28

age = input("enter your age: ")
localtime = time.localtime(time.time())
year = int(age)
month = year * 12 + localtime.tm_mon
day = 0

birth_year = int(localtime.tm_year) - year
year_local = birth_year + year

for i in range(birth_year, year_local):
    if judge_leap_year(i):
        day = day + 366
    else:
        day = day + 365

leap_year = judge_leap_year(localtime.tm_year)
for m in range(1, localtime.tm_mon):
    day = day + days_in_month(m, leap_year)

day = day + localtime.tm_mday
hours = day * 24 + int(localtime.tm_hour)
minutes = hours * 60 + int(localtime.tm_min)
seconds = minutes * 60 + int(localtime.tm_sec)
print("your age is %d years old or " % year , end="")
print("%d months or %d days or " % (month, day) , end="")
print("%d hours or %d minutes or %d seconds" % (hours , minutes, seconds))

