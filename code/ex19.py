# Function with two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Prints cheese count
    print "You have %d cheeses!" % cheese_count
    # Prints crackers
    print "You have %d boxes of crackers!" % boxes_of_crackers
    # Prints stuff
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# Print some
print "We can just give the function members directly:"
# Calls a function with arguments.
cheese_and_crackers(20, 30)



print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# 2
# ====
def print_name(first, last):
    print "Hi there %s %s" % (last, first)

adj = "The awesomeness"
adj1 = raw_input("Gimme an adjective")

adj2 = adj + " and " + adj1 + " and The best of the best"

print_name("Rj", "Hero")
print_name("Rj", adj)
print_name("Rj", adj1)
print_name("Rj", adj + " and " + adj1)
print_name("Rj", adj2)
print_name("Rj", adj + adj1)
print_name("Rj", "")
print_name("Rj", str(11 + 22))
print_name("Rj", "All day" + adj)
print_name("Rj", "no. %s" % str(11 + 22))
