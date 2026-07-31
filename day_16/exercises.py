#Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
ts = now.timestamp()

#Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
print(now.strftime("%m/%d/%Y, %H:%M:%S"))

#Today is 5 December, 2019. Change this time string to time.
date_str = "5 December, 2019"
date_date = datetime.strptime(date_str, "%d %B, %Y")
print(date_date)

#Calculate the time difference between now and new year.
new_year = datetime(2027, 1, 1)
time_until_new_year = new_year - now
print(time_until_new_year)

#Calculate the time difference between 1 January 1970 and now.
from datetime import timedelta
seconds_after_frist_jan_1970 = now.timestamp()
print(timedelta(seconds=seconds_after_frist_jan_1970))
