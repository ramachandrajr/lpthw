from sys import exit


def save_princess():
    print "You observe a tiny little crown on top of bear's head. You wonder if",
    print "bear is the actual princess?! What do you do?"

    choice = raw_input("> ")

    if choice == "kill princess":
        print "Nice guess. The princess you saw was a witch who cursed the actual",
        print "princess to turn into a bear. The bear turns into a princess, you ",
        print "get back to the castle and live happily ever after! Wait, You got a castle",
        print "right? "
        exit(0)
    elif choice == "run away with princess":
        print "Whoopsie!, The bear is the princess. The princess is the witch. The",
        print "witch takes her original form and kills you with her wand!"
        dead("You die anyways")

def kill_bear():
    print "She wakes up and explains that bear has kept her prisoner.",
    print "She asks you to kill it! You go back into its room and find a sword."
    print "What do you do?"

    message_conveyed = False

    while True:
        choice = raw_input("> ")

        if choice == "kill bear" and message_conveyed == False:
            message_conveyed = True
            print "The bear puts its head down and starts growling in fear",
            print "What do you do?"
        elif choice == "kill bear" and message_conveyed == True:
            print "Bear stands up and slaps your face off"
            dead("You die for no reason!")
        elif "leave" in choice or "don't kill" in choice:
            save_princess()
        else:
            print "What did you say?"


def princess():
    print "You see a princess lying in there. She seems unconcious.",
    print "What do you do? "

    choice = raw_input("> ")

    if choice == "wake her up":
        kill_bear()
    elif choice == "leave her alone":
        print "You get out of the castle and live happily ever after with your",
        print "riches. Princess dies, thanks for not helping pervert!"
        exit(0)
    else:
        print "I didn't understand."
        princess()

def gold_room():
    print "This room is full of gold.  How much do you take?"

    choice = raw_input("> ")

    try:
        how_much = int(choice)
    except ValueError:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        princess()
    else:
        dead("You greedy bastard!")

def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your faceoff.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed offand chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You wake up in a dark room, no light anywhere. You situp to see a",
    print "door upstraight in ambient light and a way into a pit down below ",
    print "!! with a locked entrance !! But you got the key in your pocket."
    print "Which way do you go?"

    choice = raw_input("> ")

    if "straight" in choice:
        cthulhu_room()
    elif "below" in choice or "pit" in choice:
        bear_room()
    else:
        print "What?!"
        start()


start()
