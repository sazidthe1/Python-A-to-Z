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