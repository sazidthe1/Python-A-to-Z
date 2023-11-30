# Functions
'''
built-in functions = print(), input(), len()
coutom functions = created by myself
'''
# Defining the fuunction
def hello():
    print('Hi!')
    print('Hello.')
    print('Hi there!')

hello()     # Calling the function

# def Statements with Parameters
'''
def hello(name):
    print(f'Hello, {name}!')

hello('World')
hello('Sky')
'''

# Define, Call, Pass, Argument, Parameter
'''
def sayHello(name):
    print(f'Hello, {name}!')
sayHello('Sazid')
'''

# The None Value
'''
spam = print('Hello!')
print(None == spam)
'''

# Keyword Arguments and the Print() Function
'''
print('Hello')
print('World')

print('Hello', end='')
print('World')

print('cats', 'dogs', 'mice')
print('cats', 'dogs', 'mice', sep='; ')
'''

# Local and Global Scope
'''
def spam():
    eggs = 31337
spam()
print(eggs)
'''

# Local Scopes Cannot Use Variables in Other Local Scopes
'''
def spam():
    eggs = 99
    chicken()
    print(eggs)

def chicken():
    meat = 101:
    eggs = 0

spam()
'''
# Global Variables Can Be Read from a Local Scope
'''
def spam():
    print('eggs')
eggs = 42
spam()
print(eggs)
'''

# Local and Global Variables with the Same Name
'''
def spam():
    eggs = 'spam local'
    print(eggs)     # prints 'spam local'

def chicken():
    eggs = 'chicken local'
    print(eggs)
    spam()
    print('eggs')       # prints 'chicken local'

eggs = 'global'
chicken()
print(eggs)     # prints 'global'
'''

# The global statement
'''
def spam():
    global eggs
    eggs = '1 dozen'

eggs = 'global'
spam()
print(eggs)
'''

'''
def spam():
    global eggs
    eggs = 'spam'       # this is the global

def chicken():
    eggs = '1 dozen'    # this is the local

def eggs():
    print(eggs)     # this is the global

eggs = 24       # this is the global
spam()
print(eggs)
'''

'''
def spam():
    eggs = '1 dozen'
    print(eggs)

eggs = 'global'
spam()
'''

# Exception Handling
'''
def spam(divideBy):
    return 42 / divideBy

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
'''

'''
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
'''

'''
def spam(divideBy):
    return 42 / divideBy

try:    
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
        print('Error: Invalid argument.')
'''

# Practice Project

def collatz(number):
    print(number)       # Print the initail number

    while number != 1:      # Continue until the sequence reaches 1
        if number % 2 == 0:
            number = number // 2
    
        else:
            number = 3 * number + 1
        print(number)       # Print the next number in the sequence

while True:
    try:        # Ask for user input
        number = int(input('Enter your number: '))

        # Call the function
        collatz(number)
        break       # Break out

    except ValueError:
        print('You must enter an integer. Try again.')