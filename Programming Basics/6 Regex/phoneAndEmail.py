# Step 1: Create a Regex for Phone Numbers

import pyperclip
import re

# Provided text (Copied from nostarch.com/contactus)
text = '''
Reach Us by Email - email is the best way to reach us
Help with your order: support@nostarch.com
Academic requests: academic@nostarch.com (Further information)
Bulk and special sales questions: sales@nostarch.com
Conference and event inquiries: conferences@nostarch.com
Errata - please send any errata reports to: errata@nostarch.com
General inquiries: info@nostarch.com
Media requests: media@nostarch.com
Proposals or editorial inquiries: editors@nostarch.com
Rights inquiries: rights@nostarch.com (Further information)
Reach Us by Mail
Mailing Address

No Starch Press
329 Primrose Road,  #42
Burlingame, CA 94010-4093
USA

Principal Place of Business

No Starch Press, Inc.
245 8th Street
San Francisco, CA 94103
USA

NOTE: Below are our business phone numbers but we are a completely remote company. Please email support@nostarch.com with your questions and we will do our best to promptly resolve any issues that you may have.

Phone: 800.420.7240 or +1 415.863.9900
Fax: +1 415.863.9950

Reach Us on Social Media
Twitter Facebook Instagram Linkedin Pinterest
'''

# Regular expressions for phone numbers and email addresses
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

# Step 2: Create a Regex for Email Addresses
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
    )''', re.VERBOSE)


# Step 3: Find All Matches in the Clipboard Text
# Find matches in the provided text
matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Step 4: Join the Matches into a String for the Clipboard
# Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')