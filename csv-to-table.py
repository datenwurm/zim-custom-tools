import csv
import sys

###############################################################################
# Author: Thomas Engel <thomas.engel.web@gmail.com>
# Name: csv-to-table
# Description: Transforms csv input to zim wiki table
# Command: csv-to-table.py "%t"
# Icon: <the path to the icon>
# [ ] Command does not modify data
# [X] Output should replace current selection
# [ ] Show in the toolbar
###############################################################################

if len(sys.argv) < 2:
    # No arguments to compute ...
    sys.exit(1)

input = sys.argv[1]

def max_col_len(lines, col):
    return max([len(line[col]) for line in lines])

try:
    # Transform input here ...
    lines = list(csv.reader(input.splitlines()))
    csv_col_len = len(list(lines)[0])
    csv_row_len = len(list(lines))
    max_col_len_list = [max_col_len(lines, col) for col in range(csv_col_len)]
    is_first_line = True
    for row in lines:
        for col in range(csv_col_len):
            print('| ' + row[col].ljust(max_col_len_list[col]) + ' ', end='')
        print('|')
        if is_first_line:
            for col in range(csv_col_len):
                print('|:' + ('-' * max_col_len_list[col]) + '-', end='')
            print('|')
            is_first_line = False
except Exception as e:
    # Return the input in case of an error ...
    print(input, end='')
