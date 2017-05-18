# Import argv to get arguments
from sys import argv

# Unpacking
script, input_file = argv

# A function to print the whole file.
def print_all(f):
    print f.read()
    # read is used to read the whole file.

# Function with a single argument
def rewind(f):
    # Sets pointer to the start of the file.
    f.seek(0)

# RJ
# =====
def seek(num, f):
    f.seek(num)


# function that takes two arguments
def print_a_line(line_count, f):
    # Prints first argument and then reads a
    # single line from file.
    print line_count, f.readline()

# Open a file.
current_file = open(input_file)

print "First let's print the whole file:\n"
# Prints the whole file.
print_all(current_file)

print "Now let's rewind, kind of like a tape."
# Takes the file poiter to the start
rewind(current_file)

print "Let's print three lines:"

# We'll print First line number as 1
current_line = 1
# Prints line number and the line
print_a_line(current_line, current_file)

# Increment current line number
# current_line = 2
current_line =+ 1
# Prints line number and the line
print_a_line(current_line, current_file)

seek(current_file.tell() + 10, current_file)

# Increment current line number
# current_line = 3
current_line =+ 1
# Prints line number and the line
print_a_line(current_line, current_file)

# 5
# ====
# x+=n is used as a short hand notation of x = x + n
