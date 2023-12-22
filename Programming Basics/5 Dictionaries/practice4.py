'''
# This is for practice

myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

print(type(myCat))
print(len(myCat))

# key: size, color, disposition
# value: fat, gray, loud

print(myCat['size'])    # Accessing the value
print('My cat has ' + myCat['color'] + ' fur.')

# The keys(), values(), and items() Methods

spam = {'color': 'red', 'age': 42}
for i in spam.values():
    print(i)

for j in spam.keys():
    print(j)

for k in spam.items():
    print(k)

spam = {'color': 'red', 'age': 42}
for l, m in spam.items():
    print('Key: ' + l + ' Value: ' + str(m))


# The get() Method
picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')

# The setdefault() Method
spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'

spam = {'name': 'Pooka', 'age': 5}
print(spam.setdefault('color', 'black'))


# Nested Dictionaries and Lists
allGuests = {'Alice': {'apples': 3, 'pretzels': 12},
             'Bob': {'sandwiches': 2, 'apples': 2},
             'Carol': {'cups': 4, 'apple pies': 0},
             'David': {'cakes': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Sandwiches     ' + str(totalBrought(allGuests, 'sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))
'''

# Practice Questions
