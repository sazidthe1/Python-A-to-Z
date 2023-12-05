'''
# The Lists data type
[1, 2, 3]
['cat', 'bat', 'rat', 'elephant']
['hello', 3.1415, True, None, 42]
freedom = ['Bangladesh', 16, 'December', 1971]
'''

'''
text = ['I', 'love', 'my', 'country']
print(text[1])
print(text[1:])
print(text[:1])
'''

'''
message = [['Bangladesh', 'is', 'my', 'homeland'], ['I', 'love', 'homeland']]
print(message[1][0])
print(message[1][1])
print(message[0][0])
print(message[0][0])
print(message[0][1])
print(message[0][2])
print(message[1][1])
'''

'''
# Negative Indexes
animal = ['cat', 'bat', 'rat', 'elephant']
print(animal[-1])
print(animal[-3])
'''

'''
# Getting a List from Another List with Slices
animal = ['cat', 'bat', 'rat', 'elephant']
print(animal[0:3])
print(animal[1:3])
print(animal[0:-1])
print(animal[:2])
print(animal[1:])
print(animal[:])
'''

'''
# Getting a List's Length with the len() Function
animal = ['cat', 'bat', 'rat', 'elephant']
print(len(animal))
'''

'''
# Changing Values in a List with Indexes
animal = ['cat', 'bat', 'rat', 'elephant']
animal[1] = 'cow'
print(animal)
animal[2] = animal[1]
animal[-1] = 911
print(animal)
'''

'''
# List Concatenation and List Replication
merged = [1, 2, 3] + ['A', 'B', 'C']
print(merged)
print(['A', 'B', 'C'] * 3)
group1 = [1, 2, 3]
group2 = group1 + ['A', 'B', 'C']
print(group2)
'''

'''
# Removing Values from Lists wuth del Statements
animal = ['cat', 'bat', 'rat', 'elephant']
del animal[3]
print(animal)
del animal[2]
print(animal)

# Working with Lists
catName1 = 'Zophie'
catName2 = 'Pooka'
catName3 = 'Simon'
catName4 = 'Lady'
catName5 = 'Nocila'
catName6 = 'Celo'
'''

'''
# Using for Loops with Lists
for i in range(4):
    print(i)

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
'''

'''
# Using the random.choice() with Lists
import random
pets = ['Bat', 'Cat', 'Rat']
print(random.choice(pets))

# Using the random.shuffle Functions with Lists
import random
people = ['Alice', 'Bob', 'Carol', 'David']
random.shuffle(people)
print(people)
'''

'''
# Methods
# Finding a Value in a List with the index() Method
greetings = ['hello', 'hi', 'howdy', 'heyas']
print(greetings.index('hi'))
print(greetings.index('heyas')) 

# Adding Values to List with the append() Method
animal = ['bat', 'cat', 'rat']
animal.append('ocelot')
print(animal)

# Adding Values to List with the index() Method
animal = ['bat', 'cat', 'rat']
animal.insert(2, 'platypus')
print(animal)

# Removing Values from List with the remove() Method
animal = ['bat', 'cat', 'rat', 'platypus']
animal.remove('platypus')
print(animal)

# Sorting the Values in a List with the sort() Method
number = [9, 3, -1, -5, 0]
number.sort()
print(number)

# Reversing the Values in a List with the reverse() Method
animal = ['bat', 'cat', 'rat']
animal.reverse()
print(animal)
'''

'''
# Sequence Data Types
name = 'Zophie'
#print(name[0])

for i in name:
    print('*** ' + i + ' ***')

# Mutable and Immutable Data Types
name = 'Zophie is a cat.'
article = 'the'
newName = name[:10] + article + name[11:]
print(newName)
'''

'''
# The Tuple Data Type
eggs = ('hello', 42, 0.5)
print(eggs[0])
print(eggs[1:3])
print(len(eggs))

# Coverting Types with the list() and tuple Functions
tuple = tuple(['bat', 'cat', 5])
print(tuple)
list = list(('bat', 'cat', 5))
print(list)

# References
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[0] = 'hello'
print(spam)
'''

'''
# Identity and the id() Function
print(id('Hi'))
print(id('Hello'))
print(id('Howdy'))

eggs = ['bat', 'cat']
print(id(eggs))
eggs.append('rat')
print(id(eggs))
'''
'''
# Passing References
def eggs(someParameter):
    someParameter.insert(0, 'Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

# The copy Module's copy() and deepcopy() Functions
import copy
spam = ['A', 'B', 'C', 'D']
print(id(spam))

cheese = copy.copy(spam)
id(cheese)
'''