# This is for Practice - Reading & Writing Files

'''
# Files and File Paths
A file has two key properties: a filename and a path. 
The path specifies the location of a file on the computer. For example, project.docx in the path C:\Users\Al\Documents.

from pathlib import Path
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(Path(r'C:\Users\Al', filename))

# Output would be
# C:\Users\Al\accounts.txt
# C:\Users\Al\details.csv
# C:\Users\Al\invite.docx
    
# Using the / Operator to Join Paths
homeFolder = r'C:\Users\Al'
subFolder = 'spam'
homeFolder + '\\' + subFolder
'\\'.join([homeFolder, subFolder])

homeFolder = Path('C:/Users/Al')
subFolder = Path('spam')
homeFolder / subFolder

# The Current Working Directory
from pathlib import Path
import os
Path.cwd()  # Output: WindowsPath('C:/Users/Al/AppData/Local/Programs/Python/Python37')'

os.chdir('C:\\Windows\\System32')
Path.cwd()  # Output: WindowsPath('C:/Windows/System32')

# The Home Directory
Path.home() # Output: WindowsPath('C:/Users/Al')


# Finding File Sizes and Folder Contents
i. file size = os.path.getsize(path), will return the size in bytes of the file 

Example:
os.path.getsize('C:\\Windows\\System32\\calc.exe')
>> 27648

ii. folder contents = os.listdir(path), will return a list of filename strings for each file

Example:
os.listdir('C:\\Windows\\System32')
>> ['0409', '12520437.cpx', '12520850.cpx', '5U877.ax', 'aaclient.dll', 'xwtpdui.dll', 'xwtpw32.dll', 'zh-CN', 'zh-HK', 'zh-TW', 'zipfldr.dll']

# Opening Files with the open() Function
- The open() function will pass it a string path indicating the file we want to open.

Example:
helloFile = open(Path.home() / 'hello.txt')
>> helloFile = open('C:\\Users\\documents\\hello.txt')

# Reading the Contents of Files
- The read() function will read the entire contents of a file as a string value.

Example:
helloContent = helloFile.read()
print(helloContent)
>> 'Hello, World!'

# Writing to Files
- Pass 'w' as the second argument to open() to open the file in write mode.

Example:
helloFile = open('hello.txt', 'w')
helloFile = write('Hello, World!\n) # Add the text in the file
helloFile.close()
content = helloFile.read()  # Read the file
print(content)
>> Hello, World!


# Practice Questions

Q1. What is a relative path relative to?
Ans: Relative path is relative to the current working directory.

Q2. What does an absolute path start with?
Ans: Absolute path starts with the root directory.

Q3. What does Path('C:/Users') / 'Al' evaluate to on Windows?
Ans: Path('C:/Users') / 'Al' evaluates to 'C:/Users/Al'.

Q4. What does 'C:/Users' / 'Al' evaluate to on Windows?
Ans: 'C:/Users' / 'Al' raises a TypeError.

Q5. What do the os.getcwd() and os.chdir() functions do?
Ans: os.getcwd() gets the current working directory & os.chdir() changes the current working directory.

Q6. What are the . and .. folders?
Ans: '.' refers to the current directory, '..' refers to the parent directory.

Q7. In C:\meals\eggs\spam.txt, which part is the dir name, and which part is the base name?
Ans: 'C:\meals\eggs' is the dir name, 'spam.txt' is the base name.

Q8. What are the three “mode” arguments that can be passed to the open() function?
Ans: 'r' for read, 'w' for write, 'a' for append.

Q9. What happens if an existing file is opened in write mode?
Ans: Opening in write mode truncates the file, erasing its contents.

Q10. What is the difference between the read() and readlines() methods?
Ans: read() reads the entire file as a single string, readlines() reads lines into a list.

Q11. What data structure does a shelf value resemble?
Ans: A shelf value resembles a dictionary.
'''