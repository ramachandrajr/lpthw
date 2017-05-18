print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"


five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formla(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    # Returns 3 variabls at once not possible in
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formla(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

# Reduce start_point by ten times.
start_point = start_point / 10

print "We can also do that this way:"
# The returns from the function are put straight into the string formats.
# Ofcourse we should make sure that number of string formats match function
# returns.
print "We'd have %d beans, %d jars, and %d crates." % secret_formla(start_point)
