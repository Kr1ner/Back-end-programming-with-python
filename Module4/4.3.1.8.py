import math
def is_year_leap(year):
    if year%400==0 and year%100==0:
        return True
    elif year%4==0 and year%100!=0:
        return True
    else:
        return False

def days_in_month(year, month):
    if month > 12 or month <1:
        return None
    return 28 + (month + math.floor(month/8)) % 2 + 2 % month + 2 * math.floor(1/month) + ((month==2)*is_year_leap(year))



def day_of_year(year, month, day):
    count = 0
    for i in range(1,month):
        eachday = days_in_month(year,month)
        count+=eachday
    return count + day

print(day_of_year(2000, 12, 31))
