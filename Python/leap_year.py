# Problem Statement : Determine whether a given year is a leap year.
'''
If a year is divisible by 4, it is a leap year.
However, if that year is divisible by 100, it is not a leap year, unless…
It is also divisible by 400, in which case, it is a leap year.
'''

# My Solution

try:
    year = int(input("Enter a year:"))
    if 1900 <= year <= 2100:
        if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
            print("This is a Leap Year")
        else:
            print("This is a not a Leap Year")
    else:
        print("Year must be between 1900 and 2100.")
except:
    print("Invalid Input")

# My Approach
'''
- User inputs a year.
- Verify if the year meets the leap year condition:
    - Divisible by 400, OR
    - Divisible by 4 but not by 100.
- If yes → return Leap Year, else → return Not a Leap Year.
'''

# Complexity Analysis
'''
- Time: O(1) → constant checks.
- Space: O(1).
'''

# Source : PCEP Python Essentials 1 Module


