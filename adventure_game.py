"""A simple version of an old-fashioned text-based adventure game.

Usage: adventure_game.py

Attributes:
    ITEMS: A list of strs representing the items that the character has
        acquired (starts empty)
    ENEMIES: A list of str representing possible enemies that could be in the
        game
    ENEMY: A str representing a random selection from the ENEMIES list
"""

import random
import time

ITEMS = []
ENEMIES = ["troll", "wicked fairy", "gorgon", "dragon", "pirate"]
ENEMY = random.choice(ENEMIES)


def main():
    """Main function call, runs the adventure game."""
    intro()
    field()


def intro():
    """Prints the intro to the adventure."""
    print_pause(
        "You find yourself standing in an open field, filled with grass and "
        "yellow wildflowers"
    )
    print_pause(
        f"Rumor has it that a {ENEMY} is somewhere around here, and has been "
        "terrifying the nearby village."
    )
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause(
        "In your hand your hold your trusty (but not very effective) dagger."
    )


def field():
    """Sets the scene in a field and gives them a choice where to go next.

    1 - Go to the house
    2 - Go to the cave
    """
    print_pause("")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    choice = valid_input("(Please enter 1 or 2.)\n", ['1', '2'])
    if choice == '1':
        house()
    elif choice == '2':
        cave()


def cave():
    """Sets up the cave scene.

    The user adds a sword into their inventory unless they already have it
    """
    print_pause("You peer cautiously into the cave.")

    if 'sword' in ITEMS:
        print_pause(
            "You've been here before, and gotten all the good stuff. It's "
            "just an empty cave now."
        )
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause(
            "You discard your silly old dagger and take the sword with you."
        )
        ITEMS.append("sword")

    print_pause("You walk back out to the field.")
    field()


def house():
    """Sets up the house scene and gives them a choice to run or fight.

    1 - Fight their enemy
    2 - Run from their enemy
    """
    print_pause("You approach the door of the house.")
    print_pause(
        f"You are about to knock when the door opens and out steps a {ENEMY}."
    )
    print_pause(f"Eep! This is the {ENEMY}'s house!")
    print_pause(f"The {ENEMY} attacks you!")
    if "sword" not in ITEMS:
        print_pause(
            "You feel a bit under-prepared for this, what with only having a "
            "tiny dagger."
        )
    choice = valid_input(
        "Would you like to (1) fight or (2) run away? ",
        ['1', '2']
    )
    if choice == '1':
        fight()
    elif choice == '2':
        print_pause(
            "You run back into the field. Luckily, you don't seem to have "
            "been followed"
        )
        field()


def fight():
    """Shows the result of the fight and the endgame.

    The player wins or loses the game based on whether they have the sword in
    inventory
    """
    if "sword" in ITEMS:
        print_pause(
            f"As the {ENEMY} moves to attack, you unsheathe your new sword."
        )
        print_pause(
            "The Sword of Ogoroth shines brightly in your hand as you brace "
            "yourself for the attack."
        )
        print_pause(
            f"But the {ENEMY} takes one look at your shiny new toy and runs "
            "away!"
        )
        print_pause(
            f"You have rid the town of the {ENEMY}. You are victorious!"
        )
    else:
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the {ENEMY}.")
        print_pause("You have been defeated!")

    play_again()


def play_again():
    """Asks the player if they want to play again.

    Resets all global variables to set up for a new game
    """
    choice = valid_input("Would you like to play again? (y/n) ", ["y", "n"])
    if choice == "y":
        print_pause("Excellent! Restarting game...")
        global ITEMS, ENEMY  # pylint: disable=global-statement
        ITEMS = []
        ENEMY = random.choice(ENEMIES)
        main()
    elif choice == "n":
        print_pause("Thanks for playing! See you next time.")


def valid_input(prompt, options):
    """Validates user input, repeats the prompt on invalid valid_input.

    Args:
        prompt: A str representing the prompt a player sees
        options: A list of strs representing the allowed inputs

    Returns:
        response: A str representing the players choice
    """
    while True:
        response = input(prompt)
        if response in options:
            return response


def print_pause(message):
    """Prints a message with a 2 second delay.

    Args:
        message: A str representing the message to be displayed
    """
    print(message)
    time.sleep(2)


if __name__ == '__main__':
    main()
