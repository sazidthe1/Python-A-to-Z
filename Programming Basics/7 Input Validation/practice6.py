# This is for Practice - Input Validation
'''
# Input validation code checks that values entered by the user, such as text from the input() function.

while True:
    print('Enter your age:')
    age = input()
    try:
        age = int(age)
    except:
        print('Please use numeric digits.')
        continue
    if age < 1:
        print("Age can't be a negative number.")
        continue
    break

print(f'Your age is {age} years old.')

# The PyInputPlus Module
import pyinputplus as pyip
response = pyip.inputNum('Enter a number: ')
print(response)

# The min, max, greaterThan, and lessThan Keyword Arguments
import pyinputplus as pyip
response = pyip.inputNum('Enter num: ', min=4)  # min value
print(response)

response = pyip.inputNum('Enter num: ', greaterThan=4)  # max value
print(response)

# The blank Keyword Argument
import pyinputplus as pyip
response = pyip.inputNum('Enter num: ')
print(response)

response = pyip.inputNum(blank=True)    # blank is True
print(response)
'''