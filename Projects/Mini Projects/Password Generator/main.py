# Importing required libraries
import string
import secrets

# Initializing character sets for lowercase letters, uppercase letters, digits, and symbols
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

# Creating function for generating password
def generate(length=12, lower=True, upper=True, number=True, punctuation=True):
    # Initializing character set
    char_set = ''
    
    # Including lowercase letters if specified
    if lower:
        char_set += lowercase_letters
    
    # Including uppercase letters if specified
    if upper:
        char_set += uppercase_letters
    
    # Including punctuation symbols if specified
    if punctuation:
        char_set += symbols
    
    # Including digits
    if digits:
        char_set += digits

    # Generating password by selecting characters randomly from the character set
    password = ''.join([secrets.choice(char_set) for _ in range(length)])
    return password

if __name__ == "__main__":
    # Generating a password using the generate function
    password = generate()
    
    # Printing the generated password
    print('Your password is:', password)