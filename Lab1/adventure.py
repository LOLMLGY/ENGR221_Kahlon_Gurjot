"""
Name: The princess rescue...
Last updated: 9/6/26
Description: A humble text adventure game where the player must rescue Ally the Golden Gator from the Spartans.
"""

def adventure():
    """ This function runs one session of a choose your own adventure.
        Arguments: None
        Returns: None (Printed text is not returned)
    """

    print()

    print("Welcome, worthy adventurer, to The Swamp,")
    print("home to Ally the Golden Gator and sourdough bread!")

    print()

    player_name, player_class = create_player()

    print()
    
    if player_class == "Warrior":
        health = 100
        mana = 50
        print("A brave warrior, ready to confront any challenge.")
    elif player_class == "Mage":
        health = 50
        mana = 100
        print("A cunning mage, capable of outwitting the strongest foe.")

    print()

    print("Here are your beginning stats:")
    print("Health: {}".format(health))
    print("Mana: {}".format(mana))

    print()

    print(player_name, "your quest is to rescue Ally from the Spartans")
    print("who hold her captive.")
    print("Let us begin...")

    print()

    print("It's dusk. The swamp is quiet save for the crickets and frogs. Oh and the loud Spartan camp, of course.")
    print("A single dimly lit path leads to the gate, but the reeds")
    print("along the swamp's edge look thick enough to conceal your body.")
 
    approach = input("Do you [sneak] through the reeds or [charge] the gate? ").strip().lower()
 
    if approach == "sneak":
        print()
        print("You creep through the reeds, mud soaking your boots. But hey! Atleast you don't have to fight the guards?")
        if player_class == "Mage":
            mana -= 10
            print("You spend a bit of mana keeping an invisibility spell active.")
            print("Mana: {}".format(mana))
        else:
            health -= 5
            print("A stray thorn bush scrapes you as you pass.")
            print("Health: {}".format(health))
        print("You slip past the guards unseen.")
    else:
        print()
        print("You charge the gate, shouting a battle cry!")
        health -= 20
        print("The guards see your attempt and stab you with a spear.")
        print("Health: {}".format(health))
        print("Still, your stupid cry scatters them, and the gate falls open.(Though out of fear or pity, we may never know.)")
 
    print()

        # If the approach cost too much health, the adventure can end early.
    if health <= 0:
        print("You collapse before ever reaching Ally's cage.")
        print("Your journey ends here, but perhaps another adventurer")
        print("will succeed where you could not...")
        print("Wait how did you even do this, i dont think i coded that much loss before this point, but hey, you did it. Congrats?")
        print()
        return 0
 
    # --- Decision point 2: dealing with the guard blocking Ally's cage ---
    print("Inside the camp, a lone guard stands watch over a cage of steel, and somehow she's got a purple chair?")
    print("Ally chitters softly from within, waiting for you, and bored. Got a card game for later?")
 
    if player_class == "Mage" and mana >= 20:
        choice = input("Do you [fight] the guard or cast a [spell] to distract him? ").strip().lower()
    else:
        choice = input("Do you [fight] the guard or try to [sneak] past him? ").strip().lower()
 
    if choice == "spell" and player_class == "Mage" and mana >= 20:
        mana -= 20
        print()
        print("You weave a shimmering illusion of a fleeing rabbit.")
        print("The guard runs in the opposite direction, leaving the cage unguarded.")
        print("How did you know he had a deathly fear of rabbits?")
        print("Mana: {}".format(mana))
    elif choice == "fight":
        print()
        print("Steel meets steel as you duel the guard!")
        print("And if you were a mage, good job at phyical combat, but you probably should have used a spell.")
        health -= 15
        print("You land the final blow and the guard falls.")
        print("Health: {}".format(health))
    else:
        print()
        print("You wait for the guard to turn, then dash past him.")
        print("Ok, dont choose the options i give you, see if i care!")
        health -= 5
        print("He nearly spots you, but you make it to the cage.")
        print("Oop, i do care. You take a hit from the guard's spear. and he also coated it with pure fentynal.")
        print("The second the spear scrapes your skin, you fold in place and die. screw you.")
        health -= 100000
        print("how about you follow the given choices you dick.")
        print("Health: {}".format(health))
        return 0
 
    print()
 
    if health <= 0:
        print("Your wounds finally catch up to you.")
        print("You fall just steps away from Ally's cage.")
        print()
        return 0
 
    # --- Ending: free Ally and escape ---
    print("You pry open the cage, and Ally waddles out, delighted!")
    print("Together, you make a run for the swamp's edge.")
    print("and you princess carry her because you'll be damned if you dont aura farm saving her.")
 
    print()
    print("Final stats -- Health: {}, Mana: {}".format(health, mana))
    print()
 
    if health >= 60:
        print("You and Ally burst out of the swamp mist together,")
        print("triumphant and barely winded. The Spartans never")
        print("catch sight of you again. Ally is home, safe and sound.")
        print()
        print("*** VICTORY! You have rescued Ally the Golden Gator! ***")
        print()
        return 1
    else:
        print("You and Ally limp out of the swamp, exhausted but free.")
        print("Word spreads of your daring rescue, though you'll need")
        print("weeks of rest before your next adventure.")
        print()
        print("*** You rescued Ally, but at a heavy cost. ***")
        print()
        return 1


def create_player():
    """ Prompts the user for their name and class.
        Arguments: None
        Returns:
            - player_name (string): Name of the player
            - player_class (string): Class of the player
    """

    player_name = input("Before we begin, what should I call you? ")
    player_class = input("What is your specialty? [Warrior / Mage] ")

    return player_name, player_class

win = 0
while win == 0:
    win = adventure()