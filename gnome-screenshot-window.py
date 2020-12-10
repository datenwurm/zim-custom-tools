import sys
import os
import subprocess
import time

###############################################################################
# Author: Thomas Engel <thomas.engel.web@gmail.com>
# Name: gscrotw
# Description: Takes a screenshot of a selected window
# Command: python3 gnome-screenshot-window.py "%d"
# Icon: <the path to the icon>
# [ ] Command does not modify data
# [X] Output should replace current selection
# [ ] Show in the toolbar
###############################################################################

if len(sys.argv) < 2:
	# No arguments to compute ...
	sys.exit(1)

attachment_dir = sys.argv[1]
file_name = "Screenshot_{}.png".format(time.strftime("%Y-%m-%d-%H-%M-%S"))
screenshot_file = os.path.join(attachment_dir, file_name)

try:
	# Transform input here ...
	subprocess.run(["gnome-screenshot", "-f", screenshot_file, "-w"])
	print("{{./" + file_name + "}}")
except:
	# Return the input in case of an error ...
	print(input)
