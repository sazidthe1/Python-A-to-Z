# Comparison Operators
'''
Equal to: ==
Not equal to: !=
Less than: <
Greater than: >
Less than or equal to: <=
Greater than or equal to: >=
'''

42 == 42    # True

42 == 49    # False

2 != 3      # True

2 != 2      # False

'hello' == 'hello'      # True

'hello' == 'Hello'      # False

'dog' != 'cat'      # True

True == True        # True

True != False       # True

42 == 42.0      # True

42 == '42'      # False

42 < 100        # True

42 > 100        # False

42 < 42     # True

count = 42
count <= 42

my_age = 29
my_age >= 10


# Boolean Operators
'''
True and True: True
True and False: Flase
False and True: False
False and False: True
'''

True and True       # True

True and False      # False

'''
True or True: True
True or False: True
False or True: True
False or False: False
'''

False or True       # True

False or False      # False


# The not Operator
not True        # False

not not not not True        # True


# Mixing Boolean and Comparison Operators
(4 < 5) and (5 < 6)     # True

(4 < 5) and (9 < 6)     # False

(1 == 2) or (2 == 2)    # True

2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2     # True


# Elements of Flow Control
'''
Conditions: if, elif, else (always evaluate down to Boolean value, True or False)
Block of code: Lines of codes can be grouped together in blocks
'''


# if Statements: an if statement's clause will execute if the statement's clause is True
'''
if name == 'Alice':
    print('Hi, Alice')

# else Statements: the else clause is executed only when the if statement's clause is False
if name == 'Alice':
    print('Hi, Alice')
else:
    print('Hello, stranger.')

# elif Statements: the elif statement is an "else if" statement that always follows an if or another elif statement (while only one of the if ot else clauses will execute)  
name = 'Carl'
age = 33
if name == 'Alice':
    print('Hi, Alice')
elif age < 12:
    print('You are not Alice, kiddo')
elif age > 75:
    print('You are not Alice, grannie')
elif age > 300:
    print('Unlike you, Alice is not an undead, importal, vampire.')
else:
    print('You are not neither Alice nor a little kid.')


name = 'Mary'
password = 'swordfish'
if name == 'Mary':
    print('Hello,', name + '!')
    if password == 'swordfish':
        print('Access granted.')
else:
    print('Wrong password! Try again.')
'''


# while Loop Statements: a while clause will be executed as long as the while statement's condition is True
'''
count = 0
while count < 5:
    print('Hello, World.')
    count += 1

count = 0
if count < 5:
    print('Hello, World.')
    count = count + 1
'''

# break Statements: a break statement helps to break out of a while loop's clause early
'''
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')
'''

# continue Statements: a continue statement helps to jump back to the start of the loop and re-evaluates the loop condition
''' while True:
    print('Hello, World.')
'''

# for Loops and the range() Function
total = 0
for num in range(101):
    total += num
print(total)

print('\n')
# range() Function
for i in range(12, 16):
    print(i)
print('\n')
# range() function with three agruments
for i in range(0, 10, 2):
    print(i)
print('\n')
# range() function with negative numbers
for i in range(5, 0, -1):
    print(i)


# Importing Modules: a module that contains a related group of functions | a set of modules called the standard library
'''
built-in functions: print(), input(), len(), str(), int(), float(), etc.

modules: math, random, datetime, os, requests, json, numpy, pandas, and so on.

To use the functions in a module, we must have import the module using 'import' statement.

Structure looks like: import <name of the module>

To import multiple modules: import <name of the module1>, <name of the module2>, <name of the module3>
'''

