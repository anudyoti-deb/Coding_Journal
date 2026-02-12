# Problem Statement : Given a year, month, and day, calculate how many days have elapsed since the start of that year.

# My Solution
def is_year_leap(year):  # function to check if a year is leap year
    if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
        return True
    else:
        return False


def days_in_month(year, month):  # function to check no. of days in a month
    thirty = [4, 6, 9, 11]
    thirty_one = [1, 3, 5, 7, 8, 10, 12]
    if month == 2:
        if is_year_leap(year) == True:
            return 29
        else:
            return 28
    elif month in thirty:
        return 30
    elif month in thirty_one:
        return 31
    else:
        return None


def day_of_year(year, month, day):
    # first check if the year provided is leap year or not. Based on that days of Feb will be decided.
    if is_year_leap(year) == True:
        feb = 29
    else:
        feb = 28
    total_days = 0  # empty variable to add all days of all the months
    days_in_month = [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # List containing days of months in a year
    month_entered = days_in_month[
        :month - 1]  # another list is created but with a slice restricting the no. of months based on entered month
    # end month is month-1 because last month might have partial days and not complete month
    for days in month_entered:
        total_days += days
    total_days += day  # adding with last month days.
    print("Total days elapsed : ", total_days, "Days")

yyyy = int(input('Enter year'))
mm = int(input('Enter month'))
dd = int(input('Enter day'))

day_of_year(yyyy, mm, dd)

# My Approach
'''
- Leap year check → Use is_year_leap(year) to decide if February has 28 or 29 days.
- Days in each month → Create a list of days for all months, adjusting February based on leap year result.
- Slice months → Take all months before the entered month (:month-1) to sum their days.
- Accumulate days → Add the total days of previous months plus the entered day.
- Output result → Print the total number of elapsed days.
'''

# Complexity Analysis
'''
- Time: O(m), where m = number of months before the given month (at most 12).
- Space: O(1), only storing a fixed list of month lengths
'''

# Source : PCEP Python Essentials 1 Module


