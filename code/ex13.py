from sys import argv

script, first, second, third = argv

print "This script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# 1
# ====
# It means that we can not unpack argv into less 
# variables.

# 2
# ====
## Script with more arguments
# script, arg1, arg2, arg3, arg4 = argv

# print "The first argument is:", arg1
# print "The Second argument is:", arg2
# print "The third argument is:", arg3
# print "The fourth argument is:", arg4

## Script with less arguments
# script_name, first_name, last_name = argv

# print "Your first name is:", first_name
# print "Your last name is:", last_name

# 3
# ====
name = raw_input("What is your name? ")
age = raw_input("What is your age? ")
weight = raw_input("How much do you weigh? ")

print "Hi %r, you are %r years old and you weigh %r" % (
	name, age, weight)

# 4
# ====
