import Control as c


def run():
    english1 = input(
        "First Period: English"
        "\nYou open your schoolbag and grab the assigned reading. Will you..."
        "\n1.Read alone like a scrub"
        "\n2.Ask Edward to read with you\n")
    # Path 1
    if english1 == "1":
        print("\nYou decide to read by yourself. Its lonely, but you do get all your work done ahead of time.\n")
        english2 = input(
            "Glancing about the room, you notice Edward's supreme intellect has allowed him to finish early as well."
            "\nYou lingers on his form for too long, he looks up and meets your eyes!"
            "\n1.ABORT! ABORT! LOOK AWAY!"
            "\n2.Steel your resolve and give him a wave"
            "\n3.Bask unashamed in the glorious gaze of his dark chestnut brown eyes.")
        if english2 == "1":
            print("The shame of being caught hangs over you. You keep your head down and don't look up again until"
                  "the bell rings. ")
        if english2 == "2":
            print("Not Finished")
            # edward waves back, small lp, leads to a conversation in the hallway
        if english2 == "3":
            print("You stare longingly into Edward's eyes. Hoping that your deepest affections can be broadcast"
                  "through this moment your sharing together."
                  "\nInstead, Edward makes a face and looks away. Stupid! You lost track of time swimming in his"
                  "chocolate fondue eyes and stared for way too long.")
            c.lp_down(1)
            # edward thinks its awkward
    # Path 2
    elif english1 == "2":
        if c.LP > 30:
            print("Some mushy line about Edward :P")
            # Add more conversation options about reading with edward
        else:
            print("Edward rejects")
            c.lp_down(1)
            print("TESTING LovePoints: " + str(c.LP))
