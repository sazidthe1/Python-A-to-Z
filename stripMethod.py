# This is strip() Method Project

import re

def regexStrip(text, chars=None):
    if chars is None:
        # Remove whitespace from the beginning and end of the string
        return re.sub(r'^\s+|\s+$', '', text)
    else:
        # Escape characters for regex and remove from the beginning and end of the string
        chars = re.escape(chars)
        return re.sub(f'^[{chars}]+|[{chars}]+$', '', text)
    
# Test the function
text = '   Hi there!   '
print(regexStrip(text))     # Output: 'Hi there!

textWithChars = '**Hi!**'
print(regexStrip(textWithChars, '*'))   # Output: Hello!