# This is for Practice - Organizing Files

'''
# The shutil Module
- The shutil (or shell utilities) module has functions to let us copy, move, rename, and delete files.

# Copying Files and Folders
- The shutil.copy (source, destination) will copy the file at the path source to the folder at the path destination.

Example:
import shutil, os
from pathlib import Path
p = Path.home()
shutil.copy(p / 'spam.txt', p / 'documents')
>> 'C:\\Users\\Al\\documents\\spam.txt'


# Moving and Renaming Files and Folders
- The shutil.move(source, destination) will move the file or folder at the path source to the path destination and will return a string of the absolute path of the new location.

Example:
import shutil
shutil.move('C:\\meal.txt', 'C:\\eggs')
>> 'C:\\eggs\\meal.txt'

'''