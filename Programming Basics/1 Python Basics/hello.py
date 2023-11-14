# This program greets and ask for my name and age
print('Hi there!')
my_name = input('What is your name? ') # Asking for the name
print('Nice to meet you, ' + my_name)

print('The length of your name is:', len(my_name)) 
my_age = input('What is your age? ') # Asking for the age
print('You will be ' + str(int(my_age) + 1) + ' in a year.')