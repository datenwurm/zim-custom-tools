import sys

###############################################################################
# Author: Author <author@example.com>
# Name: <the name of the custom tool>
# Description: <the description of the custom tool>
# Command: <the command used to execute the custom tool>
# Icon: <the path to the icon>
# [ ] Command does not modify data
# [ ] Output should replace current selection
# [ ] Show in the toolbar
###############################################################################

if len(sys.argv) < 2:
    # No arguments to compute ...
    sys.exit(1)

input = sys.argv[1]

try:
    # Transform input here ...
    output = input
    print(output, end='')
except:
    # Return the input in case of an error ...
    print(input, end='')
