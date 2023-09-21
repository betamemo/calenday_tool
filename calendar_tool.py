from datetime import datetime, timedelta


def get_cal_month(y, m, n):
    dt = datetime(y, m, 1)
    month = [[], [], [], [], [], [], []]
    month_str = ''

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

    m_temp = m
    padding_temp = 8

    for x in range(n):

        # Add padding before day 1
        wd = dt.weekday()
        if wd > 0:
            for i in range(wd):
                this_weekday = month[i]
                this_weekday.append(' ')

        # Append month name
        month_str = month_str + (datetime.strftime(dt, '%B')).ljust(36)

        # Add day in month
        while dt.month == m_temp:
            this_weekday = month[dt.weekday()]
            this_weekday.append(str(dt.day))
            dt = dt + timedelta(days=1)
        m_temp = dt.month

        # Add padding between month
        for i in range(len(month)):
            if len(month[i]) < padding_temp:
                for j in range(len(month[i]), padding_temp):
                    month[i].append(' ')
        padding_temp = padding_temp + 8

    print(month_str)
    return month


def get_cal_year(y, n):
    m = 1
    while 1 <= m <= 12:
        month = get_cal_month(y, m, n)
        for i in range(len(month)):
            print('\t'.join(month[i]))
        m = m + n


# Display calendar for the next year
# year = datetime.now().year + 1
# print('Calendar ', year)
# next_year = get_cal_year(year)
# print(next_year)

# Display calendar for the chosen year
# year = input('Enter year: ')
# print('Calendar ', year)
# other_year = get_cal_year(int(year))
# print(other_year)

# Display calendar for the flexible layouts
year = input('Enter year: ')
month_number = input('How many months to display in a single row (1, 2, or 3)?: ')
month_number = int(month_number)
if month_number < 1:
    print('Should greater than or equal 1')
elif month_number > 3:
    print('Should less than or equal 3')
else:
    get_cal_year(int(year), month_number)
