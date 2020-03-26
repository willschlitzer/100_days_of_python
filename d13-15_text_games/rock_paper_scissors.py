from rps_classes import Player, Roll
import random

BEST_OF = 3


def main():
    print("Time for some Rock, Paper Scissors!")
    print()
    player_name = input("What is your name?: ")
    game_loop(player_name=player_name)


def game_loop(player_name):
    computer_player = Player("Compy")
    human_player = Player(player_name)
    game_ongoing = True
    to_win = BEST_OF / 2
    available_rolls = ["rock", "paper", "scissors"]
    while game_ongoing:
        print()
        print(
            "Score: {} {} : Computer {}".format(
                human_player.name, human_player.score, computer_player.score
            )
        )
        print()
        valid_roll = True
        player_roll = input("Do you roll [r]ock, [p]aper, or [s]cissors? ")
        if player_roll == "r":
            roll = Roll("rock")
        elif player_roll == "s":
            roll = Roll("scissors")
        elif player_roll == "p":
            roll = Roll("paper")
        else:
            print("Not a valid roll")
            valid_roll = False
        if valid_roll:
            computer_roll = random.choice(available_rolls)
            if computer_roll == roll.roll_name:
                print("You both rolled {}".format(computer_roll))
            elif computer_roll == roll.wins:
                print(
                    "Your {} beat the computer's {}".format(
                        roll.roll_name, computer_roll
                    )
                )
                human_player.score += 1
            elif computer_roll == roll.loses:
                print(
                    "Your {} lost to the computer's {}".format(
                        roll.roll_name, computer_roll
                    )
                )
                computer_player.score += 1
            if computer_player.score > to_win:
                print()
                print("The computer wins! Better luck next time")
                game_ongoing = False
            elif human_player.score > to_win:
                print()
                print("You win! Congratulations {}!".format(human_player.name))
                game_ongoing = False
    again = input("Play again? y/n ")
    if again.lower() == "y":
        game_loop(player_name=player_name)


if __name__ == "__main__":
    main()
