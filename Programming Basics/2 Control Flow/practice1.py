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
elif age > 30:
    print('Unlike you, Alice is not an undead, importal, vampire.')


name = 'Mary'
password = 'swordfish'
if name == 'Mary':
    print('Hello,', name + '!')
    if password == 'swordfish':
        print('Access granted.')
else:
    print('Wrong password! Try again.')

print()