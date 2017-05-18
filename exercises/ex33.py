numbers = []

def loop_through(x, inc):
    for i in range(x):
        print "At the top i is %d" % i
        numbers.append(i)

        # We do not need this iterator anymore and
        # even if we use it the i value will be over
        # written by for loop.
        # i = i + inc
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

loop_through(10, 2)

print "The numbers: "

for num in numbers:
    print num
