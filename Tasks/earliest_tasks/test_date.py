
year = int()
month = int()
day = int()
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


'''if chexk > 0 <= 31:
    print('yes')
else:
    print('no')'''

def hi_year(year):
    if len(str(year)) == 4 and str(year).isnumeric():
        x = year / 4
        y = year/100
        if x == int(x) and y != int(y):
            hi_year = True
        else:
            z = year / 400
            if z == int(z):
                hi_year = True
            else:
                hi_year = False

        return hi_year
    else:
        print("You need specify 4 number!!!")

def month_real(month):
    if month > 0 and month < 13:
        months = True
    else:
        months = False
    return months


def days_real(days: int, month: int, year: int):
    if month_real(month) and month_real(month) != 2:
        if day_of_month[days] > 0 and day_of_month[days] < 32:
            existing_day = True
        elif month_real(month) and month_real(month) == 2:
            if hi_year(year) and day_of_month[days] < 29:
                existing_day = True
            else:
                existing_day = False
        else:
            print("You need specify one number!!!")
    else:
        existing_day = False
        return existing_day


print(days_real(1,1,2016))
print(month_real(1))
#print(hi_year(2015))
#print(day_of_month[1] == 30)