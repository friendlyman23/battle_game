import os
import random
import sys


class Character:
    def __init__(self, which_character):
        self.is_dead = False
        if which_character == 1:
            self.name = "Wizard"
            self.hp = 70
            self.damage = 150
        if which_character == 2:
            self.name = "Elf"
            self.hp = 100
            self.damage = 100
        if which_character == 3:
            self.name = "Puny Human"
            self.hp = 1
            self.damage = 0
        if which_character == 4:
            self.name = "Dragon"
            self.hp = 300
            self.damage = 50

    def kill(self, opponent):
        opponent.is_dead = True
        print(f"A devastating blow!!")
        input("(Press ENTER or RETURN to continue.)")

    def attack(self, opponent):
        if self.name == "Wizard":
            print(
                f"You attack with Whip of Dragonsbane Lightning! {opponent.name} takes {self.damage} damage!"
            )
        elif self.name == "Elf":
            print(
                f"You attack with Elendaar's Bow! {opponent.name} takes {self.damage} damage!"
            )
        elif self.name == "Puny Human":
            print(f"You throw a rock! {opponent.name} takes {self.damage} damage!")
        else:
            print(f"{self.name} attacks! Player takes {self.damage} damage!")
        opponent.hp -= self.damage
        if opponent.hp <= 0:
            self.kill(opponent)

        else:
            if self.name == "Dragon":
                print(f"You have {opponent.hp} HP remaining.")
            else:
                print(f"Dragon has {opponent.hp} HP remaining.")
            input("(Press ENTER or RETURN to continue.) ")


def get_player_character():

    while True:
        character = input("What is your choice? (Enter 1-3) ")
        try:
            character = int(character)
            if int(character) not in range(1, 4):
                input("You must enter 1, 2 or 3. Press ENTER or RETURN to continue. ")
                continue
            else:
                return Character(character)
        except ValueError:
            print("Please enter 1, 2 or 3 and press ENTER or RETURN on your keyboard. ")
            continue


def roll_dice():

    roll = random.randint(1, 6)

    # dice top row 1
    print("    --------")

    # dice top row 2
    print(
        f"  / {'o' if roll == 1 else ' '} {'o' if roll in [2, 3, 4, 5, 6] else ' '}    /|"
    )

    # dice top row 3
    print(f" /      {'o' if roll == 1 else ' '} /{'o' if roll in [1, 2] else ' '}|")

    # dice corner
    print(f" ---------o |")

    # dice front row 1
    print(
        f"| {'o'if roll in [2, 3, 4, 5, 6] else ' '}    {'o' if roll in [4, 5, 6] else ' '} |  |"
    )

    # dice front row 2
    print(
        f"| {'o'if roll == 6 else ' '} {'o' if roll in [1, 3, 5] else ' '}  {'o' if roll == 6 else ' '} | o|"
    )

    # dice front row 3
    print(
        f"| {'o'if roll in [4, 5, 6] else ' '}    {'o' if roll in [2, 3, 4, 5, 6] else ' '} |{'o' if roll in [1, 2] else ' '}/"
    )
    # dice bottom corner
    print(" ---------")

    print(f"The dice shows a {roll}!")
    input("(Press ENTER or RETURN to continue) ")

    return roll


def roll_phase(turn, o_player, o_dragon):
    if turn == 1:

        print(
            "The custom of this land dictates that the order of combat be defined by the roll of the Holy Numbered Cube!!"
        )
    else:
        print("Roll that di-that cube!!!")
    input("Press ENTER or RETURN to roll the dice. ")
    while True:
        print("Player's roll!")
        player_roll = roll_dice()

        os.system("cls" if os.name == "nt" else "clear")

        print("The dragon will now roll!")
        input("(Press ENTER or RETURN to continue.)")
        dragon_roll = roll_dice()

        print(f"You rolled a {player_roll}! The dragon rolled a {dragon_roll}!")
        if player_roll == dragon_roll:
            print("It's a tie! Roll again!")
            input("(Press ENTER or RETURN to continue.)")
            os.system("cls" if os.name == "nt" else "clear")
            continue
        elif player_roll > dragon_roll:
            print("The player will attack first!")
            input("(Press ENTER or RETURN to continue.)")
            return [o_player, o_dragon]
        else:
            print("The dragon will attack first!")
            input("(Press ENTER or RETURN to continue.)")
            return [o_dragon, o_player]


def combat(attacker, defender):
    attacker.attack(defender)
    os.system("cls" if os.name == "nt" else "clear")


def play_game():

    print("Welcome to DeathBattle IV!!!! Choose your character!")
    print("1: Wizard")
    print("2: Elf")
    print("3: Puny Human")

    oPlayer = get_player_character()
    oDragon = Character(4)

    os.system("cls" if os.name == "nt" else "clear")

    turn = 1

    print(
        "An incessant tugging at your shoulder finally rouses you to consciousness. Were you asleep? Judging from the splitting pain at the back of your head and a dull ringing in your ears, no -- you were knocked out."
    )
    print()
    input("(Press ENTER or RETURN to continue.)")
    print()
    print(
        "Your vision swims into view, and before you is a toothless grin on a pockmarked face. The stinking attendant, dragging you bodily from the stone floor to your feet, dumps the contents of a bucket of fetid water over your head."
    )
    input("(Press ENTER or RETURN to continue.)")
    print()
    print(
        '"Nice nappy time?" the attendant leers. But before you can respond, they shove you forward and out of the cell. "Nappy time over. Now play time!" the wheezing voice adds, laughing.'
    )
    print()
    input("(Press ENTER or RETURN to continue.)")
    print()
    print(
        "Stumbling forward, you pass through the cell door and into the blinding sunshine. The thousands of onlookers in this giant arena greet you with jeers, insults and a hail of thrown refuse. But you barely notice, for staring at you from across the colosseum floor, nostrils flaring, teeth gnashing, wings flexing, is...A DRAGON!!"
    )

    print()
    input("(Press ENTER or RETURN to continue.)")
    print()
    print(
        'The echoing voice of the announcer finds your ears through the din of the crowd. "Welcome one and all! Prepare for a thrilling battle to the death! Only one fighter leaves this arena alive!"'
    )
    print()
    input("(Press ENTER or RETURN to continue.)")
    print()

    while True:

        os.system("cls" if os.name == "nt" else "clear")
        attack_order = roll_phase(turn, oPlayer, oDragon)

        os.system("cls" if os.name == "nt" else "clear")

        combat(attack_order[0], attack_order[1])

        if attack_order[1].is_dead:
            print(f"The {attack_order[1].name} has died!")
            input("(Press ENTER or RETURN to continue.)")
            return attack_order[0]
        else:
            combat(attack_order[1], attack_order[0])
            if attack_order[0].is_dead:
                print(f"The {attack_order[0].name} has died!")
                input("(Press ENTER or RETURN to continue.)")
                return attack_order[1]
        print(
            f"At the end of round {turn}, the player has {oPlayer.hp} HP remaining! The dragon has {oDragon.hp} HP remaining. We commence round {turn + 1}!"
        )
        input("(Press ENTER or RETURN to continue.)")
        turn += 1


while True:

    winner = play_game()
    if winner.name == "Dragon":
        print("You lose!")
    else:
        print("You win!")
    input("(Press ENTER or RETURN to quit the game.)")
    sys.exit()
