import calendar
from datetime import date


def last_month(year, month):
    last_month = calendar.monthrange(year, month)
    last_days = str(last_month[1])
    return last_days


# print(last_month(2020, 10))

def last_day_of_last_month():
    today = date.today()
    today_str = str(today).split('-')
    year = today_str[0]
    month = today_str[1]
    l_month = int(today_str[1])-1
    l_day = last_month(int(today_str[0]), l_month)
    if int(today_str[2]) < 7:
        range_days = str(int(l_day) - (7 - int(today_str[2])))
    yesterday = int(today_str[2]) - 1
    if int(today_str[2]) == 1:
        yesterday = l_day
        month = str(int(month) - 1)
    if len(month) == 1:
        month = '0' + month
    if len(str(l_month)) == 1:
        l_month = '0' + str(l_month)
    if len(str(yesterday)) == 1:
        yesterday = '0' + str(yesterday)

    return l_day, l_month, range_days, year, month, yesterday


print(last_day_of_last_month())
