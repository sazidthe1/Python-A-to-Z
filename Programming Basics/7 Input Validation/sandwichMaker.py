# This is Sandwich Maker Project

import pyinputplus as pyip

# Prices for each item
prices = {
    'wheat': 1.0,
    'white': 1.0,
    'sourdough': 1.5,
    'chicken': 2.0,
    'turkey': 2.0,
    'ham': 1.5,
    'tofu': 2.5,
    'cheddar': 0.5,
    'Swiss': 0.5,
    'mozzarella': 0.5,
    'mayo': 0.25,
    'mustard': 0.25,
    'lettuce': 0.5,
    'tomato': 0.5
}

# Ask for bread type
bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt='Select a bread type: ')

# Ask for protein type
protein = pyip.inputMenu(['chicken', 'turkey', 'tofu'], prompt='Select a protein type: ')

# Ask if they want cheese
want_cheese = pyip.inputYesNo('Do you want cheese? (Yes/No): ')

cheese = 0
if want_cheese == 'yes':
    cheese = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], prompt='Select a cheese type: ')

# Ask if they want additional items
want_mayo = pyip.inputYesNo('Do you want mayo? (Yes/No): ')
want_mustard = pyip.inputYesNo('Do you want mustard? (Yes/No): ')
want_lettuce = pyip.inputYesNo('Do you want lettuce? (Yes/No): ')
want_tomato = pyip.inputYesNo('Do you want tomato? (Yes/No): ')

# Ask how many sandwiches
num_sandwiches = pyip.inputInt('How many sandwiches do you want? (Enter a number): ', min=1)

# Calculate total cost
total_cost = prices[bread] + prices[protein]

if want_cheese == 'yes':
    total_cost += prices[cheese]

total_cost += prices['mayo'] * (1 if want_mayo == 'yes' else 0) + \
    prices['mustard'] * (1 if want_mustard == 'yes' else 0) + \
    prices['lettuce'] * (1 if want_lettuce == 'yes' else 0) + \
    prices['tomato'] * (1 if want_tomato == 'yes' else 0)

# Multiply by the number of sandwiches
total_cost *= num_sandwiches

print(f"Your total cost for {num_sandwiches} sandwiches is: $ {total_cost:.2f}")