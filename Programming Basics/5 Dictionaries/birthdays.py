# This is Birthday Project

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input().capitalize()
    
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information of ' + name)
        print('What is their birthday? (e.g., Jan 1)')
        bday = input()
        birthdays[name] = bday
        print('Birthday database is updated.')