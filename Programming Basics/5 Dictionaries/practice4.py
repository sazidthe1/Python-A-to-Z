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
'''
