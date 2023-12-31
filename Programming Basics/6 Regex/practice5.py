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

# Matching Everything with Dot-Star
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

# Matching Newlines with the Dot Character
noNewlineRegex = re.compile('.*')
mo = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(mo)

newlineRegex = re.compile('.*', re.DOTALL)
mo1 = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(mo1)

# Review of Regex Symbols
- The ? matches zero or one of the preceding group.
- The * matches zero or more of the preceding group.
- The + matches one or more of the preceding group.
- The {n} matches exactly n of the preceding group.
- The {n,} matches n or more of the preceding group.
- The {,m} matches 0 to m of the preceding group.
- The {n,m} matches at least n and at most m of the preceding group.
- {n,m}? or *? or +? performs a non-greedy match of the preceding group.
- ^spam means the string must begin with spam.
- spam$ means the string must end with spam.
- The . matches any character, except newline characters.
- \d, \w, and \s match a digit, word, or space character, respectively.
- \D, \W, and \S match anything except a digit, word, or space character, respectively.
- [abc] matches any character between the brackets (such as a, b, or c).
- [^abc] matches any character that isn’t between the brackets.

# Case-Insensitive Matching
robocop = re.compile(r'robocop', re.I)
cop1 = robocop.search('RoboCop is part man, part machine, all cop.').group()
print(cop1)
cop2 = robocop.search('ROBOCOP protects the innocent.').group()
print(cop2)
cop3 = robocop.search('Al, why does your programming book talk about robocop so much?').group()
print(cop3)

# Substituting Strings with the sub() Method
namesRegex = re.compile(r'Agent \w+')
name = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(name)

agent = agentNamesRegex = re.compile(r'Agent (\w)\w*')
agentName = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(agentName)

# Managing Complex Regexes
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

or 

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

# Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
'''

'''
# Practice Questions

Q1. What is the function that creates Regex objects?
Ans: re.compile()

Q2. Why are raw strings often used when creating Regex objects?
Ans: r''

Q3. What does the search() method return?
Ans: search() returns the first Match object found.

Q4. How do you get the actual strings that match the pattern from a Match object?
Ans: group() method retrieves matched strings from a Match object.

Q5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 1? Group 2?
Ans: Group 0: Entire match. Group 1: First set of parentheses. Group 2: Second set of parentheses.

Q6. Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?
Ans: To match parentheses or periods, escape them with a backslash: \( for parentheses and \. for periods.

Q7. The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other?
Ans: findall() returns a list of strings when there are no capture groups, and a list of tuples when there are capture groups.

Q8. What does the | character signify in regular expressions?
Ans: | signifies an OR operation in regex.

Q9. What two things does the ? character signify in regular expressions?
Ans: ? signifies optional or non-greedy behavior.

Q10. What is the difference between the + and * characters in regular expressions?
Ans: + matches one or more occurrences, while * matches zero or more occurrences.

Q11. What is the difference between {3} and {3,5} in regular expressions?
Ans: {3} matches exactly three occurrences, while {3,5} matches between three to five occurrences.

Q12. What do the \d, \w, and \s shorthand character classes signify in regular expressions?
Ans: \d matches digits, \w matches word characters, and \s matches whitespace characters.

Q13. What do the \D, \W, and \S shorthand character classes signify in regular expressions?
Ans: \D matches non-digits, \W matches non-word characters, and \S matches non-whitespace characters.

Q14. What is the difference between .* and .*??
Ans: .* matches greedily, while .*? matches non-greedily.

Q15. What is the character class syntax to match all numbers and lowercase letters?
Ans: [0-9a-z] matches all numbers and lowercase letters.

Q16. How do you make a regular expression case-insensitive?
Ans: Use the re.IGNORECASE flag or (?i) at the start of the regex pattern.

Q17. What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile()?
Ans: . matches any character except newline. With re.DOTALL, it matches any character including newline.

Q18. If numRegex = re.compile(r'\d+'), what will numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?
Ans: X drummers, X pipers, five rings, X hens.

Q19. What does passing re.VERBOSE as the second argument to re.compile() allow you to do?
Ans: Allows comments and whitespace within the pattern for readability.

Q20. How would you write a regex that matches a number with commas for every three digits? It must match the following:
'42'
'1,234'
'6,368,745'
but not the following:

'12,34,567' (which has only two digits between the commas)
'1234' (which lacks commas)

Ans: r'^\d{1,3}(,\d{3})*$'
'''