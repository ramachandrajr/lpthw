# String with formatters is filled in with a number and saved on to a variable.
x = "There are %d types of people." % 10
# Saving a string to binary variable
binary = "binary"
# Saving the word "don't" to the variable don_t
do_not = "don't"
# Using formatters as before but now we got two formatters, so we have to put
# them in parens seperated by commas.
y = "Those who know %s and those who %s." % (binary, do_not)

# Print x
print x
# and y
print y

# Print string with formatter 'r'. r formatter is used to print anything the way
# it is rightaway. It will print variables of any types.
print "I said: %r." % x
# Same as above.
print "I also said: '%s'." % y

# Assigning boolean to a variable.
hilarious = True
# Saving a string with formatters un evaluated to a variable.
joke_evaluation = "Isn't that a joke so funny?! %r"

# Print the unevaluated string filling in its formatters with what ever is in
# hilarious.
print joke_evaluation % hilarious

# Two strings
w = "This is the left side of..."
e = "a string with a right side."

# Print two strings concated to each other.
print w + e
