'''
# This is the practice code
'''
# Finding Patterns of Text Without Regular Expressions
from phoneNumber import isPhoneNumber

message = 'Call me at 417-222-1101 tomorrow. 417-333-9999 is my office'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')