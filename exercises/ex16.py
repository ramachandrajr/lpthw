# Imports argv functionality from sys.
from sys import argv

# Script name and its first argument to get from argv.
script, filename = argv

# Print a few things.
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# Get data from keyboard but don't store it anywhere.
# This can be used as a neet little trick for waiting
# to hit enter since raw_input terminates at EOL
raw_input("?")

print "Opening the file..."
# Open a file and put its object in target.
target = open(filename, 'w+')

print "Trucating the file. Goodbye!"
# Truncate the target file.
# target.truncate()

print "Now I'm going to ask you for three lines."

# Get a line and store in line1.
line1 = raw_input("line1: ")
# Get a line and store in line2.
line2 = raw_input("line2: ")
# Get a line and store in line3.
line3 = raw_input("line3: ")

print "I'm going to write these to the file."

# Write line1 to the file.
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

# Close file.
target.close()

txt = open(filename, 'r')
read_file = txt.read()
print "Reading file %s:" % filename


print read_file
print

print "And finally, we close it."

# Close file.
txt.close()


# 4
# ====
# I think zed shaw himself has made it pretty clear
# that we need to use 'w' explicitly to specify write
# because open usually assumes 'r' by default.

# 5
# ====
# Write truncates the file, there is no need to do
# it explicitly.
