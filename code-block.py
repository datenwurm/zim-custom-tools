import sys

###############################################################################
# Author: Thomas Engel <thomas.engel.web@gmail.com>
# Name: Code Block
# Description: Renders the selected text inside a code block 
# Command: code-block.py "%t"
# Icon: <the path to the icon>
# [ ] Command does not modify data
# [X] Output should replace current selection
# [X] Show in the toolbar
###############################################################################

if len(sys.argv) < 2:
    # No arguments to compute ...
    sys.exit(1)

input = sys.argv[1]

try:
    # Transform input here ...
    print('{{{code: lang="sh" linenumbers="True"')
    print(input)
    print('}}}', end='')
except:
    # Return the input in case of an error ...
    print(input, end='')
