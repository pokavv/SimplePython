import datetime as dt

now = dt.datetime.now()
year = now.year
weekday = now.weekday()
print(now)
print(year)

birth = dt.datetime(year=1997, month=10, day=24, hour=14)
print(birth)