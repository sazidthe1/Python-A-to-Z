# This is Date Detection Project

import re

datePattern = re.compile(r'(0[1-9]|[1-2][0-9]|3[01])/(0[1-9]|1[0-2])/([1-2][0-9]{3})')

dateString = '31/12/2023'

match = datePattern.match(dateString)
if match:
    day = int(match.group(1))
    month = int(match.group(2))
    year = int(match.group(3))

    # Additional code to check if it's a valid date
    validDate = True

    if month in [4, 6, 9, 11] and day > 30:
        validDate = False
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            if day > 29:
                validDate = False
        elif day > 28:
            validDate = False
    elif day > 31:
            validDate = False

    if validDate:
        print('Valid date')
    else:
        print('Invalid date')