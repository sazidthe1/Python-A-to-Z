# Tip Calculator App
food_amount = float(input('Enter food amount $: '))
tip_percentage =  float(input('Enter your tip percentage %: ')) / 100
tip_amount = food_amount * tip_percentage # Getting the tip amount
total = food_amount + tip_amount # Getting the total amount
print('--------------------------------')
print(f'🍜 Food Amount ${food_amount}')
print(f'📝 Tip Amount: ${tip_amount}')
print('\n')
print(f'💵 Total Amount: ${total}')
print('--------------------------------')