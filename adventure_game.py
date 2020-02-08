import random
import time

items = []
enemies = ["troll", "wicked fairie", "gorgon", "dragon", "pirate"]
enemy = random.choice(enemies)


def main():
    intro()
    field()


def intro():
    print_pause(
        "You find yourself standing in an open field, filled with grass and "
        "yellow wildflowers"
    )
    print_pause(
        f"Rumor has it that a {enemy} is somewhere around here, and has been "
        "terrifying the nearby village."
    )
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause(
        "In your hand your hold your trusty (but not very effective) dagger."
    )


def field():
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
    print_pause("You peer cautiously into the cave.")

    if 'sword' in items:
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
        items.append("sword")

    print_pause("You walk back out to the field.")
    field()


def house():
    print_pause("You approach the door of the house.")
    print_pause(
        f"You are about to knock when the door opens and out steps a {enemy}."
    )
    print_pause(f"Eep! This is the {enemy}'s house!")
    print_pause(f"The {enemy} attacks you!")
    if "sword" not in items:
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
    if "sword" in items:
        print_pause(
            f"As the {enemy} moves to attack, you unsheath your new sword."
        )
        print_pause(
            "The Sword of Ogoroth shines brightly in your hand as you brace "
            "yourself for the attack."
        )
        print_pause(
            f"But the {enemy} takes one look at your shiny new toy and runs "
            "away!"
        )
        print_pause(
            f"You have rid the town of the {enemy}. You are victorious!"
        )
    else:
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the dragon.")
        print_pause("You have been defeated!")

    play_again()


def play_again():
    choice = valid_input("Would you like to play again? (y/n) ", ['y', 'n'])
    if choice == 'y':
        print_pause("Excellent! Restarting game...")
        global items, enemy
        items = []
        enemy = random.choice(enemies)
        main()
    elif choice == 'n':
        print_pause("Thanks for playing! See you next time.")


def valid_input(prompt, options):
    while True:
        response = input(prompt)
        if response in options:
            return response


def print_pause(message):
    print(message)
    time.sleep(2)


if __name__ == '__main__':
    main()
