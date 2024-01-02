# This is Strong Password Detection Project

import re

def strongPassword(password):
    # Check length >= 8, lowercase, uppercase, and digit presence
    lengthRegex = re.compile(r'.{8,}')
    lowercaseRegex = re.compile(r'.[a-z]')
    uppercaseRegex = re.compile(r'[A-Z]')
    digitRegex = re.compile(r'\d')

    # Check if all conditions are not
    hasLength = lengthRegex.search(password)
    hasLowercase = lowercaseRegex.search(password)
    hasUppercase = uppercaseRegex.search(password)
    hasDigit = digitRegex.search(password)

    # Return True only if all conditions are met
    return all([hasLength, hasLowercase, hasUppercase, hasDigit])

# Test the function
password = 'StrongPasswOrd1'
if strongPassword(password):
    print('The password is strong.')
else:
    print('The password is not strong! Try another one.')