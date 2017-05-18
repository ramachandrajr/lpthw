people = 15
cars = 40
trucks = 15

# If variable cars > people execute this block
if cars > people:
    print "We should take the cars."
# If the above is false and this condtional is
# true execute this block.
elif cars < people:
    print "We should not take the cars."
# If none of the above are true.
else:
    print "We can't decide."


if trucks > cars and people < trucks:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

# If value in people > value in trucks execute this block
if people > trucks:
    print "Alright, let's just take the trucks."
# None of the above statements are executed then run this
# block.
else:
    print "Fine, let's stay home then."

# 1
# ====
# elif gets executed if the if statement is not executed.
