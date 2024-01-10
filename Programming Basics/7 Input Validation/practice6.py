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

# The limit, timeout, and default Keyword Arguments
import pyinputplus as pyip
'''
response = pyip.inputNum('Enter num: ', limit=2)
print(response)

response = pyip.inputNum(timeout=10)
print(response)

response = pyip.inputNum(limit=3, default='N/A')    # using default keyword argument
print(response)

# The allowRegexes and blockRegexes Keyword Arguments

import pyinputplus as pyip

#response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M|i|v|x|l|c|d|m)+', r'zero'])   # allowing input
#print(response)

#response = pyip.inputNum(blockRegexes=[r'[02468]$'])  # blocking input
#print(response)

response = pyip.inputStr(allowRegexes=[r'caterpillar', 'category'],
blockRegexes=[r'bat', 'cat', 'hat', 'rat'])
print(response)

# Passing a Custom Validation Function to inputCustom()
import pyinputplus as pyip

def addToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):  # Fixed syntax error here
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.' % sum(numbersList))
    return int(numbers)

response = pyip.inputCustom(addToTen)
print(response)


# Practice Questions
Q1. Does PyInputPlus come with the Python Standard Library?
Ans: No, PyInputPlus is not part of the Python Standard Library, it's a third-party library.

Q2. Why is PyInputPlus commonly imported with import pyinputplus as pyip?
Ans: PyInputPlus is commonly imported as pyip to provide a shorter alias for convenience and brevity in code.

Q3. What is the difference between inputInt() and inputFloat()?
Ans: inputInt() is used to specifically accept integer input, while inputFloat() is used to accept floating-point numbers.

Q4. How can you ensure that the user enters a whole number between 0 and 99 using PyInputPlus?
Ans: To ensure a whole number between 0 and 99, you can use pyip.inputInt(min=0, max=99).

Q5. What is passed to the allowRegexes and blockRegexes keyword arguments?
Ans: The allowRegexes argument accepts a list of regular expressions that are allowed as input, while blockRegexes accepts a list of regular expressions to disallow as input.

Q6. What does inputStr(limit=3) do if blank input is entered three times?
Ans: inputStr(limit=3) raises a TimeoutException after three blank inputs.

Q7. What does inputStr(limit=3, default='hello') do if blank input is entered three times?
Ans: It returns the default value 'hello' after three blank inputs instead of raising a TimeoutException.
'''