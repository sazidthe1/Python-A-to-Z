'''
# This is the practice code

# Finding Patterns of Text Without Regular Expressions
from phoneNumber import isPhoneNumber

message = 'Call me at 417-222-1101 tomorrow. 417-333-9999 is my office'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')


# Finding Patterns of Text with Regular Expressions
# Creating Regex Objects
import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242')  # Matching Regex Objects
print('Phone number found: ' + mo.group())

# Grouping with Parentheses
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())


# Matching Multiple Groups with the Pipe
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

import re
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group)
print(mo.group(1))

# Optional Matching with the Question Mark
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())
mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())

# Matching Zero or More with the Star
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())

# Matching One or More with the Plus
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None)

# Matching Specific Repetitions with Braces
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
mo2 = haRegex.search('Ha')
print(mo2 == None)

# Greedy and Non-greedy Matching
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())

# The findall() Method
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999; Work: 212-555-0000')
print(mo.group())
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
mo1 = phoneNumRegex.findall('Cell: 415-555-9999; Work: 212-555-0000')
print(mo1)


# Character Classes
# Shorthand character class: Represents

\d: Any numeric digit from 0 to 9.

\D: Any character that is not a numeric digit from 0 to 9.

\w: Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)

\W: Any character that is not a letter, numeric digit, or the underscore character.

\s: Any space, tab, or newline character. (Think of this as matching “space” characters.)

\S: Any character that is not a space, tab, or newline.

shoppingRegex = re.compile(r'\d+\s\w+')
mo2 = shoppingRegex.findall('7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 chicken')
print(mo2)
'''
import re
# Making Your Own Character Classes
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowels = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(vowels)

# Making Your Own Character Classes
vowelRegex = re.compile(r'[^aeiouAEIOU]')
vowels1 = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(vowels1)

# The Caret and Dollar Sign Characters
beginsWithHello = re.compile(r'^Hello')
hello = beginsWithHello.search('Hello, world!')
print(beginsWithHello.search('He said hello.') == None)

endsWithNumber = re.compile(r'\d$')
endsWithNumber.search('Your number is 42')
print(endsWithNumber.search('Your number is forty two.') == None)

wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('1234567890')
print(wholeStringIsNum.search('12345xyz67890') == None)
print(wholeStringIsNum.search('12  34567890') == None)

# The Wildcard Character
atRegex = re.compile(r'.at')
wildcard = atRegex.findall('The cat in the hat sat on the flat mat.')
print(wildcard)
