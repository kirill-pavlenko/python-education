'''
Exercise
In this exercise, you will need to print an alphabetically sorted list of all
functions in the re module, which contain the word find.
'''

import re

# Your code goes here
find_functions = []
for func in dir(re):
    if "find" in func:
        find_functions.append(func)

print(sorted(find_functions))
