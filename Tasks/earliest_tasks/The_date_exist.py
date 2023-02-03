day_of_month = dict({1 : 31,
2 : 28,
3 : 31,
4 : 30,
5 : 31,
6 : 30,
7 : 31,
8 : 31,
9 : 30,
10 : 31,
11 : 30,
12 : 31})


def high_year(year):
    if len(str(year)) == 4 and str(year).isnumeric():
        x = year % 4
        y = year % 100
        if x == 0 and y != 0:
            hi_year = True
        else:
            z = year % 400
            if z == 0:
                hi_year = True
            else:
                hi_year = False

        return hi_year
    else:
        print("You need specify 4 number!!!")


def month_real(month):
    if month > 0 and month < 13:
        month = True
    else:
        month = False
    return month


def days_real(day):
    if day > 0 and day < 32:
        day = True
    else:
        day = False
    return day


def data_real(day: int, month: int, year: int):
    if days_real(day) == True and month_real(month) == True and month != 2 and day <= int(day_of_month[month]):
        existing_day = 'YES the date is real'
    elif days_real(day) == True and month_real(month) == True and month == 2:
        if high_year(year) == True and day <= int(day_of_month[2]+1):
            existing_day = 'YES the date is real'
        else:
            existing_day = 'NO the date is not real'
    else:
        existing_day = 'NO the date is not real'
    return existing_day


print(data_real(29,2,2020))
print(data_real(32,12,2017))
print(data_real(7,0,2026))
print(data_real(29,2,1700))