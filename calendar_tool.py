from datetime import datetime, timedelta


def get_cal_month(y, m):
    dt = datetime(y, m, 1)
    month = [[], [], [], [], [], [], []]

    mon = month[0]
    mon.append('Mon:')

    tue = month[1]
    tue.append('Tue:')

    wed = month[2]
    wed.append('Wed:')

    thu = month[3]
    thu.append('Thu:')

    fri = month[4]
    fri.append('Fri:')

    sat = month[5]
    sat.append('Sat:')

    sun = month[6]
    sun.append('Sun:')

    wd = dt.weekday()
    if wd > 0:
        for i in range(wd):
            this_weekday = month[i]
            this_weekday.append(' ')
    while dt.month == m:
        this_weekday = month[dt.weekday()]
        this_weekday.append(str(dt.day))
        dt = dt + timedelta(days=1)
    return month


def get_cal_year(y):
    for m in range(1, 13):
        print(datetime.strftime(datetime(y, m, 1), '%B'))
        month = get_cal_month(y, m)

        for i in range(len(month)):
            print('\t'.join(month[i]))


year = datetime.now().year + 1
print('Calendar ', year)
this_year = get_cal_year(year)
print(this_year)
