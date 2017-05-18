# Imports features
from sys import argv

# Unpacks script name and filename.
script, filename = argv

# Opens file and puts it in txt, we cam run functions
# over this.
txt = open(filename)

# Outputs file name.
print "Here's your file %r:" % filename
# reads the whole file.
print txt.read()

# Prints out filename.
print "Type the filename again:"
# Read filename in as a string.
file_again = raw_input("> ")

# Open file again and put it in txt_again variable.
txt_again = open(file_again)

# Read from the text file.
print txt_again.read()

# Closing
txt.close()
txt_again.close()
