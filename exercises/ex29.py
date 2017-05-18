people = 200
cats = 30
dogs = 15


if people < cats or 2 != 2:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"


dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."


if people == dogs:
    print "People are dogs."

# 1
# ====
# If statement is executed if the condition next to
# it true.

# 2
# ====
# Thats how you represent a block of code in python,
# indentation. So, the block of code indented under if
# will only be executed if the condition is true.

# 3
# ====
# Interpreter throws an error incase there is no indented line below ':'
