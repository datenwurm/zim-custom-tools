import os
import sys

###############################################################################
# Author: Thomas Engel <thomas.engel.web@gmail.com>
# Name: sort-desc
# Description: Sorts selected text in descending order
# Command: sort-desc.py "%t"
# Icon: <the path to the icon>
# [ ] Command does not modify data
# [X] Output should replace current selection
# [ ] Show in the toolbar
###############################################################################

if len(sys.argv) < 2:
    # No arguments to compute ...
    sys.exit(1)

input = sys.argv[1]

try:
    # Transform input here ...
    output = os.linesep.join(sorted(input.splitlines(), reverse=True))
    print(output, end='')
except:
    # Return the input in case of an error ...
    print(input, end='')
