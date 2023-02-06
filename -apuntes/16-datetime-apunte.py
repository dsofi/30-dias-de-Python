# Python datetime
# Python has got datetime module to handle date and time.
import datetime
print(dir(datetime))

# With dir or help built-in commands it is possible to know the available functions in a certain module. As you can see, in the datetime module there are many functions, but we will focus on date, datetime, time and timedelta. Let se see them one by one.

# Getting datetime Information
from datetime import datetime
print('--- Data Time ---')
now = datetime.now()
print(now)                      
day = now.day                 
month = now.month             
year = now.year              
hour = now.hour            
minute = now.minute           
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp : ', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}') 
# Timestamp or Unix timestamp is the number of seconds elapsed from 1st of January 1970 UTC.

# Formatting Date Output Using strftime
new_year = datetime(2020, 1, 1)
print(new_year)      # 2020-01-01 00:00:00
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute) #1 1 2020 0 0
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 1/1/2020, 0:0

# Formatting date time using strftime method and the documentation can be found here (https://strftime.org/)
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)

# String to Time Using strptime
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

# Using date from datetime
print('--- Usign Date ---')
from datetime import date
d = date(2020, 1, 1)
print(d)
print('Current date:', d.today())    
today = date.today()
print("Current year:", today.year)  
print("Current month:", today.month) 
print("Current day:", today.day)     

# Time Objects to Represent Time
print('--- Time Objects ---')
from datetime import time
# time(hour, minute, second, microsecond)
a = time()
print("a =", a)
b = time(10, 30, 50)
print("b =", b)
c = time(hour=10, minute=30, second=50)
print("c =", c)
d = time(10, 30, 50, 200555)
print("d =", d)
e = time(10, 30)
print("e =", e)
f = time(10)
print("f =", f)
g = time(0, 30)
print("g =", g)

# Difference Between Two Points in Time Using
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
print('Time left for new year: ', time_left_for_newyear)    # Time left for new year:  27 days, 0:00:00

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff)  # Time left for new year: 26 days, 23: 01: 00

# Difference Between Two Points in Time Using timedelata
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)