def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b;


print "Let's do some math woth just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what        = add(age, subtract(height, multiply(weight, divide(iq, 2))))
what_inv    = subtract(age, add(height, divide(weight, multiply(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

# 1
# ====
def add_n_mul(a, b, c):
    return a + b * c

print add_n_mul(20, 3, 4)

# 2
# ====
print 35 + ( 74 - ( 180 * (50 / 2) )  )

# 3
# ====
def do_some_math(a, b, c):
    return add(a, divide(b, multiply(c, 2)))
print 30 + ( 25 / (50 * 2) )

do_some_math(30, 25, 50)
