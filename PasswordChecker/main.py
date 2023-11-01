# Opening the password file in read mode
password_file = open('secret_password.txt', 'r')

# Reading the secret password from the file
secret_password = password_file.read()

# Closing the file after reading
password_file.close()

# Prompting the user to enter a password
print('Enter your password:')

# Reading the typed password from user input
type_password = input()

# Checking if the entered password matches the secret password
if type_password == secret_password:
    print('✅ Access Granted')
elif type_password == '12345':
    print('That password is one that an idiot puts on their luggage 😑')
else:
    print('❌ Access Denied. Please try again')