print "You enter a dark room with two doors.  Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake sitting next to a wooden door.  What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    print "3. Taunt the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off.  Good job!"
    elif bear == "2":
        print "The bear eats your legs off.  Good job!"
    elif bear == "3":
        print "Bear run towards you, you slide to the left and go behind the",
        print "bear and get out through wooden door!"
        print "Yaay! Now there are three doors: "
        print "1. A wooden door"
        print "2. A silver door"
        print "3. A golden door"
        print "Which one do you choose?"
        raw_input("> ")

        # :p
        if 1 == 1:
            print "You enter a new universe with no ends. You see a giant",
            print "creature moving towards you at a fast pace. You scratch",
            print "your head only to find a huge sword on your back. Wooow!"
            print "What'd you do?"
            print "1. Chop its legs off using the sword."
            print "2. Use your special powers to take control over the Monster."
            action = raw_input("> ")

            if action == "1":
                print "You chopped its legs off and all of a sudden it started",
                print "to grow back those!, Whoopsie!!"
                print "What'd you like to do: "
                print "1. Run"
                print "2. Chop of its legs again!"

                run = raw_input("> ")
                if run == "1":
                    print "You run into infinity and die of old age!",
                    print "Cheers to that!"
            elif action == "2":
                print "You got super powers, what are you doctor strange?",
                print "The big monster eats you and goes away for a drink!"
                print "Great job!"



    else:
        print "Well, doing %s is probably better.  Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello.  Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck.  Good job!"

else:
        print "You stumble around and fall on a knife and die.  Good job!"
