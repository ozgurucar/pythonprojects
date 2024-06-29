def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True


year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

days_of_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def days_in_month(month, year):
    if is_leap(year) and month == 2:
        return 29
    else:
        return days_of_months[month]


days = days_in_month(year=year, month=month)
print(f"Days in provided month is: {days}")
