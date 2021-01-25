# zim-custom-tools

This repository contains a collection of custom tools for zim.

## Overview

Name | Description
--- | ---
code-block.py | Transforms the selected text to a code block
csv-to-table.py | Transforms the selected comma separated text into a table 
gnome-screenshot-area.py | Takes a screenshot of an area
gnome-screenshot-interactive.py | Takes a screenshot
gnome-screenshot-window.py | Takes a screenshot of a selected window
lower.py | Transforms the selected text into lower case
sort-asc.py | Sorts the selected text in ascending order
sort-desc.py | Sorts the selected text in descending order
title.py | Transforms the selected text into title case
upper.py | Transforms the selected text into upper case

## Troubleshooting

### Issue 1 - No output

**Description:**

When executing the script via zim custom tools no output is returned.

**Solution:**

Double-check the path to the script. Zim does not notify if the script is not found.

### Issue 2 - The generated output is not rendered 

**Description:**

Some scripts generate output in zim markup language. However, the output is not rendered by zim.

**Solution:**

You need to reload the page e.g. by pressing ```ctrl+r```.
