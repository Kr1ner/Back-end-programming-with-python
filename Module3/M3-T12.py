def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def get_month_days(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return 30

def get_first_day_of_month(year, month):
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    day_of_week = (1 + (13 * (month + 1)) // 5 + k + (k // 4) + (j // 4) - (2 * j)) % 7
    return (day_of_week + 5) % 7 + 1  # Adjust the result

user_input = input("Input month of calendar as mm-yyyy: ")
month = int(user_input.split("-")[0])
year = int(user_input.split("-")[1])

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
weekdays = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

print(f'{months[month-1]} {year}'.center(20))
print(" ".join(weekdays))

starting_day = get_first_day_of_month(year, month)

print('   ' * (starting_day - 1), end='') 

for day in range(1, get_month_days(year, month) + 1):
    print(f"{day:2d} ", end='') 
    if (day + starting_day - 1) % 7 == 0: 
        print()
print()
