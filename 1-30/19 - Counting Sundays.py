"""
Problem 19 - Counting Sundays
-------------------------------------------------------------------------------
You are given the following information, but you may prefer to do some research for yourself.
```
1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
```
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november',
          'december']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
days_in_month = {
    months[0]: 31,
    months[1]: 28,
    months[2]: 31,
    months[3]: 30,
    months[4]: 31,
    months[5]: 30,
    months[6]: 31,
    months[7]: 31,
    months[8]: 30,
    months[9]: 31,
    months[10]: 30,
    months[11]: 31,
}


# ---------------- Helper Functionns -----------------
def checkLeapYear(year):
    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True

    return False


def checkSetLeapYear(year):
    if (checkLeapYear(year)):
        days_in_month['february'] = 29


def checkUnSetLeapYear(year):
    if (checkLeapYear(year)):
        days_in_month['february'] = 28


def getCurrentDay(offset_days):
    return total_day_offset % 7


# ---------------- Start Problem -----------------
total_day_offset = 0
start_year = 1900
end_year = 2000
year_offset = 0

# Travel to 1/1/1901
if checkLeapYear(start_year):
    total_day_offset += 1

total_day_offset += 365
year_offset = 1

# Get Day
sunday_sum = 0
while (start_year + year_offset) <= end_year:

    checkSetLeapYear(start_year + year_offset)
    print("Year: " + str(start_year + year_offset))
    for month in months:
        curr_day = getCurrentDay(total_day_offset)
        print("Month: " + month)
        print("Day: " + days[curr_day])

        if (days[curr_day] == 'sunday'):
            sunday_sum += 1

        total_day_offset += days_in_month[month]

    checkUnSetLeapYear(start_year + year_offset)

    print("Sunday Sum: " + str(sunday_sum))
    year_offset += 1

# For every month until stop date check if val%7 == 6
print(days[curr_day])
