# This is for Practice - Reading & Writing Files

'''
# Files and File Paths
A file has two key properties: a filename and a path. 
The path specifies the location of a file on the computer. For example, project.docx in the path C:\Users\Al\Documents.
'''
from pathlib import Path
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(Path(r'C:\Users\Al', filename))

# Output would be
# C:\Users\Al\accounts.txt
# C:\Users\Al\details.csv
# C:\Users\Al\invite.docx